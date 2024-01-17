# LaTeX

Some basic info on our favorite typesetting system. 

## Variants

To avoid being lost in all those names.

### Formats and engines

TeX is the original system. Not used directly anymore, but serves as the base of everything else.

We then have **LaTeX**: the successful follow-up. It adds plenty of commands that make writing a document easier, as well as a package system. Nearly all other systems are derived from it.
It is still in active development, at the version `LaTeX2ε` (I really picture TeX developers as long-bearded nerds with both a math and a computer science doctorates. I mean: did you know that each new version of TeX adds a digit to the version number. It is currently 3.141592653, and when the original author will die it will be changed to π...).

LaTeX is a *format*, like TeX. To produce a document you need to use an *engine*.
The 'base' engine is **pdfTeX**, which you typically run with the `pdflatex` command.

Another engine is **XeTeX**, designed to select fonts more easily.

The **LuaTeX** engine also supports selecting fonts, and also opens the insides of TeX by using the Lua scripting language. That makes for easier programming, though it is mostly aimed at package developers and more recent additions to the LaTeX kernel also allows for more complex programming.

### What to use?

Which one do I choose? Most importantly, XeTeX and LuaTeX support Unicode characters in your files, which might cause trouble for pdfTeX. I would thus avoid pdfTeX and put as much weĩrd lettɇrs as I wånt.
XeTeX and LuaTeX are pretty equivalent, with maybe a slight advantage for LuaTeX which is now the default engine of the LaTeX development team. Be sure to look at the documentation of the packages you use that should specify the differences in features (for example for packages [microtype](https://ctan.org/pkg/microtype) or [babel-french](https://ctan.org/pkg/babel-french) out the top of my head).
The format is the same so you can switch engines without modifications, save for a couple of lines in your preamble mostly.

You might hear about **ConTeXt**. It is kind of format and thus is not written like your typical LaTeX.
It uses a special command that call a engine (LuaTeX, which was developed for ConTeXt initially).
It is mainly geared towards automatic document generation (stuff like catalogs for example), so a priori not that useful to us.

## Software to use?

### Overleaf

[Overleaf](https://www.overleaf.com/) is a very straightforward way to start LaTeX. No need to install anything.

We recommend using the [PLM instance](https://plmlatex.math.cnrs.fr/login), accessible with an institutional login. You can find more information on its [documentation](https://forum.math.cnrs.fr/t/documentation-plmlatex/542).
You should note that, like the free Overleaf version, github/gitlab/dropbox integration is **not** available.
But contrary to Overleaf, you do have access to more than one collaborator (unlimited actually), the compilation time can exceed 1mn (up to 10mn), and you have access to the modifications history.

> I personally have my reserves on such tools, considering that your data is on a single server and could potentially not be available if the tool is down. A loss of data is less probable but still possible.
> If you decide to use this tool, integration with github/gitlab/dropbox is a very good idea, so that your soon-to-be Nature article is copied very often and automatically to another place.
> You can also download regularly your source code (in Menu > Source), but this is cumbersome.
> *Don't take any chance with your thesis manuscript!*

### Distribution

You need to have the engines, the packages (La)TeX code, etc. To help there you typically use a distribution that ship all of that nicely.

#### TeX Live

On Unix, TeX Live is the go-to distribution, installed through the package manager.
You can install **everything** with the package `texlive-full` but this can be heavy (multiple GBs).
It can be wise to install as you need. LaTeX packages are grouped in Ubuntu/Debian/Whatever packages.
So you might need `texlive-science` for the beloved [siunitx](https://ctan.org/pkg/siunitx). This can lead to downloading more packages than you really need.
You could use the program `tlmgr` to download packages one by one.
You can avoid most of the weight by not installing the documentations (`texlive-science-doc` for instance), which downloads plenty of pdfs that you can find online anyway.

If you do have the documentation installed, be sure to check the `texdoc` software (accessible as command line and GUI).

TeX Live is released yearly. This ensure minimal clashes between packages (because there is no real version control in LaTeX packages), but you might not have the latest version available of a package.
If this is really a problem, you can download the latest version of the `.sty` package and place it in your document folder or `$TEXMFHOME`.

#### MiKTeX

MiKTeX is available on Windows, as well as on MacOS and some distributions of Unix.
It contains the editor TeXworks.

#### MacTeX

Equivalent of TeX Live specifically tailored for MacOS. It contains Mac compatible software like TeXShop.

### Programs

You might know that running latex once is sometimes not enough, like if you have cross-references, a table of contents, a bibliography, etc.
Some software can take care of that complexity for you. Most GUI applications should allow you to configure the compilation appropriately. It might rely on the tools below.

There are some software that can automatically check if an additional round of processing is necessary.
Maybe the most well-known and well-rounded is [latexmk](https://www.cantab.net/users/johncollins/latexmk/) (you might have to install it).
The full compilation will simply look like:
```shell
latexmk -lualatex -interaction=batchmode -recorder my-pnas.tex
```

And if nothing needs to be changed, nothing will be done! It can also be running continuously and compile the document as soon as the source·s file·s have changed.
There many options that you can explore.

Sometimes the command can start to become quite hairy. You can use a Makefile to ease that. For instance, here with a build directory where all auxiliary files will be hidden:
```Makefile
BUILD_DIR := build

MAIN := my-pnas

AUXDIR_FLAGS := -auxdir="$(BUILD_DIR)" -emulate-aux-dir
LMK_FLAGS := -lualatex -interaction=batchmode -recorder -quiet

.PHONY: all clean $(MAIN)

all: $(MAIN)

$(MAIN): $(MAIN).tex
    latexmk  $(LMK_FLAGS) $(AUXDIR_FLAGS) $(MAIN).tex

clean:
    rm -rf $(BUILD_DIR)
    rm -f $(MAIN).fls
```

You can also specify more options in a `.latexmk.rc` file, to parse the logfiles with `pplatex` for instance.

Some other options:
- [arara](https://islandoftex.gitlab.io/arara/)
- [rubber](https://gitlab.com/latex-rubber/rubber/)
- [latexrun](https://github.com/aclements/latexrun)

Latexrun seems like a good alternative to latexmk, with a good informative output (without having to parse it). It may lack some features (glossaries?).

Here is a comparison of different methods in build time: https://blog.martisak.se/2023/10/01/compiling/

If you are feeling adventurous you can try [Tectonic](https://tectonic-typesetting.github.io/en-US/), which is refreshing in its simplicity: a single executable will produce a document in a single run and download any package if it is needed. An impressive and interesting project for sure, but it should be considered in beta.

## Templates?

You can share here the code of one of your article, or your PhD manuscript, or a template you found interesting.
You can share smaller snippets in this folder.

- Source code: https://github.com/Descanonge/thesis with the result available [here](https://theses.hal.science/tel-04249198)
