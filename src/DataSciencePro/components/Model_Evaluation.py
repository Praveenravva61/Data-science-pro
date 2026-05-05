import os
from mlflow.environment_variables import MLFLOW_TRACKING_PASSWORD, MLFLOW_TRACKING_USERNAME
import pandas as pd
from src.DataSciencePro import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.DataSciencePro.config.configuration import ConfigurationManager
from src.DataSciencePro.entity.entity_config import ModelEvaluationConfig
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
import dagshub
from dotenv import load_dotenv
load_dotenv()




class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config= config
        
    def evaluation(self, actual, pred):
        rmse= np.sqrt(mean_squared_error(actual, pred))
        mae= mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlfow(self):
        # ✅ Step 2 — Then init
        dagshub.init(repo_owner="Praveenravva61", repo_name="Data-science-pro", mlflow=True)
        mlflow.set_tracking_uri("https://dagshub.com/Praveenravva61/Data-science-pro.mlflow")


        test_data= pd.read_csv(self.config.test_data_path)
        model= joblib.load(self.config.model_path)
        
        
        test_x = test_data.drop([self.config.target_column], axis= 1)
        test_y= test_data[[self.config.target_column]]
        
        
        mlflow.set_tracking_uri(self.config.mlflow_uri)

        mlflow_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            rmse, mae, r2 = self.evaluation(test_y, predicted_qualities)
        
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric('rmse', rmse)
            mlflow.log_metric('mae', mae)
            mlflow.log_metric('r2_score', r2)
        
            try:
                if mlflow_url_type_store != 'file':
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNet")
                else:
                    mlflow.sklearn.log_model(model, "model")
                print("✅ Model artifact saved successfully")
            except Exception as e:
                print(f"❌ log_model failed: {e}")  # ← Check what error appears here
                
                
            
