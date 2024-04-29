# LaTeX

If you have never heard of it, in one sentence: it's a kind of code you write to turn your text, equations, figures, tables,... into a (*really*) nice document.
Instead of Microsoft Office Word or LibreOffice Writer, it does not show you in real time your document. You write your content, with some commands here and there, for instance to make some text `\textbf{in bold}`, and then run the LaTeX engine to turn it into a pdf.

This seems complicated, but it has several advantages:
- the output can be really pretty: because LaTeX has time to create the document (it's not real time) it optimizes the line breaks, paragraph breaks, and even does figure placement for you
- it handles bibliography really well
- it handles all sorts of automatic things: table of contents, footnotes, glossary, etc.
- because you can add your own code, there little to no little limitation to what you can do (you still need to understand how things work, and LaTeX can be a bit obscure if not arcane at times...)
- the *content* is separated from the *form*. Swap templates, or just change a few commands and your whole document is changed very easily.
- your document is a text file: it's very lightweight, even for a 200 pages manuscript, and works well with [version control](/Git/readme.md)

## Variants

There is many variants to TeX (it's pretty old), so if you are lost you can check [this guie](Engines_guide.md) on TeX variants.

## Software

What do you need to get started? This is covered [here](Software_to_use_guide.md).

## Documentation

For general LaTeX documentation, there is plenty of resources online and in books. Good starting points are:
- the [overleaf documentation](https://www.overleaf.com/learn), for beginners (and for experienced and curious users the advanced guides are interesting).
- [GUTenberg](https://mirror.gutenberg-asso.fr/), plenty of resources mostly in french, some in english as well in the [LaTeX Navigator](https://mirror.gutenberg-asso.fr/tex.loria.fr/)
- the excellent [memoir](https://ctan.gutenberg-asso.fr/macros/latex/contrib/memoir/memman.pdf) class has stellar documentation that covers the bases of TeX and typesetting.
- 🚧... add documentation that you think is worthy!

If you installed the documentation with the TeX distribution (see the [software guide](Software_to_use_guide.md#tex-live)) you can access it with `texdoc`.
Otherwise the documentation of any package can be found on [CTAN](ctan.org).

## Templates?

You can share here the code of one of your article, or your PhD manuscript, or a template you found interesting.
You can share smaller snippets in this folder.

- Source code: https://github.com/Descanonge/thesis with the result available [here](https://theses.hal.science/tel-04249198)
