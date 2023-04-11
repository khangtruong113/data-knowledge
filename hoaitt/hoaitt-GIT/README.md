# BASIC GIT COMMANDS

+ Git Config: **sets the author name and email adddress** to be used with your commits

```$ git config --global user.name "Youruser_nameinGitlab"```

```$ git config --global user.email "yourEmailInGitLab"```

+ Git Init: **creat a local reposity**

```$ git init TheNameOfALocalRepo```

+ Git clone: **make a copy of a repo** from an existing URL

```$ git clone URLFromGitLab```

+ Git add: **add 1/more files to staging area**

```$ git add “FileName”``` 

```$ git add *```

+ Git commit: **changed the head/records or snapshots** the file permanently in the version history

```$ git commit –m “commit massage that you want to inform members of your team”``` 

*// add file berfore you commit it*

```$ git commit –a –m “commit massage that you want to inform members of your team”```

*// git add anf also commits any files you’ve changed*

+ Git status: **display the state of the working direcoty and the staging area**, see which changes have been staged, which haven’t, which file aren’t being tracked

```$ git status```

+ Git push: **upload local repo to a remote repo**

```//send the changes made on the master branch to your remote repo```

```$ git push [variable name] master```

*//push all the branches to the server repo*

```$ git push –all```

+ Git pull: **receive data from gitlab**

```$ git pull URL```

+ Git branch: **list all the branches** available in the repo

```$ git branch```

+ Git merge: **merge the specified branched into the current branch**

```$ git merge BranchName```

+ Git checkout: **switch to the specific branche**

```$ git checkout NameOfTheBranch```

+ Git log: **check the commit history**

```$ git log```

+ Git remote: **connect your local repo to the remote server** (create, view, delete connections)

```$ git remote add URL```
