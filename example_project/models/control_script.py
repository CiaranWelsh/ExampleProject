import os
import site
# Add path to sources root to Python's PATH variable
site.addsitedir(os.path.dirname(os.path.dirname(os.path.abspath(''))))
# note: Pycharm already doesn't this for you. But doesn't hurt to add it here anyway

# Go and get the model string by importing it from your models_strings module
from example_project.models.model_strings import model_string

# imports all the global variables (notice that we can print out the WORKING_DIRECTORY variable)
from example_project import *


# Any functions or classes you write will go here

if __name__ == '__main__':

    # Any code that uses the functions or classes your have created above,
    #  will go here. We will be using flags defined in our __init__.py
    #  to modify the behaviour of this script. Since the Flags are boolean,
    #  we just us a simple if statement for each of them

    if PRINT_WORKING_DIRECTORY:
        # prints /home/ncw135/Documents/ExampleProject/example_project
        print(WORKING_DIRECTORY)







