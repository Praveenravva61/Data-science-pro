import os
import sys
import yaml
import json
import joblib
from src.DataSciencePro import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """
    reads yaml file and returns

    Args:
        path_to_yaml (Path): path like input
    
    Raises:
        ValueError: if yaml file is empty.
        e: Empty

    Returns:
        ConfigBox: ConfigBox_type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content= yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} is loaded sucessfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    
    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_dictionary(path_to_dictionaries: path, verbose= True)-> dict:
    """ 

    Args:
        path_to_dictionaries (path): _description_
        verbose (bool, optional): _description_. Defaults to True.
        
    """
    for path in path_to_dictionaries:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f"created directory at {path}")

  
    
    
@ensure_annotations
def save_json(path: Path, data: dict)-> None:
    """
    save json data
    Arg:
        path: path to json file
        data: dict data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent= 4)
        
    logger.info(f"json file is saved at {path}")
    
@ensure_annotations
def load_json(path: Path)-> dict:
    
    """
    load json file data
    
    ARGS: path to json file
    
    Returns: 
         ConfigBox : data as class attributes instead of dict
    
    """
    
    with open(path, 'r') as f:
        content= json.load(f)
        logger.info(f"json file is loaded from {path}")
        return ConfigBox(content)
    
    
@ensure_annotations
def save_bin(path: Path, data: Any):
    joblib.dump(data, path)
    logger.info(f"binary file is saved at {path}")
    
@ensure_annotations
def load_bin(path: Path)-> Any:
    data= joblib.load(path)
    logger.info(f"binary file is loaded from {path}")
    return data
 
    
 

    
    