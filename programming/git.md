


#Index
[creating a new local git repository](##creating a new local git repository)
[git status](##git status)
[tracking new files(staging area)](##tracking new files(staging area)
)
[committing changes](##committing changes)
[removing files](##removing files)
[moving files](##moving files)

[working with remotes](##working with remotes)
	[adding remote repositories](##adding remote repositories)
	[fetching and pulling from remotes](##fetching and pulling from remotes)
	[pushing to remotes](##pushing to remotes)


##creating a new local git repository
create new directory
git init
 -makes directory new repository


##deleting local git repository

##branches
list current branch:
git rev-parse --abbrev-ref HEAD
list all branches:
git branch
###master branch
 -contains the regular commits
 -master branch should always be working and on point, as this is the code everyone pulls from

###different branches
creating a new branch:
git checkout -b nameofbranch

deleting a branch:
git branch -d nameofbranch

switch to different branch: 
git checkout nameofbranch

switch to master branch:
git checkout master

updating a branch from changes in the masterbranch
 -merging the master branch with current branch

###merging branches


Explanation:
 -if not too sure about code it can be stored on a different branch, without affecting and potentially destroying main branch
 -if branch is working it can be merged with the master branch
 -branches can still be updated from the masterbranch


##removing files
removing files from  the git

git rm command
	-removes file from git and also from directory

if a commited file is simply deleted from the working directory this would be an unstaged change
to stage the removal of the file type git rm
the next time changes are commited the file will be removed and will no longer be tracked






##working with remotes

setting up a remote repository
-create a repository on github
git remote add origin <url of repository>
  -adds a remote (a url to another repository)  
  -changes can now be pushed from the local repository to the remote repository  
  -origin is the name of the repository on the computer

deleting remote origin: git remote remove origin



##pushing changes from local to remote repository
git push -u origin master
 -all commits from the branch master are pushed to the repository origin
 -"-u" means that branch and repository are remembered, git push will suffice the next time

saving Username and Token on the system: git config --global credential.helper store

git push <remote> <branch>


##fetching and pulling from remotes

git  pull origin master

		
	





##git status
each file in the working directory is either tracked or untracked
tracked files are files git knows about

untracked files are files are files in the workingdirectory git doesn't know about

determine the state of you files:
git status
