We chose to work with forks and pull-requests, which I will justify later.
Instead of working directly on the original Github repository (`Descanonge/research_support`), you have to duplicate **your** own version. This is a fork: you essentially clone the repository but not on your computer, on your Github profile.
*This implies that you have to create a Github account* if you do not have one already.
To fork the project, click on the 'fork' button at the top right of the main repository page. You can keep everything as default, even the name does not need to be changed.

You are now on *your* version of the repository (`https://github.com/your-username/research_support`) and you can do all the modifications you want.
You can use the browser editors (see the section [the Editor](the-editor)), or clone the repository and work on your computer (like we did in the section [Starting a project](starting-a-project)).

Once you are done, everything is pushed, you should be able send those changes back to the original repository by asking a '*pull-request*' (or PR). To do this, on the main page of your repository, click on 'Contribute', under the green '<> Code' button.
The administrators of the repository will receive a notification and can validate your changes. You can check this process at https://github.com/Descanonge/research_support/pulls.

About the choice of forks and PRs: this is the default way to collaborate at large scales, it makes it easy to add changes from different people while avoiding breaking stuff.
However our project is far from *needing* this. Some other solutions might be more adequate and we have to experiment. Don't hesitate to voice concerns or proposal :)
A possibility for example would be to add contributors to the list of members having permissions to edit, so you could work directly on the main repository. It may require some organization (force branching for example).