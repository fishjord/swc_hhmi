***This was taken from https://gist.github.com/pshken***

Git Cheat Sheet
---------------

# Committing and Undoing

## Adding file for committing

```
$ git add <filename>
```
or
```
$ git add .
```

## Executing Comming

```
$ git commit -m "This is my comment"
```
or adding + committing in one

```
$ git commit -a -m "My comment"
```

## Undoing all changes

Reverts **all** changes to the last commit

```
$ git reset --hard
```

# Merging

## Merge single file(s)

```
$ git checkout <local-branch-name> <file-path>
```

# Update from original repo

```
$ git remote add upstream <org_git_url>
```

Then you can fetch it normally through

```
$ git pull upstream <branch>
```

# Branches

Docs: [http://gitref.org/branching/](http://gitref.org/branching/)

## List all branches

```
$ git branch -v
```

## Create Branch

Checks out a branch and automatically switches to it.

```
$ git checkout -b <new-branch-name>
```

## Download a remote branch
```
$ git checkout -b local-branch-name origin/remote-branch-name
```

## Publish a local branch

```
$ git push -u origin <local-branch-name>
```

## Delete remote branch

```
$ git push origin :<remote-branch-name>
```

## Git Configuration

### Pretty logs

Add an alias to your `~/.gitconfig` like

```
[alias]
  lg = log --graph --full-history --all --color --pretty=tformat:"%x1b[31m%h%x09%x1b[32m%d%x1b[0m%x20%s%x20%x1b[33m(%an)%x1b[0m"
```