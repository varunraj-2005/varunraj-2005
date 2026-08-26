"""
Pulls your live repository list from the GitHub API and writes it into
README.md between the <!-- REPOS:START --> / <!-- REPOS:END --> markers.

Run by the GitHub Action on a schedule (and on manual dispatch), so the
README always reflects your latest repositories -- including brand new
ones -- without you touching it by hand.
"""
import os
import sys
import urllib.request
import json

USERNAME = os.environ.get("GH_USERNAME", "varunraj-2005")
TOKEN = os.environ.get("GITHUB_TOKEN")
README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")

START_MARKER = "<!-- REPOS:START -->"
END_MARKER = "<!-- REPOS:END -->"

API_URL = f"https://api.github.com/users/{USERNAME}/repos?sort=updated&per_page=100"


def fetch_repos():
    req = urllib.request.Request(API_URL)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "readme-live-sync-script")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def build_table(repos):
    repos = [r for r in repos if not r.get("fork")]
    repos.sort(key=lambda r: r.get("pushed_at", ""), reverse=True)
    top = repos[:6]

    lines = [
        "| Sample | Repository | Language | Stars | Last Updated |",
        "|:--:|---|:--:|:--:|:--:|",
    ]
    for r in top:
        name = r["name"]
        url = r["html_url"]
        lang = r.get("language") or "--"
        stars = r.get("stargazers_count", 0)
        updated = (r.get("pushed_at") or "")[:10]
        lines.append(f"| 🧪 | [`{name}`]({url}) | {lang} | {stars} | {updated} |")

    total_repos = len([r for r in repos])
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
    lines.append("")
    lines.append(
        f"_Live count: **{total_repos}** public repositories · **{total_stars}** stars "
        f"· auto-synced from the GitHub API._"
    )
    return "\n".join(lines)


def main():
    try:
        repos = fetch_repos()
    except Exception as e:
        print(f"Failed to fetch repos: {e}", file=sys.stderr)
        sys.exit(1)

    table = build_table(repos)

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if START_MARKER not in content or END_MARKER not in content:
        print("Markers not found in README.md", file=sys.stderr)
        sys.exit(1)

    pre = content.split(START_MARKER)[0]
    post = content.split(END_MARKER)[1]
    new_content = f"{pre}{START_MARKER}\n{table}\n{END_MARKER}{post}"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("README.md updated with latest repositories.")


if __name__ == "__main__":
    main()
