# GIT: BASICS

## 0. Install

**- Download Git** https://git-scm.com/downloads

**- Check version of git**

```git --version```

## 1. Git Workflow:

![Workflow](https://i.redd.it/nm1w0gnf2zh11.png)

![Workflow](https://www.toolsqa.com/gallery/Git/4%20Git%20Life%20Cycle.png)

## 2. File Stages

![File Stages](https://i.stack.imgur.com/slaGB.png)


**Three Git stages:**

**- Modified:** The file has been changed but not committed to the database.

**- Staged:** The file has been marked for inclusion in the next commit.

**- Committed:** The file has been committed to the database.

## 3. Configure Git

**- Set your user name and email address: git config**

```$ git config --global user.name "your_username"```

```$ git config --global user.email "your_email@example.com"```

**- List and show Git config settings**

```$ git config --list```

+ Typing git config <key> to check a specific key’s value:
  
```$ git config user.name```
  
```TaMinhSon810```

## 4. Commands:

### 4.1. Basic

**- ```git init```:** Create empty Git repo in specified directory. Run with no arguments to initialize the current directory as a git repository.

```$ git init <directory>```
  
**- ```git clone```:** Clone repo located at <repo> onto local machine. Original repo can be located on the local filesystem or on a remote machine via HTTP or SSH.

```$ git clone <repo>```
  
**- ```git add```:**  Add files to the staging area
  
```$ git add <filename>```
  
```$ git add *```
  
**- ```gỉt commit```:** Create a snapshot of the changes and save it to the git directory.
  
```$ git commit -m "<message>"```
  
**- ```git status```:** List which files are staged, unstaged, and untracked
  
```$ git status```
  
**- ```git log```:** See the repository’s history by listing certain commit’s details
 
```$ git log```
  
**- ```git diff```:** Show unstaged changes between your index and working directory 
  
```$ git diff```
  
### 4.2. Working with branches
  
**- ```gỉt branch```:** List all of the branches in your repo**

```$ git branch```
  
**- ```git checkout```:** Creates branches and helps you to navigate between them
  
+ Create and check out a new branch named <branch>:
  
```$ git checkout -b <branch-name>```
  
+ Switch from one branch to another:
  
```$ git checkout <branchname>```
  
**- Delete the feature branch:**

```$ git branch -d <branchname>```
  
 ### 4.3. Remote Repositories
  
**- Connect the local repository to a remote server:**
  
```$ git remote add origin <host-or-remoteURL>```
 
**- List all currently configured remote repositories:**
  
```$ git remote -v```
  
**- ```git pull```:** merges all the changes present in the remote repository to the local working directory
  
```$ git pull origin <branch>```

**- ```git fetch```:** allows users to fetch all objects from the remote repository that don’t currently reside in the local working directory.

```$ git fetch origin <branch>```
 
**- ```git push```:** Send local commits to the master branch of the remote repository.
  
```$ git push origin <branch>```
  
**- ```git merge```:** Merge a different branch into your active branch
  
```$ git merge <branch>```

### 4.4. Other Commands

**- ```git revert```:** Create new commit that undoes all of the changes made in **commit**, then apply it to the current branch

```$ git revert <commit>```

**- ```git reset```:**

```git reset [--optional flag] <commit-hash> ```

***optional flag***:

**+ git reset --mixed:** The default option for git reset. Updates the current branch tip to the specified commit and unstages any changes by moving them from the staging area back to the working tree.

**+ git reset --soft:** Known as a soft reset, this updates the current branch tip to the specified commit and makes no other changes.

**+ git reset --hard:** Known as a hard reset, this updates the current branch tip to the specified commit, unstages any changes, and also deletes any changes from the working directory.


**- ```git rebase```:** used to apply certain changes from one branch to another. **base** can be a commit ID, branch name, a tag, or a relative reference to HEAD

```git rebase <base>```
  



  


