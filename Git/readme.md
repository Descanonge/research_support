# Using Git and Github/Gitlab

You may have noticed that this help repository is relying on git, so it's a first reason to learn about it if you want to contribute!
On top of that, it is a very powerful tool to backup your work, manage different versions, and also collaborate with others.

Sorry this guide is a bit lengthy but this is (I think) a really great and important tool, and not necessarily easy to grasp at first.
I will try to stick to the minimum necessary to get around. A section focuses on how to contribute to this repository.

## Which is which ?

Git is a software that does **version control**, when you '*commit*' it save the documents in your project directory to their current state.
You can easily check what has been changed between commits, revert your directory to a specific one, etc.
You can also create different '*branches*', which are co-existing versions of your project.

Your project directory constitute a '*repository*'. It can be linked to other versions of your repository, for example one on a server somewhere, or the one of your colleague.
In practice, there is one of them that act as the master version, the 'real' version. And most often it is stored on a server that offers additional services.

Github offers to store your repository and features such as viewing/editing the code, engaging in discussions, and facilitating collaboration.
Note that Github was bought by Microsoft and is thus operating on their servers (it is free though).
Gitlab is a similar service but let your organization run the servers.

## How to I work with it ?

### The Editor

You can do a lot of things directly from Github or Gitlab by finding the 'add file' and 'edit' buttons. You can also use a more fully fledged code editor / IDE. In Gitlab it will be suggested as the 'Web IDE' when clicking the blue 'Edit' button. On Github you can find it on the main page of the repository, by clicking on the green '<> Code' button, then the 'Codespace' tab.
Both editors seems essentially the same, though the *REDACTED* could not open a terminal and run commands (maybe because I was using Firefox?).
The editor is based on Visual Studio Code so you might feel right at home[^1].

> Little tip: split the window in two (button on top right) to have the preview of how the markdown is going to look.

However, you might prefer using your own editor, on your own computer.
If the repository already exists on the server (you can create a repository from there)[^2], you must '*clone*' it on your computer.
The address will appear in the '<> Code' or 'Clone' button. It is either *REDACTED* or `https://github.com/<username>/<project>.git`.

[^1]: uh technically 🤓 VS Code was created on web technology making this kind of stuff possible. Note you can similarly connect to your Github account from VS Code.

[^2]: If you already have an existing directory on your computer you can go in it and execute:
      `git init`. You can then create an empty repository on Github/lab, register it as a remote:
      `git add remote origin -u <url>`.


### Starting a project

We will use git in the command line in the rest of this guide, but you can also use a graphical client like [thoses](https://git-scm.com/downloads/guis) or extensions for your editor[^3]:
``` shell
git clone https://github.com/aang/restore-balance.git
```
This will create a `restore-balance` folder, with all the files and the git information.
The address of the original repository on the server is kept as a 'remote' named 'origin' by default.

If the original repository add one branch named 'main' ('master' was the old norm but it has evolved to main), you will end up with a '*reference*' named 'origin/main' that points to the server and a '*branch*' 'main', which sits on your computer.
Let's do some modifications to our local work directory. Having worked hard, we save our labor by creating a *commit*. We must first select the changes we want to save by '*staging*' them, for now let's stage everything then commit:
``` shell
git add
git commit -m "Learn waterbending from Katara"
```
Note the *commit message* indicated with `-m`, you can also use `-c` alone which will open your text editor for you to write the message.[^4]

Okay, this is the end of the day you have a couple of commits, and you want to save your progress of the day on the server. For this we need to '*push*' those commits.
Because we cloned from the server repository, we can simply do `git push`.
This is because our branch 'main' has its '*upstream*' set to 'origin/main', so git knows whence our branch comes from and where to push and pull.
If we created our repository from scratch[^3], we must set this up with:
``` shell
git push -u origin main
```

[^3]: Most serious editors have git integrated: it shows you the lines you
    added/modified/deleted since the last commit, and provide an interface for
    interacting with git (staging, staging, etc.). For instance
    [magit](https://magit.vc/) for Emacs (yes I am biased but it is a really
    awesome git client).

[^4]: It is up to you, but as convention it tends to have imperative tense and uppercase
    first letter (to match commit messages generated by git from time to time), to be
    short and instructive (to easily find a commit in a long long log of them), and they
    **can** be followed by a small paragraph after a blank line, generally indicating
    **why** things were changed. It helps to not have too much things changed at once.

### Branching out

There are many features to git, but branches can be important and useful, so let's cover what they can do quickly.
As said previously a branch is a separate version of your project; the term is actually a good representation of it.
You can switch between branches to work on each version as you wish.
Branches can run parallel to each other but you can split them into more branches.

You can also synchronize two branches by '*merging*' them. This will not delete them, just synchronize them.
Merging can be a daunting process at first: if both branches did modifications on the same parts of your project, git cannot choose which modification to keep. You have to help and resolve the conflicts.

You can find more details in this guide: https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

Note that in this guide, the programmer only works in 'side' branches, never directly on the main branch.
This is standard procedure in software development or when working with others on the same repository, however this is not an obligation.
## Closing tips 

We only scratched the surface here, hopefully you will be able to start using git on a project, even simple, even alone, it will still have many benefits and make you learn some more!

There is of course a bazilion of content on git. A good starting point is the [Pro Git book](https://git-scm.com/book/en/v2) from which is the branching guide link above.
You can also always check the manual pages (`man git <whatever operation>`, or [online](https://git-scm.com/doc)), even though they might be a bit technical and 'dry'.
Don't hesitate to expand this list.

Some final tips:
- working on 'side' branches is a good habit to take, not necessarily at the very beginning, but it helps a lot when starting to collaborate with others
- you **will** make some mistakes and commit them. **It will happen**. And this is not a problem. You can '*revert*' a commit (this adds a new commit removing the changes of the last one), or just fix by hand and add a new commit.
  You can also '*amend*' a commit: this will remove it from the history and put its changes as 'staged', you can fix your mistake, stage it and commit like nothing happened, but...
- ... this means you have **modified the history** of your repository. And if you have watched one or two movies about time travel you know that in the end the plot makes no sense. It's fun and all, but **be wary** of any operation that touch the history, it's for the experts!
- Especially if you pushed it already. If by the time that you push a new history anyone had cloned or worked on your repository, they will be in a big mess. So even if you have pushed an embarrassing mistake, **origin is diamond**.

Happy gitting !
