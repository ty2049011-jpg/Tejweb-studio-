# Tejweb Studio

Static site (Netlify) + Supabase backend.

- `index.html` public site: services, demo portfolio, pricing, cost calculator, 6-step inquiry form, FAQ, contact, legal templates
- `admin.html` admin panel (login, dashboard, inquiries, clients, projects, payments, Content editor)
- `supabase/migrations/` SQL 001 to 003 (already applied to project ceqmbxgwfjkcemzfoime)
- `supabase/first_admin.sql.example` authorize your admin (see ADMIN-SETUP.md)
- `404.html`, `robots.txt`, `sitemap.xml`, `netlify.toml`

## Deploy on Netlify
Upload the whole folder contents (index.html must be at the site root). No build step.

## Secrets
Only the Supabase URL and publishable key are in the HTML. Never commit a service_role/secret key.
