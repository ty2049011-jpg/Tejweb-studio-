import re,json,glob,os,sys
D="https://tejwebstudio.online";bad=[]
pages={"index.html":D+"/"};
for p in glob.glob("services/*/index.html"):pages[p]=D+"/"+os.path.dirname(p)+"/"
for p,url in pages.items():
    s=open(p).read();body=re.sub(r"<script.*?</script>","",s,flags=re.S)
    def one(pat,name):
        n=len(re.findall(pat,s,re.S))
        if n!=1:bad.append(f"{p}: {name} count={n}")
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
sm=open("sitemap.xml").read()
for u in re.findall(r"<loc>([^<]+)</loc>",sm):
    if not u.startswith(D):bad.append("sitemap wrong domain "+u)
    t=u[len(D):].lstrip("/")
    if t and not os.path.exists(t+"index.html"):bad.append("sitemap url without file "+u)
if "tejwebstudio.online" not in open("robots.txt").read():bad.append("robots sitemap")
t=[re.search(r"<title>([^<]+)",open(p).read()).group(1) for p in pages]
if len(set(t))!=len(t):bad.append("duplicate titles")
print("ISSUES:" if bad else "all checks passed",*bad,sep="\n")
