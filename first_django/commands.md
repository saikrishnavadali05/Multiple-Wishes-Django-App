### Important Django commands

```python manage.py runserver```
> This puts the server up an running the default port is 8000
```python manage.py makemigrations```
> makemigrations basically generates the SQL commands for preinstalled apps
```python manage.py migrate```
> Migrations are Django’s way of propagating changes you make to your models into your database schema. 

### Steps to create virtual environment

### git commands
<br></br>
> delete a local branch
```git branch -d <local-branch>```
<br></br>
> delete a remote branch
```git push origin --delete <remote-branch-name>```
<br></br>
> Command to force delete a local branch (irrespective of whether the branch is merged into another branch or not)
```git branch -D <local-branch>```
  <br></br>
> Create a new branch from an older commit
```git branch <new-branch-name> <older-commit-hash>```
  <br></br>
> Create and checkout to a new branch from an older commit
```git checkout -b <new-branch-name> <older-commit-hash>```



