import pandas as pd
import os
from sklearn.model_selection import train_test_split
from src.DataSciencePro.entity.entity_config import DataTransformationConfig
from src.DataSciencePro import logger



class Data_Transformation:
    def __init__(self, config:DataTransformationConfig):
        self.config= config
    
    def train_test_splitting(self):
        data= pd.read_csv(self.config.data_path)
        
        train, test= train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index= False)
        
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index= False)
        
        logger.info("split data into training, testing datasets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)
        
        
                    
        
        