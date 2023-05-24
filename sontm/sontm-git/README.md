# GIT: BASICS
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
 
**- git push:** Send local commits to the master branch of the remote repository.
  
```$ git push <remote> <branch>```


