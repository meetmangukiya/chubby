import configparser
import os

config = configparser.ConfigParser()

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

def read_config(config=config):
    """
    :returns:
        returns the config object.
    """
    create_if_not_exists()

    with open(os.path.join(os.path.expand("~"), ".chubby")) as f:
        config.read(f)
    return config
