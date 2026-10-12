# Tejweb Studio

Static website + Supabase backend.

- `index.html`: public site (portfolio, services, 4-step inquiry form saved to Supabase)
- `admin.html`: admin panel (login, dashboard, inquiries, clients, projects, payments)
- `supabase/migrations/`: SQL for the database, tables and Row Level Security
- `ADMIN-SETUP.md`: how to create the first administrator

## Deploy (static hosting: Netlify, Vercel, GitHub Pages)
1. Upload the repo as-is (no build step). `index.html` is the home page, `admin.html` is at `/admin.html`.
2. Supabase project `ceqmbxgwfjkcemzfoime` already has migrations 001 and 002 applied. For a NEW project, run them in order in the SQL Editor and update the URL and key at the top of both HTML scripts.
3. Follow `ADMIN-SETUP.md` to authorize your admin account and disable public sign-ups.

## Secrets
Only the public URL and publishable key are in the HTML. Never commit a `service_role` / secret key or database password. Server-side keys (if added later) go in environment variables, see `.env.example`.

## Status
Database security tested via SQL simulation. Browser flows (inquiry submit, admin login, CRUD) still need testing on the hosted site.
