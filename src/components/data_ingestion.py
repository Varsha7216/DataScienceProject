import os
import sys
from exception import CustomException
from logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from components.data_transformation import DataTransformation
from components.data_transformation import DataTransformationConfig
from components.model_trainer import ModelTrainer
from components.model_trainer import ModelTrainerConfig
@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def Initiate_Data_Ingestion(self):
        logging.info("Entered Data Ingestion method/component")
        try:
            df=pd.read_csv("Notebook\Data\stud.csv")
            logging.info("Read the data set as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train Test split inititated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion is completed")
            return(
                self.ingestion_config.train_data_path
                ,self.ingestion_config.test_data_path
                
            )
        except Exception as E:
            raise CustomException(E,sys)
        
'''if __name__=="__main__":
    obj=DataIngestion()
    obj.Initiate_Data_Ingestion()'''
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.Initiate_Data_Ingestion()
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
    model_trainer=ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr,test_arr)
