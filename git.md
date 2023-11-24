# Using Git and Github/Gitlab

You may have noticed that this help repository is relying on git, so it's a first reason to learn about it if you want to contribute!

Plus it's really useful to save your work, to share your work, and to collaborate with others.

Sorry this guide is a bit lengthy but this is (I think) a really great and important tool, and not necessary easy to grasp at first.

## Which is which ?

Git is a software that does **version control**, when you '*commit*' it save the documents in your project directory to their current state.
You can easily check what has been changed between commits, revert your directory to a specific one, etc.
You can also create different '*branches*', which are co-existing versions of your project.

Your project directory constitute a '*repository*'. It can be linked to other versions of your repository, for example one on a server somewhere, or the one of your colleague.
In practice, there is one of them that act as the master version, the 'real' version. And most often it is stored on a server that offers additional services.

Github offers to store your repository and features such as viewing/editing the code, engaging in discussions, continuous integration (more on that later), and facilitating collaboration.
Note that Github was bought by Microsoft and is thus operating on their servers (it is free though).
Gitlab is a similar service but let your organization run the servers. The IN2P3 (a particle physics institute) has an instance open to all researchers in the [EduGain federation](https://technical.edugain.org/status), which in France includes institutions within this [list](https://services.renater.fr/federation/introduction/la-federation-education-recherche/fer-idps) (you are most likely on there).
Both are equivalent in terms of features, [gitlab.in2p3.fr](https://gitlab.in2p3.fr) is the recommended service for work-related projects, even though using Github can give you more visibility.

## How to I work with it ?

### The Editor

You can do a lot of things directly from Github or Gitlab by finding the 'add file' and 'edit' buttons. You can also use a more fully fledged code editor / IDE. In Gitlab it will be suggested as the 'Web IDE' when clicking the blue 'Edit' button. On Github you can find it on the main page of the repository, by clicking on the green '<> Code' button, then the 'Codespace' tab.
Both editors seems essentially the same, though the IN2P3 Gitlab instance could not open a terminal and run commands (maybe because I was using Firefox?).
The editor is based on Visual Studio Code so you might feel right at home[^1].

> Little tip: split the window in two (button on top right) to have the preview of how the markdown is going to look.

However, you might prefer using your own editor, on your own computer.
If the repository already exists on the server (you can create a repo from there)[^2], you must '*clone*' it on your computer.
The address will appear in the '<> Code' or 'Clone' button. It is either `https://gitlab.in2p3.fr/<username>/<project>.git` or `https://github.com/<username>/<project>.git`.

[^1]: uh technically 🤓 VS Code was created on web technology making this kind of stuff possible. Note you can similarly connect to your Github account from VS Code.

[^2]: If you already have an existing directory on your computer you can go in it and execute:
      `git init`. You can then create an empty repo on Github/lab, register it as a remote:
      `git add remote origin -u <url>`.


### Starting a project

We will use git in the command line in the rest of this guide, but you can also use a graphical client like [thoses](https://git-scm.com/downloads/guis) or extensions for your editor[^3]:
``` shell
git clone https://github.com/aang/restore-balance.git
```
This will create a `restore-balance` folder, with all the files and the git information.
The address of the original repo on the server is kept as a 'remote' named 'origin' by default.

If the original repo add one branch named 'main' ('master' was the old norm but it has evolved to main), you will end up with a '*reference*' named 'origin/main' that points to the server and a '*branch*' 'main', which sits on your computer.
Let's do some modifications to our local work directory. Having worked hard, we save our labor by creating a *commit*. We must first select the changes we want to save by '*staging*' them, for now let's stage everything then commit:
``` shell
git add
git commit -m "Learn waterbending from Katara"
```
Note the *commit message* indicated with `-m`, you can also use `-c` alone which will open your text editor for you to write the message.[^4]

Okay, this is the end of the day you have a couple of commits, and you want to save your progress of the day on the server. For this we need to '*push*' those commits.
Because we cloned from the server repository, we can simply do `git push`.
This is because our branch 'main' has its '*upstream*' set to 'origin/main', so git knows whence our branch comes and thus where to push and pull.
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

There are many features to git, but branches can be important and useful, so let's cover them quickly.
As said previously a branch is a separate version of your project; the term is actually a good representation of it.

For instance let's say we created a new branch 'bug at the commit B to fix a bug and worked on it a bit before going back to the 'main' branch and working on it as well:
``` raw

         C---D---E bug
        /
   A---B---F---G main
```

To create a branch simply use: `git branch <name>`. To change the current branch: `git checkout <name>`. If you have un-committed changes that could be overwritten by changing branch, git will tell you and not do it. Either commit or use [stashing](https://git-scm.com/docs/git-stash).

Now let's say the changes you did in the 'bug branch are ok and you want to incorporate them into 'main'. To do this, we need to '*merge*' the branches: that is to apply the changes of one of them onto the other.
You can do it into both direction (merge bug into main or merge main into bug), but a typical workflow involves creating a branch for "working on the side": adding a new feature, testing some configuration, etc. When that work is finished, the side branch is merged into the main one and eventually deleted.

This is what we are going to do: **merge bug into main** and keep main.
We first **go to the main branch**, think of it as the boss of things here: `git checkout main`.
Then we start the merge: `git merge bug`.

Git will create a new commit H that will combine E and G:
``` raw

         C---D---E bug
        /         \
   A---B---F---G---H main
```
But we have a problem: what if we modified the same parts of the same files in bug and main, how git will know which version to keep ? Well it won't, it will pause the process and ask you to resolve the conflict. 
A simple `git status` will show you the culprits. Edit those files[^5]: git will have left markers to show both versions:
``` yml
<<<<<<< HEAD:animals.yml
terrestrial:
  - Polar bear dog
  - Snow leopard caribou
  - Mink snake
=======
terrestrial:
  - Polar bear dog
  - Mink snake
>>>>>>> bug:animals.yml
```
Make the necessary corrections, save the file, and stage it (`git add animals.yml`).
You can now finish the merge with `git commit` (the message will be pre-written).

> Note that if we had not worked on main (F and G did not exist, and 'main' was at B) the merge would be very simple, git only has to move the 'main' pointer to E. This is a *fast-forward*.

This is all a bit complex, and can seem superfluous but it can be useful in many situations, especially when you start collaborating with others. If someone added commits to the main branch on the server, your local repository is not up to date anymore and there can be conflicts.
Git will not allow you to push! You have to get up to date by doing `git pull`, which can trigger a merge. Once resolved, you can push again.

[^5]: Git clients and editors can help you. `git mergetools` will try to find something installed for you.

## Forks and pull-requests

## Closing tips 

No modification of the history !
*Origin is diamond*.

https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

https://git-scm.com/doc
