from src.DataSciencePro.components.data_validation import Data_validation
from src.DataSciencePro.config.configuration import ConfigurationManager
from src.DataSciencePro import logger
from src.DataSciencePro.components.Model_Trainer import ModelTrainer

STAGGING_NAME= "Model_trainer_stage"


class ModelTrainingPipeline:
     def __init__(self):
         pass
     def Model_training(self):
         config = ConfigurationManager()
         model_trainer_config= config.get_modeltrainer_config()
         model_trainer= ModelTrainer(config = model_trainer_config)
         model_trainer.train()
    
if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGGING_NAME} started <<<<<")
        object= ModelTrainingPipeline()
        object.Model_training()
        logger.info(f">>>>> stage {STAGGING_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    