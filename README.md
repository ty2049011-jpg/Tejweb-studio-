# Tejweb Studio

Static site (Netlify) + Supabase backend.

- `index.html` public site: services, demo portfolio, pricing, cost calculator, 6-step inquiry form, FAQ, contact, legal templates
- `admin.html` admin panel: login, dashboard, inquiries (status, notes, estimated budget, CSV export), clients, projects, payments, Content editor (pricing, calculator, contact, FAQs, testimonials)
- `supabase/migrations/` run 001, 002, 003 in order (already applied to project ceqmbxgwfjkcemzfoime)
- `supabase/first_admin.sql.example` authorize your admin (see ADMIN-SETUP.md)
- `404.html`, `robots.txt`, `sitemap.xml`, `netlify.toml`

## Deploy on Netlify
Drag the folder into Netlify, or connect the repo. No build step; publish directory is `.`.

## Secrets
Only the Supabase URL and publishable key are in the HTML. Never commit a service_role/secret key or DB password.

## Not built yet
Client login portal, portfolio image upload and project editor, email notifications, per-client pages. Portfolio shows labelled demo projects only.
