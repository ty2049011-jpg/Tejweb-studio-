import json,os,html,re
D="https://tejwebstudio.online"
e=html.escape
S=[
("business-website-development","Business Website Development","Business Website","Business Website Development Services | Tejweb Studio","Professional business website development by Tejweb Studio: responsive, fast, SEO-friendly websites that present your company and bring in enquiries.",
 "Business Website Development","A business website is often the first place customers check before they contact you. Tejweb Studio designs and builds responsive business websites that explain what you do clearly and make it easy to get in touch.",
 ["Small and growing businesses that need a professional online presence","Professionals and consultants who want a website for their services","Companies replacing an outdated or non-mobile-friendly site"],
 ["Clear home, services, about and contact pages","Contact form and WhatsApp contact button","Mobile-first responsive layout","Basic on-page SEO setup: titles, descriptions and headings","Deployment assistance"],
 [("How many pages does a business website need?","Many small business sites use around five pages: home, services, about, contact and one more. The right number depends on your content. The Professional package covers up to five pages."),("Are domain and hosting included?","No. Domain, hosting and paid integrations are separate costs. Deployment assistance is part of the packages."),("How do I get a quote?","Send your requirements through the project form or try the cost calculator. The final scope and price are agreed in writing before work starts.")],
 ["landing-page-development","website-maintenance","e-commerce-website-development"]),
("e-commerce-website-development","E-commerce Website Development","E-commerce Website","E-commerce Website Development | Tejweb Studio","E-commerce website development by Tejweb Studio: online store layouts with product pages, cart and checkout flow, built to be responsive and easy to manage.",
 "E-commerce Website Development","An online store needs more than a good-looking homepage. Tejweb Studio builds e-commerce websites with clear product pages and a straightforward path from browsing to checkout.",
 ["Businesses that want to sell products online","Existing shops that want a website of their own","Brands that need a store tailored to their catalogue"],
 ["Product and category pages","Cart and checkout flow","Mobile-first shopping experience","Room to add and change products","Payment and delivery integrations scoped during requirements"],
 [("Can you connect a payment gateway?","Payment and delivery integrations are discussed during requirements and may cost extra. Nothing is added to your store without agreeing it first."),("How long does an online store take?","It depends on the number of products and features. You state your preferred timeline in the project form and receive a realistic one with your quote."),("What does it cost?","E-commerce sites vary widely in scope. Use the cost calculator for an estimate, then request a custom quote.")],
 ["business-website-development","custom-web-applications","website-maintenance"]),
("landing-page-development","Landing Page Development","Landing Page","Landing Page Development | Tejweb Studio","Landing page development by Tejweb Studio: a single, fast, focused page built around one clear action, such as enquiries, sign-ups or WhatsApp contact.",
 "Landing Page Development","A landing page does one job: it moves a visitor toward a single action. Tejweb Studio builds fast, focused landing pages for campaigns, launches and services.",
 ["Businesses running ads or campaigns","Freelancers and service providers who need one strong page","Teams launching a product or offer"],
 ["One focused page with a clear call to action","Contact form or WhatsApp button","Fast-loading, responsive layout","Basic on-page SEO setup","Deployment assistance"],
 [("What is the difference between a landing page and a website?","A landing page is a single page with one goal. A website has several pages that cover your business more broadly."),("Can I add more pages later?","Yes. A landing page can grow into a full business website when you are ready."),("How do I get started?","Send your requirements through the project form. The Starter package is a one-page website.")],
 ["business-website-development","portfolio-website-development","website-maintenance"]),
("portfolio-website-development","Portfolio Website Development","Portfolio Website","Portfolio Website Development | Tejweb Studio","Portfolio website development by Tejweb Studio: clean, responsive sites that show your work, build your personal brand and make you easy to contact.",
 "Portfolio Website Development","A portfolio website shows your work in your own words and layout. Tejweb Studio builds responsive portfolio sites for creatives and professionals who want to be found and contacted.",
 ["Designers, photographers and other creatives","Freelancers and consultants","Professionals who want a personal website"],
 ["Project or work gallery","About and contact sections","Personal branding that fits your style","Mobile-first responsive layout","Easy to update"],
 [("What content should I prepare?","Your best work, a short introduction, contact details and any logo or colours you already use. We can help fill gaps."),("Can I update the portfolio myself later?","We can build the site so you can edit content yourself, or you can ask us to make updates."),("How do I get a quote?","Use the project form or cost calculator. The final scope and price are agreed before work begins.")],
 ["landing-page-development","business-website-development","website-maintenance"]),
("custom-web-applications","Custom Web Applications","Custom Web Application","Custom Web Application Development | Tejweb Studio","Custom web application development by Tejweb Studio: dashboards, portals and tools with secure logins and a database, built around your workflow.",
 "Custom Web Applications","Some needs do not fit a standard website. Tejweb Studio builds custom web applications such as dashboards, booking tools and client portals, shaped around how your business works.",
 ["Businesses with a specific workflow to digitise","Teams that need a dashboard or admin panel","Startups building a first version of a product"],
 ["Secure logins and access control","Database-backed features","Dashboards and admin panels","Built to an agreed scope","Technology chosen to fit the project"],
 [("What kinds of applications can you build?","Examples include dashboards, booking systems and client portals. Describe your idea in the project form and it will be reviewed."),("How is the price decided?","Custom applications are quoted from the agreed scope. Use the project form to request a custom quote."),("Can you add features to something that already exists?","Possibly. Share the details in the project form and the options will be reviewed with you.")],
 ["business-website-development","e-commerce-website-development","website-maintenance"]),
("website-maintenance","Website Maintenance","Other","Website Maintenance Services | Tejweb Studio","Website maintenance by Tejweb Studio: content updates, bug fixes and ongoing support after launch, with the plan and price agreed in advance.",
 "Website Maintenance","A website needs care after launch. Tejweb Studio offers maintenance so updates, fixes and small improvements do not fall on you.",
 ["Businesses with an existing website that needs regular updates","Owners who do not want to manage technical changes","Sites built by Tejweb Studio that need post-launch support"],
 ["Content updates","Bug fixes","Ongoing support","Plan and price agreed before it starts"],
 [("Is maintenance included in the website price?","Maintenance is an optional extra. The plan and price are agreed before it starts."),("Do you maintain websites you did not build?","Share the details of your site in the project form and it will be reviewed case by case."),("Does maintenance include domain and hosting?","No. Domain and hosting are separate costs.")],
 ["business-website-development","landing-page-development","custom-web-applications"])]
names={s[0]:s[1] for s in S}
HEAD='''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'''+"<style>"+re.sub(r"\s+"," ",open("tools/service.css").read())+"</style>"
ORG={"@type":"Organization","@id":D+"/#org","name":"Tejweb Studio","url":D+"/","description":"Website development studio run by Tejpratap, building business websites, e-commerce sites, landing pages, portfolio sites and custom web applications.","contactPoint":{"@type":"ContactPoint","telephone":"+917595986787","contactType":"customer support"}}
for slug,name,typ,title,desc,h1,intro,who,feat,faqs,rel in S:
    url=f"{D}/services/{slug}/"
    g={"@context":"https://schema.org","@graph":[ORG,
     {"@type":"WebPage","@id":url+"#webpage","url":url,"name":title,"description":desc,"isPartOf":{"@id":D+"/#website"},"breadcrumb":{"@id":url+"#crumbs"}},
     {"@type":"Service","@id":url+"#service","name":name,"serviceType":name,"description":intro,"url":url,"provider":{"@id":D+"/#org"}},
     {"@type":"BreadcrumbList","@id":url+"#crumbs","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":D+"/"},{"@type":"ListItem","position":2,"name":name,"item":url}]},
     {"@type":"FAQPage","@id":url+"#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}]}
    q=typ.replace(" ","%20")
    page=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Tejweb Studio"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{D}/og-image.png"><meta name="twitter:card" content="summary_large_image">
{HEAD}
<script type="application/ld+json">{json.dumps(g,ensure_ascii=False)}</script></head>
<body><header><div class="w nav"><a class="logo" href="/"><i>T</i>Tejweb Studio</a><nav aria-label="Main"><a href="/#services">Services</a><a href="/#portfolio">Portfolio</a><a href="/#pricing">Pricing</a><a href="/#contact">Contact</a></nav><a class="btn pri" href="/#/start-project?type={q}">Start a Project</a></div></header>
<main><section class="hero"><div class="w"><nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a> / <span>{e(name)}</span></nav><h1>{e(h1)}</h1><p class="lead">{e(intro)}</p><div class="row"><a class="btn pri" href="/#/start-project?type={q}">Start Your Project</a><a class="btn" href="/#calculator">Estimate the cost</a></div></div></section>
<section><div class="w two"><div><h2>Who this is for</h2><ul>{"".join(f"<li>{e(x)}</li>" for x in who)}</ul></div><div><h2>What is included</h2><ul>{"".join(f"<li>{e(x)}</li>" for x in feat)}</ul></div></div></section>
<section><div class="w"><h2>How it works</h2><p>You send your requirements through the project form. They are reviewed, and a final scope and price are agreed in writing before work starts. Domain, hosting, paid integrations and additional features may cost extra. See <a href="/#pricing">pricing</a> for starting prices.</p></div></section>
<section><div class="w"><h2>Frequently asked questions</h2>{"".join(f"<details><summary>{e(a)}</summary><p>{e(b)}</p></details>" for a,b in faqs)}</div></section>
<section><div class="w"><h2>Related services</h2><div class="rel">{"".join(f'<a href="/services/{r}/">{e(names[r])}</a>' for r in rel)}</div></div></section>
<section><div class="w cta"><h2>Ready to talk about your {e(name.lower())}?</h2><a class="btn pri" href="/#/start-project?type={q}">Tell Me About Your Project</a></div></section></main>
<footer><div class="w"><p>© Tejweb Studio · <a href="/">Home</a> · <a href="/#/privacy">Privacy Policy</a> · <a href="/#/terms">Terms of Service</a> · <a href="https://wa.me/917595986787" rel="noopener noreferrer">WhatsApp</a></p></div></footer></body></html>'''
    os.makedirs(f"services/{slug}",exist_ok=True)
    open(f"services/{slug}/index.html","w").write(page)
urls=[D+"/"]+[f"{D}/services/{s[0]}/" for s in S]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{u}</loc><lastmod>2026-10-13</lastmod></url>\n" for u in urls)+"</urlset>\n")
print(len(S),"pages")
