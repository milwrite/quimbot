# MoltComps Landing Page

**Temp hosting:** GitHub Pages  
**Production:** TBD (moltcomps.com or custom domain)

## Structure

- `index.html` — Main landing page (Tailwind CSS via CDN)
- Pricing tiers: $49 / $199 / $499
- Demo comp pack showcase
- FAQ section
- CTA + email capture (coming soon)

## Deployment

GitHub Pages serves from this directory.

**URL:** TBD (will be `https://milwrite.github.io/quimbot/sidequests/moltcomps/site/` or custom subdomain)

## Next Steps

1. Connect Stripe checkout (replace alert placeholders)
2. Add email capture (ConvertKit or Loops)
3. Create 2 real demo comp packs (replace TechStart.com example)
4. Add analytics (Plausible or Simple Analytics)
5. Launch content marketing (SEO articles, Reddit/Quora outreach)

## Local Testing

```bash
# Serve locally
python3 -m http.server 8000
# Visit http://localhost:8000
```

## Notes

- Uses Tailwind CSS via CDN (no build step)
- Mobile-responsive
- Smooth scroll navigation
- Placeholder Stripe integration (coming soon)
