# Project Isabel Startup Website 1.0 Foundation

A complete static rebuild of Project Isabel's public startup website. It is designed to communicate the platform's evidence-first identity to accelerators, cloud-credit programs, technical collaborators, data partners, and early research users.

## Run locally

No build step or external package is required.

```bash
python -m http.server 8080
```

Open `http://localhost:8080`.

## Included

- Responsive single-page startup website
- Accessible navigation and reduced-motion support
- Product-interface illustration with synthetic values
- Locked-principles narrative and explicit execution-free boundary
- Platform, workflow, research OS, roadmap, and early-access sections
- Browser-local demo form
- SEO and social metadata
- Automated structural tests and audit report

## Before production

1. Choose the final domain and legal operator.
2. Connect the early-access form to a secure endpoint or CRM.
3. Replace the privacy draft with the final legal notice.
4. Add approved analytics only after consent/privacy review.
5. Add real screenshots only after the application dashboard is ready.
6. Configure security headers at the hosting layer.

## Deployment

The folder can be deployed directly to GitHub Pages, Cloudflare Pages, Netlify, Vercel static hosting, AWS Amplify Hosting, or an S3/CloudFront static site.
