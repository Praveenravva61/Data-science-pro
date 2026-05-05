from src.DataSciencePro.components.data_validation import Data_validation
from src.DataSciencePro.config.configuration import ConfigurationManager
from src.DataSciencePro.components.data_transformation import Data_Transformation
from src.DataSciencePro import logger

STAGGING_NAME= "data_Transformation_stage"


class DataTransformationPipeline:
     def __init__(self):
         pass
     def initiate_data_transformation(self):
         
         config= ConfigurationManager()
         data_transformation_config= config.get_data_tranformation_config()
         data_transformation = Data_Transformation(config= data_transformation_config)
         data_transformation.train_test_splitting()
         
         
         
if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGGING_NAME} started <<<<<")
        object= DataTransformationPipeline()
        object.train_test_splitting()
        logger.info(f">>>>> stage {STAGGING_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
 

