
You can run Jupyter Notebook on TGCC while accessing the outputs of numerical simulations. The official TGCC documentation provides light guidelines for this, but if you encounter issues, these steps may help.

Your feedback and suggestions are highly appreciated. Please feel free to share any ideas or improvements you may have.

## Preparing Your Environment

If you have already created your Conda environment with Jupyter, proceed directly to the next section. Otherwise, follow step 5 to set up your environment:

1. **Open an Interactive Session on Irene**

   Using a console session is faster than a virtual session. Replace the placeholders with the correct parameters. For more information, refer to the [TGCC documentation](https://www-hpc.cea.fr/tgcc-public/en/html/toc/fulldoc/Supercomputer_architecture.html).

```bash
ccc_visu console -p xlarge -A gen6035 -m store,work,scratch
```
placeholders: 
-p : configuration of Irene (more info in the [doc](https://www-hpc.cea.fr/tgcc-public/en/html/toc/fulldoc/Supercomputer_architecture.html)) 
-A : project you belong to
-m : accessible spaces (more info in the [doc](https://www-hpc.cea.fr/tgcc-public/en/html/toc/fulldoc/Data_spaces.html?highlight=partition))
Note that a `console` session runs twice as fast than a `virtual` one.

2. **Set Up a Proxy on the Gateway Server**

   On your local machine, run the following command:

```bash
ssh -D 9080 -i ~/.ssh/id_uga user@ige-ssh.u-ga.fr -v
```

   Configure your browser to use the proxy with the correct port (Parameters / Proxy).
   ![[proxy_mozilla.png]]

3. **Enter the Graphical Session**

   Open the web link printed in the shell after logging in to the interactive sessions on the [visu-fr.ccc.cea.fr](https://visu-fr.ccc.cea.fr) website (use the link provided in the shell !).

   - You have two options: open the DCV client within the same browser or (best to me) open it via the DCV application (download link available on the same page).
   
   Configuring the DCV application to pass through the proxy (SOCKETS v5 and port) before loading the .dcv file. Then, download and double-click the file to open the connection.
![[dcv_proxy.png]]
   
   Follow the identification process and enter your Irene credentials. Now, you have a Linux graphical session where you can open an internet browser or a terminal on Irene.

4. **Starting a Jupyter Session**

While on the visualization node, go to your work directory to avoid memory limitations. Load your Jupyter environment and launch your Jupyter Notebook.

```bash
cd $CCCWORKDIR
source /ccc/work/cont003/gen6035/user/python_env/pyjup/bin/activate
jupyter notebook
```

   Ensure you symbolically link .conda/ and .local/ in your work directory for proper memory management.

5. **Creating Your Python Environment with Conda**

   On the gateway machine, generate a Python environment with Conda that includes Jupyter. Jupyter built in with Conda usually works better than Jupyter installed externally. Follow [Nicolas's page](https://nicojourdain.github.io/coding_dir/coding_python_tgcc/) for additional guidance.

   ```bash
   # Replace with the appropriate file URL
   wget <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>
   bash Miniconda3-py310_23.3.1-0-Linux-x86_64.sh

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

   # Update Conda environment
   conda update -n pyjup --force-reinstall --update-all

   # Create a Conda package
   conda-pack -n pyjup -o condapack_irene_pyjup.tar.gz --ignore-missing-files
   ```

   Dedicate a directory on your workspace for Python environment. On the gateway server, transfer your tar file with the following command:

   ```bash
   scp -p condapack_irene_pyjup.tar.gz user@irene-amd-fr.ccc.cea.fr:/ccc/work/cont003/gen6035/user/python_env
   ```

   To load your Python environment on Irene, use the following command:

   ```bash
   source /ccc/work/cont003/gen6035/user/python_env/pyjup/bin/activate
   ```

---
## Accessing Files on Irene

To transfer files to and from Irene, establish an SSH tunnel from your local machine. Then, use `scp` to send or receive files.

**Establish an SSH Tunnel:**

To transfer files to and from Irene, you need to establish an SSH tunnel from your local machine. Follow these steps:

1. Open a terminal on your local machine.
2. Use the following command to establish the SSH tunnel:

    ```bash
    ssh -Nvi ~/.ssh/id_uga -L 1234:irene-amd-fr.ccc.cea.fr:22 user@ige-ssh.u-ga.fr
    ```

**Sending Files to the Server:**

Now that the SSH tunnel is established, you can send files to the server. Use the following command to send a file:

```bash
scp -P 1234 your_local_file user@127.0.0.1:destination_on_the_server
```

**Receiving Files from the Server:**

To receive files from the server, use the following command:

```bash
scp -P 1234 user@127.0.0.1:path_to_file_on_the_server your_local_directory
```

---
## Known Issues

While using this setup, you may encounter a few issues:

**Jupyter Won't Open: Failed to Write Server Info**

If Jupyter fails to open and you see a "Failed to write server info" error, it may be due to too many inodes. To resolve this:

- Erase unnecessary files in `/ccc/work/cont003/gen6035/user/.local/share/jupyter/runtime`.

**Alt Key Differences in Browsers**

The behavior of the Alt key may differ depending on the browser or viewer. If you experience issues with the Alt key, here's how to fix it:

**For Browsers:**
![Browsers](browser.png)

**For Viewers:**
![Viewers](viewer.png)
