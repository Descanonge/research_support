# Information specific for LOCEAN

## Visio

CNRS is providing a Zoom account. Go to https://cnrs.zoom.us and sign-in using Janus.
To use the client, when signing-in use the SSO (Single Sign-On) button. Specify `cnrs` as the company domain. This will then redirect you towards Janus authentication in the browser.
More information [here](https://ods.cnrs.fr/zoom-cnrs.php).

To install on Linux (Ubuntu or debian) if you are root, download the `.deb` file from https://zoom.us/download and then run:
``` shell
sudo apt install ~/Downloads/zoom_amd64.deb
```
(apt is now able to do that and solve dependencies, no need to go through dpkg normally).

If you are not root, download the `.tar.xz` file for the 'Other Linux OS' and extract it somewhere you will keep. `/opt` or `~/.local/opt` by example.
To make your system aware of it link the executable somewhere in your path:
``` shell
ln -s ~/.local/opt/zoom/zoom ~/.local/bin/zoom
```

To have an entry in your application menu create the file `~/.local/share/applications/zoom.desktop`:
``` desktop
[Desktop Entry]
Name=Zoom
Exec=zoom
Type=Application
Terminal=false
```
that should do the trick.

## Password manager

You noticed you already have multiple credentials to remember... And it's not going to get better.
We **highly** recommend you use a password manager to track all of those.
This avoid using weak password by generating them at random (no even if you write in leet, 'ilov3c4ts' is going to get cracked *very* easily).
A lot of software exists with plenty of features which makes everything very easy.

I can personally recommend [Bitwarden](https://bitwarden.com/): open source and free[^1], with plenty of features. It runs on pretty much everything (from your browser, browser extension, phone app, client for computer, even with linux command-line!). Your passwords and other info are stored encrypted on servers, on the plus side you can access it from anywhere but some could see this as a liability.

Are there some more that you have tested ?

[^1]: There is a free version that should more than cover your needs, and paid plans are really cheap should you need them.
