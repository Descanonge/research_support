# Specific informations for LOCEAN

## Lab documentation

There is already existing documentation for/by the lab.

The **welcome booklet** is currently available on the DropSU cloud storage (as of 2023-11-05). You will need a Sorbonne login, hopefully this is temporary until we get a better intranet and/or more stable documentation.
- https://dropsu.sorbonne-universite.fr/f/193630834 (in english)
- https://dropsu.sorbonne-universite.fr/f/193630819 (in french)
If you have trouble accessing it ask to a senior PhD.

The **IT documentation** covers more technical subjects: mail, wifi, VPN, printers, etc. It is available *in french* in the intranet at http://info.locean-ipsl.upmc.fr/fr/.
This means you need either:
- to be connected by ethernet at the lab, which requires an approved machine.
- to use the proxy (see below)

Of course you can find more 'informal' information in this repository (more like folk's know-how), and if you still have questions you can open an issue here, or send a mail to the [IT team](http://info.locean-ipsl.upmc.fr/fr/support/).

## Proxy setup

You can use the proxy to access some lab resources from the outside (intranet, cloud). It also gives you access to some reviews.
You can set it up in your browser settings (for Firefox: Settings > General > Network settings > Configure how Firefox connects to the internet > Manual proxy).
You can also use an extension to quickly activate or deactivate the proxy, like [FoxyProxy](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/), also available for Chrome.

- proxy HTTP: <adresse du proxy>
- port: <port>
- username: LOCEAN login (initial of given name + family name | initiale prénom + nom)
- password: LOCEAN password

## VPN setup

The VPN allows to redirect all your internet traffic through the IPSL (whereas the proxy only works for the http protocol, and thus is less secure).

To setup the VPN, you first need to go to the intranet [here](http://info.locean-ipsl.upmc.fr/fr/reseau-distant/#vpn) and download the configuration files.
You can extract them for instance in `~/.config/vpn-ipsl` or a similar location.
You should have a certificate (`ca.crt`), a PGP key (`ta.key`), and a configuration file (`vpn-ipsl.ovpn`).

Follow the instructions on the intranet to install it.

The username should be: `<LOCEAN login (initial + family name)>@locean.ipsl.fr`.
The password is your LOCEAN password.

### Troubleshooting

Currently (november 2023), the IPSL VPN system is not up to date.
It uses an obsolete algorithm to check the validity of your certificate (if I understand correctly the certificate signature is obtained from MD5 or SHA1 which can be easily broken now, anyone could impersonate the VPN server).
Your system (which should have an up to date client) is unhappy about that and might refuse to connect. When activating the VPN it is going to fail by timeout.
You can confirm what is happening with (you might need to be root):
``` shell
journalctl -r -u NetworkManager
```
You will then find those lines in the output:
``` plain
VERIFY ERROR: depth=0, error=CA signature digest algorithm too weak: C=FR, L=Guyancourt, O=LATMOS, OU=LATMOS, CN=vpn.ipsl.upmc.fr, emailAddress=xxxx@latmos.ipsl.fr, serial=25
OpenSSL: error:0A000086:SSL routines::certificate verify failed
```

The person in charge should have been notified by now but things are moving slowly...
You can find workarounds allow the use of weak signature by more or less disabling the certificate signature check.
Needless to say this is not a good idea and is a security risk. I cannot explain it publicly here, but if this is an *absolute necessity* I guess someone knows how to do it in 426.

If not working, prefer the alternatives of the proxy and the SSH bridge.


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

## Cloud

You should have access to the IPSL cloud, which is powered by Nextcloud.
This is the preferred solution to store, backup and share files (rather than private solution like Dropbox, Google, etc.).
It allows has plenty of applications: cooperative edition of documents (using OpenOffice, which you should also have on your machine), calendar, todo list, kaban deck, forms, etc.

You can access it in your browser at https://cloud.ipsl.fr with your lab credentials: `<initial + family name>@locean.ipsl.fr` and your usual password.

You can also use a local client to synchronize your files automatically. It should be already installed on your machine, under the name of the Nextcloud client.
To set it up, just give the url of the cloud above, and sign in normally in the browser that should have opened.
You can then setup one or more directories to synchronize automatically.

You can also access to your files on the cloud without synchronizing by using the WebDAV protocol.
It is actually really easy: go to [your files](https://cloud.ipsl.fr/index.php/apps/files/) on the browser and click on 'Files settings' in the lower left corner. Copy the url under WebDAV.
Enter this url in your file manager path bar (for some other clients you might have to do some different manipulations, check this [wiki page](https://wiki.archlinux.org/title/WebDAV#Client)), and replace `https` by `davs`: it should look something like this: `davs://cloud.ipsl.fr/remote.php/dav/files/some-long-token`.
Enter your credentials once more, and you should have direct access to the files on your cloud!

You can save this address as a shortcut for easy access.
It's obviously up to you but a nice workflow is to have this shortcut when you want to look at your remote files from your machine, and have some select folders here and there that you actively synchronize.
Let's try to avoid too much network consumption by synchronizing only what is necessary.

NB: You can also use a client for your phone (there are Nextcloud applications).

## Password manager

You noticed you already have multiple credentials to remember... And it's not going to get better.
We **highly** recommend you use a password manager to track all of those.
This avoid using weak password by generating them at random (no even if you write in leet, 'ilov3c4ts' is going to get cracked *very* easily).
For most managers, browsers extensions and phone apps exists which makes everything very easy.

Bitwarden and ... are free and open-source.
