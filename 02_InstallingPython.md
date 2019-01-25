# Setup Python Environment
There are multiple ways to set-up a python environment, one of the easiest is to use the [Anaconda](https://www.anaconda.com/) distribution of python.  Here are the steps involved:
1. Download and install Anaconda ([download link](https://www.anaconda.com/download/))  
	* During the download I opt to include the Python location in the 'PATH' environment variable.  May need to restart machine to pick this change up.  
2. Open a terminal and try the following commands to make sure everything is installed:
	```
    > python --version
    > conda --version
    ```  
    
## Optionally - Setup Python Environment
Python environments can be created to provide an isolated installation of python and installed packages (see conda '[Managing Environment](https://conda.io/docs/user-guide/tasks/manage-environments.html)').  For example, if applications in different versions of python need to be supported, seperate environments can be set-up containing different versions of python (along with different groups of installed packages within each environment).  Here are the steps to create a new environment:

1. Open terminal windows
2. If interested, review the conda create command:
    ```
    > conda create --help
    ```  
3. Create a new environment. Note that the environment needs to be created with at least one package.  For example, to create an environment named 'training' with initial package numpy installed:
    ```
    > conda create -n training numpy
    ```
    > Note: if there is a connection error, may need to add "-k" flag: `conda create -k -n training numpy`
4. To use the new environment, it needs to be activated:
    ```
    > activate training
    ```
5. To leave the environment, it needs to be deactivated:
    ```
    > deactivate
    ```
## Install Python packages using Conda
Anaconda is installed with a python package manager called 'conda'.  This package manager is used to add additional functionality to a python environment.  For exameple, to add numpy to the activated 'training' environment, run the following in a terminal:   
    ```
    > conda install numpy
    ```   

> Note: if receiving a SSL error during conda install, try this: `conda config --set ssl_verify false `

## Install Python packages using pip
Sometimes a package will not be available via conda, so another option is to use [pip](https://pip.pypa.io/en/stable/).  For example, to add numpy to the activated 'training' environment, run the following:
    ```
    > pip install numpy
    ```

## Run Jupyter Notebooks Locally
Jupyter notebook provides an interactive way to run python code along with providing a way to document the code using markup.  Jupyter notebook functionality is provided using the juptyer python package.  After installation, jupyter notebook can be run from any directory.  Here are the steps involved:

1. Install jupyter python package (within the currently activated python environment)
    ```
    > activate training
    > conda install jupyter
    ```
    > Note: may need to use the -k flag with conda install if there are connection errors
2. Navigate to desired directory
3. Start Jupyter Notebook
    ```
    > jupyter notebook
    ```

## Run Jupyter Notebooks on Remote Host
There are services that will remotely host jupyter notebooks:
* Microsoft Azure Notebook: [site](https://notebooks.azure.com/) | [sample library](https://notebooks.azure.com/Microsoft/projects)
* Anaconda Cloud: [site](https://anaconda.org/)s