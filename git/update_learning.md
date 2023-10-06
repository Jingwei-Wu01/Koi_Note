# How to update a file to Github via git?



<!--You dont have to do this again if you've done it before-->

### 1. ssh & git config

**Create SSH KEY:** `ssh-keygen -t rsa -C jingweiwu@bupt.edu.cn`

`enter`

Your identification has been saved in /Users/k/.ssh/id_rsa.

Your public key has been saved in /Users/k/.ssh/id_rsa.pub.

`ssh-add ~/.ssh/id_rsa`

Identity added: /Users/k/.ssh/id_rsa (jingweiwu@bupt.edu.cn)

`cd ~/.ssh`

```
$ls
$id_rsa		id_rsa.pub	known_hosts
```

Private key: `cat id_rsa`

**Public key:** `cat id_rsa.pub`

### 2. Github Setting

Add new SSH key in GitHub (in **id_rsa.pub**)



<!--Required if you're uploading a new project-->

### 2.5 Github Setting

New repository

### 3. Terminal

`git init ` 

`git add .`

 `git commit -m "description"` 

`git remote add origin git@github.com:Jingwei-Wu01/Koi_Note.git` 

`git push -f origin master`



## How to update?

**`git add file_name`**

**`git commit -m "description"`** 

**`git push origin master`**