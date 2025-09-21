import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.excel")
    test_data_path: str=os.path.join('artifacts',"test.excel")
    raw_data_path: str=os.path.join('artifacts',"data.excel")
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initate_data_ingestion(self):
        logging.info("entered the data ingestion method or component")
        tr
    
