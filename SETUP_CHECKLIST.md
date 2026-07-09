# SETUP_CHECKLIST — the manual steps only you can do (tonight)

*Grows during the session. Everything here is one-time; after this the machine
runs itself.*

## 0. PyPI publish — ✅ DONE 2026-07-08 (identity-resolver 0.1.0 live)
- [ ] Create account + API token at pypi.org
- [ ] `cd identity-resolution-engine && python3 -m pip install build twine && python3 -m build && python3 -m twine upload dist/*`
- [x] DONE — https://pypi.org/project/identity-resolver/0.1.0/ live; pip install verified; portfolio stat lights up next refresh

## 1. Free API keys to request (all instant)
- [ ] **Census API key** — https://api.census.gov/data/key_signup.html (email arrives in minutes)
- [ ] **FRED API key** — https://fred.stlouisfed.org/docs/api/api_key.html (instant with account)
- [ ] **YouTube Data API key** — console.cloud.google.com → new project → enable "YouTube Data API v3" → credentials → API key
- [ ] **Gmail app password** — myaccount.google.com/apppasswords (requires 2FA on). Name it "mission-control". 16-char password, save it once.

## ⚠️ WHY THE 6 AM EMAIL FAILED (2026-07-08)
The dispatch job errored `At least one of 'to' … must be specified` — because
**no mail secrets are set yet**. This is the pending checklist step, not a bug.
Set the two secrets below and the email works (MAIL_TO now defaults to
MAIL_USERNAME, so 2 secrets are enough). Then Actions → "Daily email — dispatch"
→ Run workflow to test immediately.

## 2. Repo secrets to set (Settings → Secrets and variables → Actions)
| Repo | Secret | Value |
|---|---|---|
| mission-control | MAIL_USERNAME | safayashubham@gmail.com |
| mission-control | MAIL_APP_PASSWORD | the 16-char Gmail app password |
| mission-control | MAIL_TO | safayashubham@gmail.com |
| mission-control | ANTHROPIC_API_KEY | *(optional — fresh-generation path)* |
| us-consumer-pulse | CENSUS_API_KEY | from step 1 |
| us-consumer-pulse | FRED_API_KEY | from step 1 |
| shubham-safaya.github.io | YOUTUBE_API_KEY | *(optional — RSS path needs no key)* |

## 3. Config values to confirm
- [ ] `mission-control/config/content-config.json` → `linkedin_start_day`:
      set to your ACTUAL next Day number (check your last LinkedIn post).
      Bank files are day-001…day-090 and are offset by this number at
      assembly time — no renaming needed.
- [ ] `mission-control/config/blackout.json` → add your private date ranges
      (September / December). Format inside the file. The email switches to
      light mode inside those ranges and never names why.

## 4. Test-fire tonight (Actions tab → workflow → Run workflow)
- [ ] mission-control → "Daily email — assemble" → then "Daily email — dispatch" → check inbox
- [ ] shubham-safaya.github.io → "Refresh stats" → confirm stats strip updates
- [ ] us-consumer-pulse → "Daily refresh" (after keys set)

## 5. First-24-hours verification (tomorrow ~6:05 AM Central)
- [ ] 6:00 AM email arrived with today's Day-N post + tasks
- [ ] live/ healthcheck issue count = 0 (github.com/Shubham-Safaya/live/issues)
- [ ] Portfolio stats strip shows yesterday's date
- [ ] data/history/ folders gained one new file each
