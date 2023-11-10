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



## Pull request?

```
git clone https://github.com/hanxiaomax/missing-semester.git
```

<u>commit</u>	<u>New pull request</u>



#### gitignore

```
git config --global core.excludesfile ~/.gitignore .DS_Store
```





git push origin master之后报错

hint: Updates were rejected because the remote contains work that you do hint: not have locally. This is usually caused by another repository pushing 
hint: to the same ref. You may want to first integrate the remote changes 
hint: (e.g., 'git pull ...') before pushing again. 
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

这个错误消息表示你试图将你的更改推送到远程仓库时，远程仓库中已经有了一些你本地仓库中没有的更改。这通常发生在多人协作的项目中，当其他人在你之前推送了他们的更改。

要解决这个问题，你可以按照以下步骤操作：

### 1. 拉取远程仓库的最新更改到本地

```
git pull origin master
```

这将会拉取远程 `master` 分支的最新更改到你本地的 `master` 分支。如果远程仓库有你本地没有的更改，这将会创建一个合并提交，你可能需要解决合并冲突。

### 2. 解决合并冲突（如果有）

如果有合并冲突，你需要手动解决它们。解决冲突后，你需要将解决冲突后的文件添加到暂存区，然后提交这些更改：

```
git add <filename>
git commit
```

### 3. 再次推送你的更改

解决了合并冲突并提交了你的更改后，你可以尝试再次推送你的更改到远程仓库：

```
git push origin master
```