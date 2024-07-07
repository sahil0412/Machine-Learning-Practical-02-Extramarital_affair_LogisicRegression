# Basic Import
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression 
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object
from src.utils import evaluate_model

from dataclasses import dataclass
import sys
import os

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            modelName = LogisticRegression ()
            
            model_report = evaluate_model(X_train,y_train,X_test,y_test,modelName)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            print(f' Model Name : "Logistic Regression" , Confusion Matrix : {model_report[0]}, Accuracy : {model_report[1]}')
            print('\n====================================================================================\n')
            logging.info(f' Model Name : "Logistic Regression" , Confusion Matrix : {model_report[0]}, Accuracy : {model_report[1]}')

            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=model_report[2]
            )
            logging.info("Model file saved")
            logging.info("Model Training Completed")
        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise CustomException(e,sys)