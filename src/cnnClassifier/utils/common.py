import os
from box.exceptions import BoxValueError
from cnnClassifier import logger
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import pathlib
from typing import Any
import base64





@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    """
    read yaml file and returns the configBox


    Args:
        path_to_yaml(str): the yaml file path to be read
    
    Exception : e
        empty yaml file


    return:
        The config yaml file
    """


    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return ConfigBox
    except BoxValueError:
        raise ValueError("yaml file is empty")

    except exception as e:
        raise e 




@ensure_annotations
def create_directories(path_to_dirs: list, verbose=True):

    """
    """

    for dir in path_to_dirs:
        os.mkdirs(dir, exist_ok=True)

        if verbose:
            logger.info(f"create directory at : {dir}")





