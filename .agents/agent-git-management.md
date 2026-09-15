# Agent Git Management

## Core Rule

Do not touch Git unless explicitly asked. File edits are working-tree changes only.

## Allowed Git Actions (Only When Explicitly Requested)

- `git status` / `git diff` / `git log` (read-only inspection)
- `git add <files>` (staging)
- `git commit -m "message"`
- `git push` / `git pull` / `git fetch`
- `git checkout <branch>` / `git switch <branch>`
- `git merge` / `git rebase`
- `git reset` / `git restore`
- `git stash` / `git tag`
- `git branch` / `git remote`

## Prohibited Git Actions (Unless Explicitly Asked)

- Do not run `git add`, `git commit`, `git push`, or any mutating Git command during normal file updates
- Do not modify `.gitignore`, `.gitattributes`, or other Git metadata
- Do not create, rename, or delete branches
- Do not modify Git state when asked to "update files" or "fix something" - only edit the files themselves

## Workflow

1. When asked to update files, edit files only. Do not stage, commit, or push.
2. When asked to commit, stage and commit only the files that were changed.
3. When asked to push, push the current branch.
4. When asked to create a PR, use `gh` CLI or GitHub website.

## Notes

- Git history is preserved unless explicitly asked to rewrite it.
- Do not force-push unless explicitly requested.
- Do not skip hooks unless explicitly requested.
- Do not amend commits unless explicitly requested.
