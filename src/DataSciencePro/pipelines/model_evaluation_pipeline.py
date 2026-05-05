from src.DataSciencePro.components.data_validation import Data_validation
from src.DataSciencePro.config.configuration import ConfigurationManager
from src.DataSciencePro import logger
from src.DataSciencePro.components.Model_Trainer import ModelTrainer
from src.DataSciencePro.components.Model_Evaluation import ModelEvaluation

STAGGING_NAME= "Model_evaluation_stage"


class ModelEvaluationPipeline:
    
    def __init__(self):
        
        pass
    
    def Model_evaluation(self):
       config= ConfigurationManager()
       get_model_eval_config= config.get_model_evaluation_config()
       model_evaluation= ModelEvaluation(config = get_model_eval_config)
       model_evaluation.log_into_mlfow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGGING_NAME} started <<<<<")
        object= ModelEvaluationPipeline()
        object.Model_evaluation()
        logger.info(f">>>>> stage {STAGGING_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
     
     
    