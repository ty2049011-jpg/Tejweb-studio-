# Tejweb Studio admin: setup

## Files
- `tejweb-studio-live.html` public site (unchanged except Supabase form wiring)
- `admin.html` admin panel (host it next to the public site, e.g. /admin.html). It is noindex.

## Keys
Browser files use only SUPABASE_URL and the publishable key. Never put the service_role / secret key or DB password in any HTML file. If you later add server code (email, cron), keep keys in env vars: SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY, SUPABASE_SERVICE_ROLE_KEY (server only).

## Create the first administrator (no public sign-up exists)
1. Supabase dashboard > Authentication > Users > Add user > Create new user. Enter your email + strong password, tick Auto Confirm.
2. Authentication > Sign In / Providers > Email: turn OFF "Allow new users to sign up" so nobody else can register.
3. SQL Editor, run (replace the email):
   insert into public.admin_profiles (user_id, email)
   select id, email from auth.users where email = 'YOU@EXAMPLE.COM';
4. Open admin.html and sign in. Any other account that signs in is rejected, and the database refuses its queries anyway.

## Deploy
Upload both HTML files to Netlify / Vercel / GitHub Pages (static hosting). In Supabase > Authentication > URL Configuration, set Site URL to your domain.
