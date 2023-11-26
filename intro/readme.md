# Introductory Guide

Some of the key subjects you might need or want to check out.

## Git

[Git](git.md)

## Bash


## Python

[Setting up](Using Python/setting_up.md)

## Writing

## Editors

Let's begin by defining what is an IDE: Integrated Development Environment. A software to write code that has plenty of tools to help you: smart completion, linting (check your code for syntax errors), compilation, git integration, etc.
There are generally only made for one specific language, but quite powerful.
- Spyder: for Python
- Rstudio: for R
- Matlab
- TexStudio: for LaTeX
- CodeBlocks: for C, C++, Fortran
Jupyter lab could count as an IDE.

All of those are great but some prefer to do everything in the same software.
Generally you add features by adding plugins that make your editor IDE-like.
Same features, sometime even better and more configurable, but not necessarily as streamlined. Stuff might not work from time to time.

Gedit: pretty basic, generally available, can be extended somewhat.
Notepad++: ?

Now we are left with the big contenders.
Visual Studio is a microsoft code editor for which most plugins are developed by the community (there used to be Atom, an alternative but it was too much work to keep up).
It has lots of users, is quite customizable, and plugins can add some impressive features. Definitely a good choice if you don't want to spend *too* much time on setting your editor up.

The next two editors are somewhat special. Vim and Emacs have been around for some time (this is an understatement, there are probably the oldest user software still widely in use), and can be quite daunting to get into. But if you don't mind an all-keyboard interface, and spending some time in their innings (or even like it) the reward is pretty good.

Note that you can still use them "vanilla", without (too much) plugins or configuration, they are still *very* good.

Let's start with Vim quickly, the best text-editor around!
It is probably already on your machine (it is everywhere!). It is a terminal software (though there exist GUI like vim-gtk): so let's open a terminal and edit a document: `vim mydoc.txt`.
Vim normally opens in **normal mode**, where the keys do not insert characters, but execute actions.
If we want to write a sentence, we press **i** to go into **insert mode**, now we can write whatever we want and press **escape** to go back to normal mode.
Some examples of actions include:
- gg: go to the top of the file
- 0: go to the beginning of the line
- w: go to the beginning of the next word
- cw: remove the text up to the next word and go into insert mode
- etc.

You can find more information there: https://vimhelp.org/.
Plenty of plugins exists that can extend its features close to an IDE (see [neovim](https://neovim.io/)).

This is an odd system for sure, and requires some learning but it can be done little by little and soon you will be able to edit a text blazzingly fast with a couple of keystrokes.
It is also a good way to edit a file from a terminal quickly, even on a remote machine.

Last but not least is Emacs. It is closer to a standard editor, with plenty of chord-like keybindings. For instance to save the current file you type Ctrl-F then Ctrl-S.
Just as is, it is a powerful editor with plenty of keybindings.
But the real magic of Emacs is the way it works: like any software Emacs is a collection of variables and functions. Well **all** variables and functions are accessible to the user.
Emacs is made for you to change the values of variables (this is how you configure it), or re-define functions to your liking.

Extending Emacs is very easy: it is self documented (and really well documented), and you can make change while it is running!
Want proof? The community re-implemented Vim in Emacs, so with just a plugin you can use Vim modal editing (and then you don't have to learn Emacs unusual keybindings)!
This makes an infinitely customizable editor, as powerful as you make it.
Turning it into an IDE is not easy though, but some projects have created "Emacs distributions" that will get you started in no time: [Doom Emacs](https://github.com/doomemacs/doomemacs) and [Spacemacs](https://www.spacemacs.org/)
