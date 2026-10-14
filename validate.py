import re,json,glob,os,sys
D="https://tejwebstudio.online";bad=[]
pages={"index.html":D+"/"};
for p in glob.glob("services/*/index.html"):pages[p]=D+"/"+os.path.dirname(p)+"/"
for p,url in pages.items():
    s=open(p).read();body=re.sub(r"<script.*?</script>","",s,flags=re.S)
    def one(pat,name):
        n=len(re.findall(pat,s,re.S))
        if n!=1:bad.append(f"{p}: {name} count={n}")
    if len(re.findall(r"<style>(.{500,}?)</style>",s,re.S))<1:bad.append(p+": no inline CSS")
    if re.search(r'<link rel="stylesheet" href="/',s):bad.append(p+": depends on external local stylesheet")
    one(r"<title>[^<]+</title>","title");one(r'<meta name="description" content="[^"]{60,170}"',"meta description (60-170 chars)");n1=len(re.findall(r"<h1[ >]",body))
    if n1!=(2 if p=="index.html" else 1):bad.append(f"{p}: h1 count={n1}")
    m=re.search(r'<link rel="canonical" href="([^"]+)"',s)
    if not m or m.group(1)!=url:bad.append(f"{p}: canonical {m and m.group(1)} != {url}")
    if "netlify.app" in s:bad.append(p+": netlify.app reference")
    for j in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):
        try:json.loads(j)
        except Exception as ex:bad.append(p+": bad JSON-LD "+str(ex))
    for h in re.findall(r'href="(/[^"#?]*)',body):
        t=h.lstrip("/")
        if h=="/":continue
        if not(os.path.exists(t) or os.path.exists(t+"index.html") or os.path.exists(t.rstrip("/")+"/index.html")):bad.append(f"{p}: broken link {h}")
from html.parser import HTMLParser
VOID={"meta","link","img","br","input","hr","source"}
class P(HTMLParser):
    def __init__(s):super().__init__();s.st=[];s.err=[]
    def handle_starttag(s,t,a):
        if t not in VOID:s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID:return
        if not s.st or s.st[-1]!=t:s.err.append(f"unexpected </{t}> (open: {s.st[-3:]})")
        else:s.st.pop()
for p in pages:
    b=re.sub(r"<script.*?</script>","",open(p).read(),flags=re.S);b=re.sub(r"<style.*?</style>","",b,flags=re.S);pp=P();pp.feed(b)
    if pp.err or pp.st:bad.append(f"{p}: tag balance {pp.err[:2]} unclosed={pp.st}")
ix=open("index.html").read();ib=re.sub(r"<script.*?</script>","",ix,flags=re.S)
ids=set(re.findall(r'id="([^"]+)"',ib));ROUTES={"start-project","privacy","terms","refunds"}
for h in re.findall(r'href="#([^"]*)"',ib):
    name=h.split("?")[0]
    if h=="" or (name.startswith("/") and name.lstrip("/") in ROUTES|{""}) or name in ids:continue
    bad.append("index.html: dead hash link #"+h)
sm=open("sitemap.xml").read()
for u in re.findall(r"<loc>([^<]+)</loc>",sm):
    if not u.startswith(D):bad.append("sitemap wrong domain "+u)
    t=u[len(D):].lstrip("/")
    if t and not os.path.exists(t+"index.html"):bad.append("sitemap url without file "+u)
if "tejwebstudio.online" not in open("robots.txt").read():bad.append("robots sitemap")
t=[re.search(r"<title>([^<]+)",open(p).read()).group(1) for p in pages]
if len(set(t))!=len(t):bad.append("duplicate titles")
print("ISSUES:" if bad else "all checks passed",*bad,sep="\n")
