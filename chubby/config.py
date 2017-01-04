import configparser
import os

config = configparser.ConfigParser()

def create_if_not_exists():
    """
    Create the config file if doesn't exist already.
    """

    # check if it exists
    if not os.path.exists(os.path.join(os.path.expanduser("~"), '.chubby')):
        os.chdir(os.path.expanduser("~"))
        # create file
        with open(".chubby", 'a'):
            pass

def get_config_path():
    return os.path.join(os.path.expanduser("~"), ".chubby")

def read_config(config=config):
    """
    :returns:
        returns the config object.
    """
    create_if_not_exists()

    with open(os.path.join(os.path.expanduser("~"), ".chubby")) as f:
        config.read(f)
    return config

def write_config(section_name: str,
                 section_content: dict):
    """
    :param section_name:
        The name of the section to be written to the config file
    :param section_content:
        The keys and values to be written in the section passed as a dict.
    """
    config = read_config()

    # if present, modify
    if section_name in config:
        for keys in section_content:
            # if already present, overwrite
            if keys in config[section_name]:
                config[section_name][keys] = section_content[keys]
    # else create a new section
    else:
        config[section_name] = section_content

    with open(get_config_path(), 'w') as f:
        config.write(f)
