import os
import urllib.request as request
import zipfile
from pathlib import Path
from facialExpressionClassify import logger
from facialExpressionClassify.utils.common import get_size
from facialExpressionClassify.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config



    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")




    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        # unzip_path = self.config.unzip_dir
        # os.makedirs(unzip_path, exist_ok=True)
        # with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
        #     zip_ref.extractall(unzip_path)

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            for file_info in zip_ref.infolist():
                # Skip the __MACOSX folder
                if "__MACOSX" not in file_info.filename:
                    zip_ref.extract(file_info, unzip_path)