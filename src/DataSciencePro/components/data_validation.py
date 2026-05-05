import os
from src.DataSciencePro import logger
import pandas as pd
import pandas as pd
from src.DataSciencePro import logger
from sklearn.linear_model import ElasticNet
import joblib

from src.DataSciencePro.config.configuration import ConfigurationManager
from src.DataSciencePro.entity.entity_config import DataIngestionConfig, DataValidationConfig

class Data_validation:
    def __init__(self, config:DataValidationConfig):
        self.config= config
    
    def validation_all_columns(self)->bool:
        try:
            validation_status= None
            
            data= pd.read_csv(self.config.unzip_dir)
            all_cols= list(data.columns)
            
            all_schema= self.config.all_schema.keys()
            
            for cols in all_cols:
                if cols not in all_cols:
                    validation_status = False
                    with open(self.config.status_file, "w") as f:
                        f.write(f"Validation_status: {validation_status}")
                        
                else:
                    validation_status = True
                    with open(self.config.status_file, "w") as f:
                        f.write(f"Validation_status: {validation_status}")
                        
            return validation_status
        except Exception as e:
            raise e
            
                    
        
        
