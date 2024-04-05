# Matplotlib bases

## Colormaps

### Maps

Colormaps are key in our field and it is important to choose them carefully.
Some colormaps are, to put it plainly, quite bad. The most infamous example is the 'jet' colormap, which can make structures appear to our eye where there is none.
To avoid that you want your colormap to be 'perceptually uniform': what your eye sees should reflect accurately the data values, all across the range of the colormap. 

And all eyes are not equal: between 3% and 7% of the male population has some form of red-green colorblindness (the rate among women is an order of magnitude lower).
We have to take this into account.
And as a bonus, it can be useful to have a colormap that stays correct when converted to grayscale.
See [Thyng et al. 2016](https://tos.org/oceanography/assets/docs/29-3_thyng.pdf), or the plethora of resources [here](https://matplotlib.org/cmocean/#why-jet-is-a-bad-colormap-and-how-to-choose-better), if you're interested in details.

Matplotlib default colormaps have been corrected and should be safe to use (see this [blog post](http://bids.github.io/colormap/)).

A very good starting point is [cmocean](https://matplotlib.org/cmocean/): 'beautiful colormaps for oceanography', readily available for Python (and others).
Note that these were [evaluated](https://matplotlib.org/cmocean/colormaps_viscm.html#colormaps-viscm) for moderate forms of colorblindness that should account for the majority of deficiencies but can still be degraded for some people. You can always check your plot with the tools below.

You can also find the very nice colormaps from Fabio Crameri: https://www.fabiocrameri.ch/colourmaps/

### Lines and cie.

Inclusivity must also be taken into account for other plot elements: lines, points, patches, etc.
For those, it is useful to have discrete sets of colors.
You can create you own or test such sets on this website: https://davidmathlogic.com/colorblind.
You will also find examples of sets: IBM, Wong and Tol. 

The last one is taken from a quite comprehensive collection of colorblind safe schemes (different base sets, high contrast set, pale and dark sets if you want text over it, and some discrete colormaps). See the website of the creator for details: https://personal.sron.nl/~pault/.
It is packaged for python [here](https://github.com/Descanonge/tol_colors) ;).

Of course you can also use other properties than colors to make your plot more readable: linestyle, linewidth, hatching, etc.
You can also give a legend close to the plot so that the reader can easily compare the legend to the plot. Or even have your legend *on* the plot, like a label next to each line.

### Check your plot

Checking the overall plot for colorblindness inclusivity is a good idea.
Here are tools to test your plot:
- http://mapeper.github.io/jsColorblindSimulator/
- https://www.color-blindness.com/coblis-color-blindness-simulator/

## Configuration

You can configure matplotlib so that your plots are nicer/to your liking.
See this page of the documentation: https://matplotlib.org/stable/users/explain/customizing.html

Here is an example of file, you can save it as `~/.config/matplotlib/matplotlibrc` or `./matplotlibrc` (your current directory).
You can also save it as `~/.config/matplotlib/stylelib/mystyle.mplstyle` and activate it with:
``` python
import matplotlib.pyplot as plt
plt.style.use('mystyle')
```

Anyway here is the file:
``` yml
xtick.direction : in
ytick.direction : in

axes.grid : True
grid.linestyle : :

legend.fancybox : False

# Paul Tol colorset, colorblind safe ('bright' version)
axes.prop_cycle : cycler('color', ['4477AA', 'EE6677', '228833', 'CCBB44', '66CCEE', 'AA3377', 'BBBBBB'])

font.family : DejaVu Sans
font.style : normal

svg.fonttype : none

mathtext.fontset : custom
mathtext.default : regular
mathtext.it : DejaVu Sans:italic
mathtext.rm : DejaVu Sans
mathtext.cal : DejaVu Sans
mathtext.fallback : cm

font.size : 9.0
xtick.labelsize : small
ytick.labelsize : small
legend.fontsize : small
axes.titlesize : medium

text.usetex : False
text.latex.preamble : \usepackage{bm} \usepackage{siunitx} \setlength{\parindent}{0in}
```
