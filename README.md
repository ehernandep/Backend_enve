
## Git Flow

`git pull --rebase origin main`
Pull last commits from main

`git checkout -b {name-of-branch}`
Create a new branch from main

`git add .`
Add all files with changes bofere commit

`git commit -m '{commit description}`
Commit changes

`git push origin {name-of-branch}`
Push change to the new branch

`Merge PR into main`

`git checkout main`
go back to main

`git pull --rebase origin main`
Pull last commits from main

## IMPORTANT
If someone of the team merge into main and you already have a branch open, you need to pull the changes from the main before continue.
First make sure you are up to date with your current branch then:
`git merge main`
If you have conflicts you can see it in Source control in visual studio code. If you have some doubts of what need to stay and what not 
better discuss with the team.
If you don’t have any conflicts make sure you do your git commit -m ‘<comment>’ and continue the development.


