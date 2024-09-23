# calculator.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

if __name__ == "__main__":
    print("Simple Calculator")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    operation = input("Choose operation (add, subtract, multiply, divide): ")

    if operation == "add":
        print(f"Result: {add(x, y)}")
    elif operation == "subtract":
        print(f"Result: {subtract(x, y)}")
    elif operation == "multiply":
        print(f"Result: {multiply(x, y)}")
    elif operation == "divide":
        print(f"Result: {divide(x, y)}")
    else:
        print("Invalid operation")


Sharanya Prasad
  1:59 PM
apiVersion: apps/v1
kind: Deployment
metadata:
  name: calculator-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: calculator
  template:
    metadata:
      labels:
        app: calculator
    spec:
      containers:
      - name: calculator
        image: sharanyaganeshprasad/calculator:latest
        stdin: true
        tty: true


Sharanya Prasad
  2:28 PM
Hands on : https://platform.qa.com/lab-challenge/amazon-elastic-container-service-challenge/
:white_tick:
1

2:30
Amazon Elastic Container Service Challenge
New


Sharanya Prasad
  9:02 AM
23.9.24 : CI/CD basics
CI-CD-1.md
 
​
# CI/CD Advanced Concepts
​
## 1. What is `origin` in a Git repository?
​
`origin` is an alias created by Git to refer to the remote repository (usually hosted on platforms like GitHub, GitLab, etc.). When you clone a repository from GitHub to your local machine, Git automatically names the remote link as `origin`. This allows you to easily fetch, pull, and push code between the local and remote repositories without specifying the full URL each time.
​
### Features of `origin`:
- **Ease of use:** Instead of typing the full URL of the repository, you can simply use `origin` to reference the GitHub repository.
- **Default alias:** Git automatically assigns this alias when you clone a repository.
- **Push and pull:** You can push changes to `origin` and pull updates from `origin` easily.
​
#### Example:
```bash
git remote -v
```
​
## 2. Adding Locally Hosted Code to GitHub
​
### Step 1: Initialize a Git repository locally
```bash
git init
```
​
### Step 2: Add files to the staging area
```bash
git add .
```
​
### Step 3: Commit the changes
```bash
git commit -m "Initial commit"
```
​
### Step 4: Add the remote repository (GitHub)
```bash
git remote add origin https://github.com/your-username/your-repository.git
```
​
### Step 5: Push your local changes to GitHub
```bash
git push -u origin main
```
​
## 3. Creating New Local Branches and Pushing Them to Remote
​
### Create a new branch:
```bash
git branch new-feature
```
​
### Switch to the new branch:
```bash
git checkout new-feature
```
​
Or in Git versions 2.23+:
```bash
git switch new-feature
```
​
### Create a new branch and switch to it in one command:
```bash
git checkout -b new-feature
```
​
### Pushing the branch to remote:
```bash
git push origin new-feature
```
​
### Creating a new branch from a specific commit:
```bash
git checkout -b feature-branch <commit-id>
```
​
### Switching to the previous branch:
```bash
git checkout -
```
​
## 4. Creating an Orphan Branch (Empty Branch)
​
An orphan branch is a branch with no history. It starts without the commit history of the current branch.
​
### Command to create an orphan branch:
```bash
git checkout --orphan new-branch
```
​
## 5. Renaming Branches
​
### Renaming the current branch locally:
```bash
git branch -m new-branch-name
```
​
### Renaming a remote branch:
```bash
git push origin :old-branch-name new-branch-name
git push origin -u new-branch-name
```
​
## 6. Deleting Branches
​
### Delete a local branch:
```bash
git branch -d branch-name
```
​
To force delete a branch:
```bash
git branch -D branch-name
```
​
### Delete a remote branch:
```bash
git push origin --delete branch-name
```
​
## 7. Branch Lifecycle with an Example
​
1. **Creating a Branch**:  
   Developers create branches to work on isolated features or fixes.
   ```bash
   git checkout -b feature-branch
   ```
​
2. **Making Changes**:  
   Code changes, additions, and commits are done on the branch.
   ```bash
   git add .
   git commit -m "Add feature"
   ```
​
3. **Pushing to Remote**:  
   Pushing the changes from local to the remote repository.
   ```bash
   git push origin feature-branch
   ```
​
4. **Code Review/Merging**:  
   The branch undergoes code review and, after approval, is merged into the `main` or `master` branch.
   ```bash
   git checkout main
   git merge feature-branch
   ```
​
5. **Deleting the Branch**:  
   After the merge, the branch is deleted locally and remotely.
   ```bash
   git branch -d feature-branch
   git push origin --delete feature-branch
   ```
```
git init                       # Initialize a new Git repository
git add <file>                 # Stage files for commit
git commit -m "message"        # Commit changes
git branch <branch>            # Create a new branch
git switch <branch>            # Switch to a branch
git checkout <branch>          # Switch or checkout a branch
git push origin <branch>       # Push branch to remote repository
git merge <branch>             # Merge a branch into the current branch
git branch -d <branch>         # Delete a local branch
git push origin --delete <branch> # Delete a remote branch
​
```