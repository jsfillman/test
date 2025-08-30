# 🧰 GitHub + Docker Live Demo — 12‑Step Runbook (Web UI + stock git/docker)

**User:** `jsfillman` **Repo:** `intern-workshop-app` **Registry:** GHCR (`ghcr.io/jsfillman/intern-workshop-app`)

No GitHub CLI. Use the **web UI** for repo + PR, and plain `git`/`docker` in terminal.  
Claude Code generates the app + workflow.

> Prereqs: Docker Desktop running; Git installed and authenticated for HTTPS pushes (PAT if prompted).

---

## 1) Create repo with a blank README (Web UI)
1. Go to https://github.com/new
2. **Owner:** `jsfillman`
3. **Repository name:** `intern-workshop-app`
4. **Public**
5. ✅ Check **“Add a README file”** (we want a blank initial commit)
6. Click **Create repository**

---

## 2) Clone repo locally
```bash
git clone https://github.com/jsfillman/intern-workshop-app.git
cd intern-workshop-app
```

---

## 3) Have Claude Code generate the initial app (all the things)
Paste this prompt into Claude Code:

```
You’re scaffolding a polished but tiny Flask app with Bootstrap that builds fast in Docker and publishes to GHCR on merges.

Requirements:
- Python/Flask app listening on 0.0.0.0:8080
- Bootstrap 5 via CDN; centered hero with:
  - Title: “Hello from Intern Workshop”
  - Subtitle: “Built live with GitHub + Docker 🚀”
  - Primary button: “Interns Rule ✨”
- Env overrides: TITLE, SUBTITLE, BUTTON_TEXT
- Route /status → JSON { "ok": true, "version": "1.0.0" }
- Minimal CSS polish in static/styles.css
- Dockerfile (python:3.12-slim, gunicorn run)
- .dockerignore & .gitignore
- GitHub Actions workflow .github/workflows/docker-publish.yml that:
  - Builds on PRs to main (no push)
  - Publishes to GHCR on pushes to main (incl. PR merges)
  - Image name: ghcr.io/${{ github.repository_owner }}/intern-workshop-app
  - Tags: latest on main + SHA tags
- README.md with local + Docker quickstart

Deliverables (file-by-file, no extra commentary):
- app.py
- templates/index.html
- static/styles.css
- requirements.txt
- .gitignore
- .dockerignore
- Dockerfile
- .github/workflows/docker-publish.yml
- README.md
```

**Create/replace the files locally** with Claude’s output (save each path in your repo).

---

## 4) Push it
```bash
git add .
git commit -m "feat: initial Flask+Bootstrap app, Dockerfile, and GHCR workflow"
git push origin main
```

---

## 5) Build it locally and demo it works (Baseline)
```bash
docker build -t intern-workshop-app:latest .
docker run -d --name intern-workshop-app -p 8080:8080 intern-workshop-app:latest
# Open the app in your browser:
open http://localhost:8080 2>/dev/null || xdg-open http://localhost:8080
```
✅ Expect **“Hello from Intern Workshop”**.

Stop before the edit:
```bash
docker rm -f intern-workshop-app
```

---

## 6) Create a branch
```bash
git checkout -b change-home-theme
```

---

## 7) Have Claude make a minor edit (index text + CSS theme)
Paste this prompt into Claude Code:

```
Make small visual tweaks:
- In templates/index.html: change the H1 to “Interns rule ✨” and adjust subtitle copy.
- In static/styles.css: switch gradient hues slightly darker and add a subtle card shadow.
Output only the updated file contents.
```

Apply the changes Claude returns (overwrite the two files).

```bash
git add templates/index.html static/styles.css
git commit -m "chore: tweak hero copy and theme (Interns rule ✨)"
git push -u origin change-home-theme
```

---

## 8) Create a PR (Web UI)
1. Go to `https://github.com/jsfillman/intern-workshop-app`
2. Click **Compare & pull request** (or “New pull request” → base: `main`, compare: `change-home-theme`)
3. Create PR with a short note (e.g., *“Minor hero copy + theme tweak”*)

---

## 9) Show diff between PR branch and main (Web UI)
- On the PR page, click **Files changed** to highlight exactly what changed (HTML + CSS).  
- Optional: add a quick comment/review to model collaboration.

---

## 10) Merge the PR (Web UI)
- Click **Merge pull request** → **Confirm**.  
- Delete branch when prompted (optional).

---

## 11) Show GHA builds package (Web UI)
- Go to the repo’s **Actions** tab → watch the workflow run on the merge to `main`.  
- After it completes, go to **Packages** (in the repo sidebar or your profile) and confirm the new image:
  - **Image:** `ghcr.io/jsfillman/intern-workshop-app:latest` (plus a SHA tag)

> If Packages isn’t visible in the repo sidebar, open your profile → **Packages** → locate `intern-workshop-app`.

---

## 12) Pull package and run it with the new edits
```bash
# Stop and remove any local container from earlier (if still running)
docker rm -f intern-workshop-app 2>/dev/null || true

# Pull the freshly published image from GHCR
docker pull ghcr.io/jsfillman/intern-workshop-app:latest

# Run the image from GHCR
docker run -d --name intern-workshop-app -p 8080:8080 ghcr.io/jsfillman/intern-workshop-app:latest

# Open the app again
open http://localhost:8080 2>/dev/null || xdg-open http://localhost:8080
```
✅ Expect the **updated hero text/theme** from the merged PR.

Cleanup:
```bash
docker rm -f intern-workshop-app
```

---

## 🧯 Troubleshooting Speed‑run
- **Push auth prompt** → use a GitHub Personal Access Token (HTTPS) when asked for password.
- **Port in use** → swap to `-p 8081:8080` and open `http://localhost:8081`.
- **Actions didn’t publish** → ensure the workflow file exists at `.github/workflows/docker-publish.yml` and that the job ran on the merge **to main**.
- **Can’t find package** → check Actions log for push step; verify image name `ghcr.io/jsfillman/intern-workshop-app`.
- **Slow first build** → pip cache warm‑up; subsequent builds are faster.

---

## 🎤 Lines to drop while it cooks
- “GitHub = multiplayer save file.”
- “PR = your branch asking to move back in with the family.”
- “Docker = a lunchbox with everything your app needs.”
- “Same command, different app — because Docker rebuilt from new code.”
- **Closer:** “GitHub is how you build with people. Docker is how you ship to the world.”
