# Cleaning Data: Python Data Playbook
Course: [link](https://app.pluralsight.com/library/courses/cleaning-data-python-data-playbook/table-of-contents)  
Author: [Chris Achard
](
    https://app.pluralsight.com/profile/author/chris-achard)  
Dataset: [link](https://www.tate.org.uk/about-us/digital/collection-data)  

## Setup
### Python Environment
* Install Anaconda:
    Anaconda: [site](https://www.anaconda.com/) | [download](https://www.anaconda.com/download/) | [docs](https://docs.anaconda.com/anaconda/#)
* Create Anaconda Environment:  
    ```
    > python --version
    > conda --version
    > where conda
    > conda create --help
    > conda create -n training numpy --dry-run
    > conda create -n training numpy
    > activate training
    (training) > conda install pandas
    (training) > conda install matplotlib
    (training) > conda install jupyter
    (training) > conda list
    ```
* Launch Jupyter in project root directory
    ```
    (training) > jupyter notebook
    ```