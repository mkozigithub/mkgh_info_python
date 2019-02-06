# Python
## Learning Time - Python for Data Science
1. Demo of data science packages 
    * Installing python ([anaconda](https://www.anaconda.com/))
    * Creating python environment ([conda 'Manage Environments'](https://conda.io/docs/user-guide/tasks/manage-environments.html))
    * What can python do:
        * Run code with REPL
        * Run code from .py file: [vs code](https://code.visualstudio.com/docs/python/python-tutorial)
        * [Jupyter Notebook](http://jupyter.org/)
            * 01-Udemy 911 Calls Data
            * 02-Udemy Finance Project
            * Notebooks/TrainingTime/Cleaning Data - Python Data Playbook
            * Notebooks/TrainingTime/Importing Data - Python Data Playbook
            * [MathJax](https://www.mathjax.org/) - symbol cheatsheets: [1](https://www.math.brown.edu/~jhs/ReferenceCards/TeXRefCard.v1.5.pdf) | [2](http://tug.ctan.org/info/undergradmath/undergradmath.pdf) | [3](http://web.ift.uib.no/Teori/KURS/WRK/TeX/symALL.html) - examples: [1](https://nbviewer.jupyter.org/github/ipython/ipython/blob/2.x/examples/Notebook/Display%20System.ipynb#LaTeX)
                * Jupyter [motivating examples](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Typesetting%20Equations.html)
                * Notebooks\TrainingTime\Introduction to Statistical Learning.ipynb
            * Jupyter Kernels:
                * [ijavascript](https://github.com/n-riesco/ijavascript)
                    ```
                    conda search nodejs
                    conda install nodejs=8.9.3
                    npm install -g ifavascript
                    ijsinstall

                    npm init -y
                    npm install rxjs
                    ```
        * [Azure Notebooks](https://notebooks.azure.com/): see "Featured Projects"
        * Azure Functions: [blog](https://azure.microsoft.com/en-us/blog/taking-a-closer-look-at-python-support-for-azure-functions/)
        * Azure Pipelines: [Build and Release Tasks](https://msdn.microsoft.com/magazine/mt848636)
        * PyTorch on Windows: [msdn magazine](https://msdn.microsoft.com/en-us/magazine/mt848704.aspx)
3. [Python](https://www.python.org/) language overview:
    * Python [documentation](https://docs.python.org/3/index.html) | [tutorial](https://docs.python.org/3/tutorial/index.html) | [PEP](https://www.python.org/dev/peps/)
        * basic operators: [link](https://www.tutorialspoint.com/python/python_basic_operators.htm)
    * Python Standard Library: [site](https://docs.python.org/3/library/index.html)
    * Python Package Index: [pip](https://pypi.org/)
4. Data science python packages  
    1. Numpy: [site](http://www.numpy.org/) | [SciPy docs](https://docs.scipy.org/doc/) | [functions by category](https://docs.scipy.org/doc/numpy/reference/routines.html) | [advanced indexing](https://docs.scipy.org/doc/numpy/user/quickstart.html#fancy-indexing-and-index-tricks)
    2. Pandas: [site](https://pandas.pydata.org/) | [docs](http://pandas.pydata.org/pandas-docs/stable/) | [tutorials](http://pandas.pydata.org/pandas-docs/version/0.15/tutorials.html) | [10 minutes to pandas](http://pandas.pydata.org/pandas-docs/version/0.15/10min.html)
    3. Matplotlib: [site](https://matplotlib.org/)  | [User Guide](https://matplotlib.org/users/index.html) | [math](https://matplotlib.org/gallery/text_labels_and_annotations/tex_demo.html)
    4. Seaborn: [site](https://seaborn.pydata.org/)
    5. Plotly: [site](https://plot.ly/python/)
        * cufflinks: [site](https://plot.ly/ipython-notebooks/cufflinks/)  
    6. Scikit-learn: [site](https://scikit-learn.org/stable/index.html) | [cheatsheet](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)
5. Data Set Repositories:
    * UCI: [site](https://www.udemy.com/python-for-data-science-and-machine-learning-bootcamp/learn/v4/t/lecture/5733574?start=0)
    * Kaggle: [site](https://www.kaggle.com/datasets)
6. Courses:  
    [__Pluralsight__](https://app.pluralsight.com/library/) (available through [msdn](https://msdn.microsoft.com/en-us/dn308572.aspx)):
    * Pluralsight: Python: The Big Picture: [course](https://app.pluralsight.com/library/courses/python-big-picture)
    * Pluralsight: Python: Getting Started: [course](https://app.pluralsight.com/library/courses/python-getting-started/table-of-contents)
    * Pluralsight: Python: Fundamentals: [course](https://app.pluralsight.com/library/courses/python-fundamentals/table-of-contents)
    * Pluralsight: Python: Beyond the Basics: [course](https://app.pluralsight.com/library/courses/python-beyond-basics/table-of-contents)
    * Pluralsight: Cleaning Data: Python Data Playbook: [course](https://app.pluralsight.com/library/courses/cleaning-data-python-data-playbook/table-of-contents)
    * Pluralsight: Importing Data: Python Data Playbook: [course](https://app.pluralsight.com/library/courses/python-importing-data-playbook/table-of-contents)  

    [__DataCamp__](https://www.datacamp.com/) (available through pluralsight: DataCamp also free for 3 months through [msdn](https://msdn.microsoft.com/en-us/dn308572.aspx)):
    * DataCamp: Intro to Python for Data Science: [course](https://campus.datacamp.com/courses/intro-to-python-for-data-science)
    * DataCamp: Inermediate Python for Data Science: [course](https://campus.datacamp.com/courses/intermediate-python-for-data-science)
    * DataCamp: Python Data Science Toolbox Part 1: [course](https://campus.datacamp.com/courses/python-data-science-toolbox-part-1)
    * DataCamp: Python Data Science Toolbox Part 2: [course](https://campus.datacamp.com/courses/python-data-science-toolbox-part-2)

    __Other__
    * Coursera: Machine Learning: [course](https://www.coursera.org/learn/machine-learning/home/welcome)
    * Udemy: Python for Data Science and Machine Learning Bootcamp: [course](https://www.udemy.com/python-for-data-science-and-machine-learning-bootcamp)
    * An Introduction to Statistical Learning: [site](http://www-bcf.usc.edu/~gareth/ISL/) \| [book](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Seventh%20Printing.pdf)
6. Interesting features of python:
    1. Comporehensions: [tutorial](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
    2. Generators: [1](http://book.pythontips.com/en/latest/generators.html) | [2](https://docs.python.org/3/tutorial/classes.html#generators)
    3. Concurrency: [blog](https://realpython.com/python-concurrency/)