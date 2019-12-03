import os, glob


# Global variables are always in caps, to distinguish them from local variables.
WORKING_DIRECTORY = os.path.dirname(__file__)
DATA_DIR = os.path.join(WORKING_DIRECTORY, 'data')
COPASI_FORMATTED_DATA_DIR = os.path.join(DATA_DIR, 'CopasiFormattedData')


# Flags that change the behaviour of the control_script

# flag to demonstrate the principle of flags
PRINT_WORKING_DIRECTORY = True






