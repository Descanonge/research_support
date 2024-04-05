You can run Jupyter Notebook on TGCC while accessing the outputs of numerical simulations. The official TGCC documentation provides light guidelines for this, but if you encounter issues, these steps may help.
  
Your feedback and suggestions are highly appreciated. Please feel free to share any ideas or improvements you may have.

To remain anonymous, consider a user having the login `toto`, belonging to the project `gintonic`on the container of Irene named `container`. 
## Preparing Your Environment

If you have already created your Conda environment with Jupyter, proceed directly to the next section. Otherwise, go to the next section to set up your environment:

1. **Open an Interactive Session on Irene**

For detailed instructions and parameters, please consult the [TGCC documentation](https://www-hpc.cea.fr/tgcc-public/en/html/toc/fulldoc/Supercomputer_architecture.html). Additionally, requesting resources on `hybrid` is often easier and quicker than on `xlarge`. It's important to note that a `console` session runs twice as fast as a `virtual` one.

```bash

ccc_visu console -p xlarge -A gintonic -m store,work,scratch

```

placeholders:
-p : configuration of Irene (more info in the [doc](https://www-hpc.cea.fr/tgcc-public/en/html/toc/fulldoc/Supercomputer_architecture.html))
-A : project you belong to
-m : accessible spaces (more info in the [doc](https://www-hpc.cea.fr/tgcc-public/en/html/toc/fulldoc/Data_spaces.html?highlight=partition))
optional placeholders:
-T : time limit in seconds (by default set to 2h)

2. **Starting a Jupyter Session**
While on the visualization node, go to your work directory to avoid memory limitations. Load your Jupyter environment and launch your Jupyter Notebook. You can sum up these commands in a function in the `.bashrc`.
```bash
cd $CCCWORKDIR
source /ccc/work/container/gintonic/toto/python_env/pyjup/bin/activate
jupyter notebook
```

Ensure you symbolically link `.conda/` and `.local/` in your work directory for proper memory management.

3. **Set Up a Proxy on the Gateway Server**

On your local machine, run the following command:

```bash
ssh -D 9080 -i ~/.ssh/id_uga toto@ige-ssh.u-ga.fr -v
```

Configure your browser to use the proxy with the correct port.
In Mozilla Firefox:
1. Go to 'Parameters' > 'Proxy'
2. Select 'Configuration manuelle du proxy'
3. Enter the following:
- Hôtes SOCKS: 127.0.0.1
- Port: 9080
4. Check 'SOCKSv5'
5. Check 'Utiliser un DNS lorsque SOCKS v5 est actif'
6. Leave the other fields empty.


4. **Enter the Graphical Session**
Open the web link printed in the shell after logging in to the interactive sessions on the [visu-fr.ccc.cea.fr](https://visu-fr.ccc.cea.fr) website (use the link provided in the shell !).

You have two options: you can either open the DCV client within the same browser or, in my opinion, it's best to open it via the DCV application (the download link is available on the same page).

For Mac users: any arm64 or x86 distribution works for newer Macs.

Occasionally, the newest version of the DCV client might not be compatible with the latest version of your operating system. In such cases, you may need to try using an older DCV distribution.

To configure the DCV application to pass through the proxy (SOCKS v5 and port) before loading the .dcv file, follow these steps:

1. Open the DCV application.
2. Navigate to Connexion Settings > Proxy.
3. Configure 'Get throught SOCKSv5 proxy'
4. Enter the following: 127.0.0.1 : 9080
5. Leave unchecked the box 'Proxy server requiring password' line and leave empty the Username/Password fields.
6. Apply.

> Follow the identification process and enter your Irene credentials. Now, you have a Linux graphical session where you can open an internet browser or a terminal on Irene.

## Creating Your Python Environment --- with Conda

On the gateway machine, generate a Python environment with Conda that includes Jupyter. Jupyter built in with Conda usually works better than Jupyter installed externally. Follow [Nicolas's page](https://nicojourdain.github.io/coding_dir/coding_python_tgcc/) for additional guidance.

```bash

# Replace with the appropriate file URL
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Accept to initialize Miniconda3
. ~/.bashrc

echo "y" | conda create --name pyjup python=3.8 jupyter
conda activate pyjup

# Install necessary packages

echo "y" | conda install numpy ipython netcdf4 xarray matplotlib scipy pandas pillow
echo "y" | conda install dask
echo "y" | conda install zarr
echo "y" | pip install watermark
echo "y" | conda install cartopy
echo "y" | conda install -c conda-forge cmocean
echo "y" | conda install -c conda-forge papermill
echo "y" | conda install -c conda-forge gsw
echo "y" | pip install tqdm
echo "y" | conda install -c conda-forge pyinterp
echo "y" | pip install conda-pack

#xarray=0.15.1=py_0
# Update Conda environment

conda update -n pyjup --force-reinstall --update-all

# Create a Conda package
conda-pack -n pyjup -o condapack_irene_pyjup.tar.gz --ignore-missing-files
```

Dedicate a directory on your workspace for Python environment. Check if on which server you connect. On the gateway server, transfer your tar file with, for instance, this command:

```bash
scp -p condapack_irene_myp.tar.gz toto@irene-amd-fr.ccc.cea.fr:/ccc/work/container/gintonic/toto/python_env
```

Untar your file `tar -xvf condapack_irene_pyjup.tar.gz myenv`
To load your Python environment on Irene, use the following command:

```bash
source /ccc/work/container/gintonic/toto/python_env/pyjup/bin/activate
```

---

## Accessing Files on Irene
To transfer files to and from Irene, establish an SSH tunnel from your local machine. Then, use `scp` to send or receive files.

**Establish an SSH Tunnel:**
To transfer files to and from Irene, you need to establish an SSH tunnel from your local machine. Follow these steps:

1. Open a terminal on your local machine.
2. Use the following command to establish the SSH tunnel:

```bash
ssh -Nvi ~/.ssh/id_uga -L 1234:irene-amd-fr.ccc.cea.fr:22 toto@ige-ssh.u-ga.fr
```
1 **Immediate transfer with scp**

It allows to receive or send with one line command a targeted file. Quickly redondant.

1.1 **Sending Files to the Server:**
Now that the SSH tunnel is established, you can send files to the server. Use the following command to send a file:
```bash
scp -P 1234 your_local_file toto@127.0.0.1:destination_on_the_server
```
1.2 **Receiving Files from the Server:**
To receive files from the server, use the following command:
```bash
scp -P 1234 toto@127.0.0.1:/ccc/work/container/gintonic/toto/python_notebook/draft/*.pdf /localdir/
```

2 **Opened transfer with sftp**

Or open a transfer connexion with
```bash
sftp -P 1234 toto@127.0.0.1
```
Then,
```bash
cd /ccc/work/container/gintonic/toto/python_notebook/draft/
lcd /Users/antoinenasser/Documents/work/outputs_tgcc/
get *.pdf
```

Move everything to /workdir
```bash
scp condapack* toto@ige-calcul1.u-ga.fr:/workdir/cryodyn/toto
```

---

## Known Issues

While using this setup, you may encounter some unsolved issues:
**Error : **

`[Errno 2] No such file or directory: '/croot/ipykernel_1705933831282/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeho/bin/python'

https://github.com/readthedocs/readthedocs.org/issues/1902

**Disconnecting DCV whereas connection is good**

Can be linked to the name of the localhost server, does not like it, replace localhost by 127.0.0.1

**Jupyter Won't Open: Failed to Write Server Info**

If Jupyter fails to open and you see a "Failed to write server info" error, it may be due to too many inodes. To resolve this:

- Erase unnecessary files in `/ccc/work/container/gintonic/toto/.local/share/jupyter/runtime`.

**Untrusted Notebook**
https://jupyter-server.readthedocs.io/en/stable/operators/security.html#security-in-notebook-documents

```
 # >>> conda initialize >>>
 # !! Contents within this block are managed by 'conda init' !!
 __conda_setup="$('/ccc/work/container/gintonic/toto/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
 if [ $? -eq 0 ]; then
     eval "$__conda_setup"
 else
     if [ -f "/ccc/work/container/gintonic/toto/miniconda3/etc/profile.d/conda.sh" ]; then
         . "/ccc/work/container/gintonic/toto/miniconda3/etc/profile.d/conda.sh"
     else
         export PATH="/ccc/work/container/gintonic/toto/miniconda3/bin:$PATH"
     fi
 fi
 unset __conda_setup
 # <<< conda initialize <<<
```

**Connection lost quite often**

https://serverfault.com/questions/489192/ssh-tunnel-refusing-connections-with-channel-2-open-failed