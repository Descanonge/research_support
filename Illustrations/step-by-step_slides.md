# Step-by-step slide illustrations with Inkscape

Having step-by-step illustrations in your slides can be a great way do explain complicated processes or plots. I think here of parts of the plot (like a new line or subplot) appearing on each slide.
You can find examples in my PhD defense: https://github.com/Descanonge/soutenance/blob/master/presentation.pdf.

I am mainly going to discuss some Inkscape workflows to get step-by-step pdfs, and a little about the LaTeX code to insert the results in a beamer presentation. This can be useful even if you don't use LaTeX.
**If anyone knows of a similar way to do this in PowerPoint or Impress I'd be interested!**

The result can be really nice, but be warned this is quite some work: a lot of it for splitting up the illustrations in steps, and another good part dealing with LaTeX antics if you plan on doing your whole presentation in LaTeX.

## Splitting up an illustration

Let's assume you have an existing svg graphic: it can be an illustration you created with Inkscape, or one that you obtained from matplotlib for instance:
``` python
fig, ax = plt.subplots()
...
fig.savefig('my_graphic.svg')
```

From there we start to regroup objets into different layers by using the 'Layers and Objects' panel (it can be opened from the menu Layer>Layers and Objects). Each layer is named following the beamer overlay syntax, like so:
![example][example_layers.png]

(I uploaded this example on git because it's not so heavy -> https://github.com/Descanonge/soutenance/blob/master/resources/front_circulation)

There does not need to be a one-to-one correspondance between layers and steps.
As you can see the step 1 is split into two layers (`base` and `isopycnals`) which allows to add the `upwell` layer in between at step 6.
Also note that here all steps are kept until the end but this is not necessary, for example here we could keep one layer for only one step with `mld<5>`.

Now let's export all this to pdf. I propose two solutions.

## Inkscape slides

We can directly create each slide using [inkscape-slides](https://github.com/shosatojp/inkscape-slide).
This python script detects layers using the overlay syntax and create as many pdfs as there are steps, all independants:
``` shell
python inkscape-slide.py my_graphic.svg
```

Here is a quick script to organize things a bit, just give it the name of your svg file as argument:
``` shell
infile=${1:-unset}

if [[ ! -f "$infile" ]]; then
    echo "file ${infile} does not exist"
    exit 1
fi

name="$(basename "$infile" .svg)"

outdir="_${name}"
mkdir -p "${outdir}"

cp "$infile" "${outdir}/"
python inkscape-slide.py "${outdir}/${name}.svg" --format "${outdir}/{1:d}.pdf" --inkscape-args ''
```

Watch out for a couple of kinks:
- layer names should be kept simple, avoid weird characters and accents
- some path effects *might* not work, you might need to apply them

It's quite easy to input those into LaTeX:
``` latex
\includegraphics<1>{resources/_my_graph/1.pdf}
\includegraphics<2>{resources/_my_graph/2.pdf}
\includegraphics<3>{resources/_my_graph/3.pdf}
...
```

We can automate things a bit using latex3.
``` latex
\RequirePackage{expl3}
\RequirePackage{xparse}

\NewDocumentCommand \multigraph { O{} m m }{
  \int_step_inline:nn {#2 - 1} {
    \includegraphics <##1 | handout:0> [#1] {#3/##1.pdf}
  }
  \includegraphics <#2-> [#1] {#3/#2.pdf}
}
```
We can then give the includegraphics options, the filename, and the number of steps:
``` latex
\begin{frame}
    \multigraph[width=0.9\textwidth]{my_graph}{6}
\end{frame}
```

Boom. And as you may have notice it handles the handout option of beamer gracefully by only keeping the last step when in this mode.

But because each step includes copies of what's in the previous slide, it may increase the volume of your slides, especially if they include 2d images.

## Batch-export

This next solution overcome this issue by exporting each layer and then reconstruct the illustration in LaTeX. It's a bit more handywork though (but you might find a way to automate this in LaTeX?).

We will use this time the [batch-export](https://github.com/StefanTraistaru/batch-export) Inkscape extension. Follow the intall instructions and then, using the same example file as before, export your layers from the menu: Extensions > Export > Batch export.
From the panel select your output directory (`_my_graph`) and once everything is configured click apply.
Be sure to appropriately set the export size: all outputs must have the same size to line up correctly. One way to do this is to select a 'page' export size and adjust the page size to your graphics (with Edit > Resize page to selection for instance).

You will find in the output directory each layer as a separate pdf.
Note that here the overlay syntax is not mandatory but we're going to keep it to make things clearer.

We can now import that into LaTeX; it will be more tricky.
Superposing pdfs is actually pretty easy:
``` latex
\includegraphics<1->{layer_base.pdf}%
\llap{\includegraphics<2->{layer_2.pdf}}%
\llap{\includegraphics<3->{layer_3.pdf}}%
```

But typing for each layer all the includegraphics options can quickly turn messy. We define a `\graph` command that will repeat these options for us (the definition is only valid inside the group so it does not clash between different frames): 
``` latex
\begingroup
\newcommand\graph[2]{%
  \llap{\includegraphics<#2>[height=0.75\textheight]{_front_circulation/#1<#2>.pdf}}}%

\begin{frame}
  \frametitle{Impact des fronts sur la croissance du phytoplancton}
  \frametitle<6->{Impact des fronts sur la stratification}
  \includegraphics[height=0.75\textheight]{front_circulation/transparent/base<1->.pdf}%
  \graph{upwell}{6-}%
  \graph{isopycnals}{1-}%
  \graph{jet}{2-}%
  \graph{vorticity}{3-}%
  \graph{circulation}{4-}%
  \graph{mld}{5-}%
\end{frame}

\endgroup
```

This is a bit menial but is quite flexible. It could also theoratically all put together in a python script (running batch export automatically and generating some LaTeX, maybe someday...).
