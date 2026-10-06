# Git practice
Work in your own project folder. Never add credentials or customer records.
```text
git init -b main
git status
git add README.md .gitignore
git commit -m "Document project scope"
git log --oneline
```
Create your own empty repository on GitHub, then copy its actual URL:
```text
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```
Replace YOUR_REPOSITORY_URL; it is not runnable as written. Verify the same commit and README in GitHub. If rejected, inspect the remote history; do not force-push over others' work. Make a small branch, inspect git diff, commit and review it before merging.
