# Setup — Make this your GitHub profile README

Your profile README lives in a special repo named exactly like your username:
**`varunraj-2005/varunraj-2005`**. If it doesn't exist yet, create it on GitHub
(check "Add a README file") — GitHub will show it on your profile automatically.

### 1. Copy these files in
Copy everything in this folder into that repo, keeping the structure:
```
varunraj-2005/
├── README.md
├── .github/workflows/update-readme.yml
├── scripts/update_repos.py
└── assets/elements/*.svg
```

### 2. Push it
```bash
git add .
git commit -m "Add heroic dossier README with live sync"
git push
```

### 3. Turn on the live sync
Go to your repo → **Actions** tab → enable workflows if prompted → open
**"Sync Live Repository Log"** → click **Run workflow** once to populate the
Field Log table immediately. After that it re-runs automatically every 6
hours and on every push, so:
- **New repo?** Shows up within 6 hours (or instantly if you push to this repo).
- **New stars / renamed repo?** Same — picked up on the next sync.
- **Stats panels** (commits, streak, top languages, profile views) are live
  images fetched fresh from their services on every profile view — nothing
  to configure, they just work as soon as the README is public.

### Notes
- The `Sample 🧪` column and lab theming are cosmetic flavor to match the
  portfolio's dossier style — feel free to rename the section.
- GitHub has no "on new repo created" webhook you can subscribe to directly,
  which is why this uses a 6-hourly schedule instead of true instant push.
  You can shorten the cron in `update-readme.yml` (e.g. `*/30 * * * *` for
  every 30 minutes) if you want tighter sync — GitHub Actions free minutes
  are generous enough for that on a personal profile repo.
- If you ever rename your GitHub username, update `GH_USERNAME` in
  `update-readme.yml` and `scripts/update_repos.py`.
