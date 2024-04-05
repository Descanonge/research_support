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