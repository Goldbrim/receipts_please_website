# Receipts, Please. release checklist

## Website and legal

- [ ] Confirm `Receipts, Please` exactly matches the developer name displayed on the final Google Play listing; confirm `Receipts, Please.` is the final app name there.
- [ ] Register `receiptsplease.app` (if not already done), set up DNS for GitHub Pages, and create the `hello@receiptsplease.app` mailbox.
- [ ] Have the developer approve the Privacy Policy and Terms of Service. Verify actual retention and deletion behavior for Supabase database backups/logs, OpenAI processing logs, RevenueCat records, GitHub Pages hosting logs, and the support mailbox. Do not promise that all third-party copies disappear within 30 days.
- [ ] Confirm Goldbrim LLC is the correct legal entity named in the footer, Terms of Service, and Privacy Policy.
- [ ] Decide whether the Terms need a minimum age and a governing-law / disputes clause, and whether the Privacy Policy needs a children's privacy section. Placeholders are marked `TODO` at the top of `src/terms.njk` and `src/privacy.njk`.
- [ ] Approve the new Privacy Policy sentence about launch-notice emails. If you set `waitlistEndpoint`, name the form provider in the Privacy Policy first.
- [ ] Confirm `hello@receiptsplease.app` can receive, verify, track, and complete manual deletion requests for app-controlled account/cloud data within 30 days. Test the prefilled link and plain-address fallback.
- [ ] Verify the cleanup job for stale temporary receipt images and drafts is deployed and scheduled; test deletion of an account with backed-up photos before approving the cloud-deletion description.
- [ ] Publish the repository to GitHub, set **Settings → Pages → Source** to **GitHub Actions**, configure the `www.receiptsplease.app` custom domain, enable Enforce HTTPS, and verify HTTPS plus direct, publicly accessible 200 responses for all five routes without sign-in or PDF delivery. Confirm `robots.txt`, `sitemap.xml`, and the 404 page are served.
- [ ] Check mobile and desktop layout, keyboard navigation, readable text, all internal links and assets, and reduced-motion behavior on the deployed site.
- [ ] Check the social preview by pasting the URL into a messaging app or a link-preview checker.
- [ ] Verify all four app screenshots look sharp and appear in the correct order on the live site.
- [ ] Put `https://www.receiptsplease.app/privacy/` and `https://www.receiptsplease.app/delete-account/` into the correct Google Play Console fields. Leave `playStoreUrl` empty in `src/_data/site.json` until the verified Play listing URL exists.

## App and Google Play

- [ ] Rebrand the Flutter title, Android label, account/about text, subscription screen, and Play listing from “Dollars & Sense” to “Receipts, Please.” before release. This website intentionally does not change Flutter or Supabase.
- [ ] Decide whether Android device backups may include the local receipt database and saved photos. The current XML rules exclude secure credential preferences only. Either keep the website disclosure aligned with that behavior or change and verify the app backup rules in a separate app task.
- [ ] Set the existing `DOLLARS_TERMS_URL` and `DOLLARS_PRIVACY_URL` release build values to the live HTTPS URLs, and verify both links open in the app. Make the Privacy Policy readily accessible in-app beyond the Play listing.
- [ ] Complete the Google Play Data safety form, including collection/sharing categories and account-deletion answers, using the release build's actual SDK and provider behavior. Verify the external deletion link starts a request without reinstalling the app.
- [ ] Verify the final Google Play and RevenueCat product configuration, actual plan prices, trial eligibility, renewal and cancellation text, purchase/restore behavior, and the Google Play subscription-management route with test accounts.
- [ ] Complete the project's existing physical-device release gate and test in-app account deletion with populated synced records and cloud-backed photos.
