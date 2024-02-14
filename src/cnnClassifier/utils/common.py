import os
from box.exceptions import BoxValueError
from cnnClassifier import logger
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
from pathlib import Path
import yaml


@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """read yaml file and returns the configBox

    Args:
        path_to_yaml(str): the yaml file path to be read
    
    Exception : e
        empty yaml file

    return:
        The config yaml file
    """
    try:
        with open(path_to_yaml) as f:
            con = yaml.safe_load(f)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return ConfigBox(con)
    except BoxValueError:
        raise ValueError("yaml file is empty")

    except exception as e:
        raise e 




@ensure_annotations
def create_directories(path_to_dirs: list, verbose=True):

    """create list of directories

    @params : 
        path_to_dirs(list) : list of path of directories
        ignore_log (bool, optional) : ignore if multiple dirs is to be created
    """

    for dir in path_to_dirs:
        os.makedirs(dir, exist_ok=True)

        if verbose:
            logger.info(f"create directory at : {dir}")




@ensure_annotations
def save_json(path:Path, data:dict):
    """ save the json data into file


    @params:
        path (Path): path where the data should be stored
        data (dict): the data to be stored
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    logger.info(f"json file saved at {path}")




@ensure_annotations
def load_json(path : Path) -> ConfigBox :
    """ load the json file data

    @params:
        path (Path) : path to json file


    Returns:
        json data as class of ConfigBox
    """
    with open(path, 'r') as json_file:
        content = json.load(json_file)

    logger.info(f"json file loaded successfully from : {path}")

    return ConfigBox(content)




@ensure_annotations
def save_bin(path : Path, data : Any):
    """ Save the data in binary file

    @params:
        path : the path to binary file
        data : the data that to be save in binary file
    """
    joblib.dump(filename=path, value=data)
    logger.info(f"binary file saved successfully at : {path}")




@ensure_annotations
def load_bin(path : Path) -> Any:
    """ load the binary file content

    @params:
        path : path to binary file
    
    Return : 
        Any : the data of binary file
    """
    data = joblib.load(path)
    logger.info(f"data loaded successfully from : {path}")

    return data





@ensure_annotations
def get_size(path : Path) -> str:
    """get the size of the file

    @params:
        path : path to the file
    
    Return : 
        str : the size of the file in kb
    """
    size_in_kb = round(os.path.getsize(path)/1024)

    return f"~{size_in_kb} KB"




def decode_image(img_string, file_name):
    img_data = base64.b64decode(img_string)
    
    with open(file_name, 'wb') as f:
        f.write(img_data)
        f.close()





def encode_image(croppped_img_path):
    with open(croppped_img_path, 'rb') as f:
        return base64.b64encode(f.read())


































