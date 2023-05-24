# GIT: BASICS
## 0. Git Workflow:

![Workflow](https://i.redd.it/nm1w0gnf2zh11.png)

## 1. Configure Git

**- Set your user name and email address: git config**

```$ git config --global user.name "your_username"```

```$ git config --global user.email "your_email@example.com"```

**- List and show Git config settings**

```$ git config --list```

+ Typing git config <key> to check a specific key’s value:
  
```$ git config user.name```
  
```TaMinhSon810```

## 2. Basics Commands:

**- git init:** Create empty Git repo in specified directory. Run with no arguments to initialize the current directory as a git repository.

```$ git init <directory>```
  
**- git clone:** Clone repo located at <repo> onto local machine. Original repo can be located on the local filesystem or on a remote machine via HTTP or SSH.

```$ git clone <repo>```
  
**- git add:**  Add files to the staging area
  
```$ git add <filename>```
  
```$ git add *```
  
**- gỉt commit:** Create a snapshot of the changes and save it to the git directory.
  
```$ git commit -m "<message>"```
  
**- git status:** List which files are staged, unstaged, and untracked
  
```$ git status```
  
**- git log:** See the repository’s history by listing certain commit’s details
 
```$ git log```
  
**- git diff:** Show unstaged changes between your index and working directory 
  
```$ git diff```
  
### Working with branches
  
**- gỉt branch:** List all of the branches in your repo**

```$ git branch```
  
**- git checkout:** Creates branches and helps you to navigate between them
  
+ Create and check out a new branch named <branch>:
  
```$ git checkout -b <branch-name>```
  
+ Switch from one branch to another:
  
```$ git checkout <branchname>```
  
**- Delete the feature branch:**

```$ git branch -d <branchname>```
  
 ### Remote Repositories
  
**- Connect the local repository to a remote server:**
  
```$ git remote add origin <host-or-remoteURL>```
 
** List all currently configured remote repositories:**
  
```$ git remote -v
  
** git pull:** merges all the changes present in the remote repository to the local working directory
  
```$ git pull origin <branch>
 
**- git push:** Send local commits to the master branch of the remote repository.
  
```$ git push origin <branch>```
  
**- git merge:** Merge a different branch into your active branch
  
```$ git merge <branch>```
  


  



