# Receipts, Please.

**A smarter home for your receipts.**

Official website for Receipts, Please., a mobile app that helps you organize receipts, understand your spending, and track prices over time. Live at <https://www.receiptsplease.app>.

## Features

- **Save Receipts:** Scan and digitally organize purchase receipts.
- **Understand Spending:** Explore spending trends by store, category, and individual item.
- **Track Prices:** Compare historical prices and see how costs change over time.
- **Search Purchases:** Easily find past receipts and purchases.

## How the site is built

The site is built with [Eleventy](https://www.11ty.dev/), which turns the templates in `src/` into plain HTML in `_site/`. The header, footer, and navigation live in one place (`src/_includes/layouts/base.njk`), so a new page or link only needs to be added once.

| Where | What |
| --- | --- |
| `src/_data/site.json` | Site name, domain, email, company, Play Store link, waitlist endpoint |
| `src/_data/nav.json` | Header and footer links |
| `src/_includes/layouts/` | Shared page shell (`base.njk`) and legal-page layout (`document.njk`) |
| `src/*.njk` | One file per page (home, privacy, terms, account deletion, support, 404) |
| `src/styles.css` | All styles |
| `src/assets/` | Web-ready images (generated, see below) |
| `art/` | Full-size original artwork, not published |

### Run it locally

Requires Node.js 20 or newer.

```bash
npm install
npm start
```

Then open <http://localhost:8080>. `npm run build` writes the finished site to `_site/`.

### Deploying

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site and publishes it to GitHub Pages. One-time setup in the GitHub repository:

1. **Settings → Pages → Build and deployment → Source:** choose **GitHub Actions**.
2. **Settings → Pages → Custom domain:** enter `www.receiptsplease.app`, then tick **Enforce HTTPS**. (With Actions deploys, GitHub uses this setting rather than the `CNAME` file.)
3. At your DNS provider, point `www` at `<your-github-username>.github.io` (CNAME record) and the apex `receiptsplease.app` at GitHub Pages' A records so it redirects to `www`.

## Switches in `site.json`

- **`playStoreUrl`**: leave empty until the Google Play listing is live. Once set, the hero shows a real "Get it on Google Play" button, the header shows "Get the app", and the launch-notice section is removed.
- **`waitlistEndpoint`**: leave empty to use the "Email me at launch" button (opens the visitor's email app). To collect sign-ups with a form instead, create a form with a service such as Formspree or Buttondown and paste its form action URL here. The form posts a field named `email`, plus a hidden `_gotcha` spam trap. Update the Privacy Policy to name the provider before you turn it on.

## Images

Web-ready images are generated from the originals in `art/`:

```bash
pip install Pillow
npm run images
```

This makes the logo, favicons, app icons, the hero mascot, the 1200×630 social preview card (`og-image.png`), and the homepage WebP screenshots.

### Updating the app screenshots

The four original promotional images live in `art/screenshots/`. `npm run images` converts them to WebP in `src/assets/screenshots/` at their original dimensions (quality 100, method 6) to keep fine text sharp. The generated WebP files are committed and published; the PNG originals are not. The build adds a content version to the stylesheet and screenshot URLs so visitors receive updated assets promptly.

To update the gallery, replace the corresponding PNG in `art/screenshots/`, run `npm run images`, and check the titles, captions, alt text, and dimensions in the `screenshots:` list at the top of `src/index.njk`.

## Copyright

© 2026 Goldbrim LLC. All rights reserved.
