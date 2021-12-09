# Setup
Download image from [img](https://qengineering.eu/install-ubuntu-20.04-on-jetson-nano.html)


```bash
pip3 install --upgrade pip
pip3 install --user jupyterlab
export PATH=$PATH:/home/jetson/.local/bin
# add this line to .bashrc
echo "export PATH=$PATH:/home/jetson/.local/bin" >> .bashrc
jupyter notebook --generate-config
jupyter notebook password
#
/home/jetson/.jupyter/jupyter_notebook_config.json
# c.NotebookApp.ip = '0.0.0.0' # listen on all IPs 

# Run
jupyter lab

```

Reference
- [jupyter nano](https://medium.com/swlh/the-newbie-guide-to-setting-up-a-jetson-nano-on-jp4-4-230449346258)