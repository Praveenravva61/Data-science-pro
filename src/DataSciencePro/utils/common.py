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
    
    