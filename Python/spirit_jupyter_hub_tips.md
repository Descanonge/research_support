# Spirit Jupyter-Hub Tips

The mesocentre provides an instance of jupyter-hub, a cloud platform that can run jupyter labs or notebooks across a cluster.
It can be run from spirit, spiritx, or jean-zay.
The documentation to set it up and use it is here: https://documentations.ipsl.fr/spirit/jupyterhub/documentation.html

However, it may not be always completely clear so here are some additional tips.

## Connection

You can access the hub at those addresses:
* spirit: https://jupyter-su.ipsl.fr/spirit
* spiritx: https://jupyter-x.ipsl.fr/spiritx

But you need to be in the IPSL network to have access to it.
You can use the VPN if it is setup correctly on your computer, but currently this is rather unlikely... so you may need to use a SOCKS5 proxy.
A proxy is just like a VPN, but it only works inside your browser.

We need to configure the proxy, and setup a SSH connection for the proxy to go through.

### Proxy

You can use the basic firefox settings to setup the proxy (Settings > General > Network Settings > Settings... > Manual proxy configuration). But this is cumbersome to activate and deactivate.
It is very recommended to use the FoxyProxy extension for Firefox or Chrome. The documentation on how to configure it is available there (https://documentations.ipsl.fr/spirit/common/foxyproxy.html) but I will try to make it clearer along the way.

Follow the instructions on how to add a new proxy, and when it comes to configure it here are some pointers:
* **Title:** Whatever you want, "Spirit JupyterHub" sounds good
* **Type:** `SOCKS5`
* **Hostname:** `localhost`
* **Proxy DNS:** On
* **Port:** Whatever you want between 1024 and 65535. You **need** to keep the same value in the following steps. Avoid using the same value as someone else. I will use `1312` here.

All the other stuff must be left blank: do **not** input your login or password here.

The rest of the documentation is delving into the details of setting up pattern to automatically activate proxies when you open some URLs. This is a lesser concern. You can circumvent this anyway:
* go to the jupyter-hub url
* click on the FoxyProxy extension
* expand the "more" tab
* in the expanding list, choose your new lovely proxy, for me: Spirit JupyterHub
* you can click "Quick Add" to add this URL to the patterns automatically, so you can use "Proxy by Patterns" next time
* you can also click "Set Tab Proxy" (with the proxy selected in the list) so that it is active only in this tab of your browser. You must reload the page.

### SSH 

This will only cover linux :/ Look for setting up a SOCKS5 proxy, you should find the information easily enough.

We just need to connect to spirit, spiritx, or jean-zay as normal, but add a "dynamical port forward" option. In the `.ssh/config` file it correspond to "DynamicalForward" and in the CLI it's `-D <port>`.

So if our normal configuration looks like this:
```
Host spirit
    HostName spirit1.ipsl.fr
    User chaeck
    IdentityFile ~/.ssh/id_ciclad  # yes i'm so old it was called ciclad at the time
```
we launch `ssh -N -D 1312 spirit`. The `-N` option avoids opening an interactive session, but it is optional. Note that we used the same port as in the proxy configuration.

If you want an even quicker command, we can add this to `.ssh/config`:
```
Host spirit-tunnel
    HostName spirit1.ipsl.fr
    User chaeck
    IdentityFile ~/.ssh/id_ciclad
    DynamicForward 1312
    SessionType none
```
and simply use `ssh spirit-tunnel`. The `SessionType none` line is equivalent to `-N`.

### Password

You launched the SSH tunnel, activated the proxy, and went to the correct jupyter-hub address. If everything is going well, you should see a login window. Your id is the same as the one you use when connecting (ie `<login>@spirit1.ipsl.fr`). And you probably have to create a password. Just follow the instructions for that.
