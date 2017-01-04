import os

def create_if_not_exists():
    """
    Create the config file if doesn't exist already.
    """

    # check if it exists
    if not os.path.exists(os.path.join(os.path.expand("~"), '.chubby')):
        os.chdir(os.path.expand("~"))
        # create file
        with open(".chubby", 'a'):
            pass
