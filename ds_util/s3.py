from logging import basicConfig, getLogger, DEBUG
logger = getLogger(__name__)

import pathlib
import subprocess
import boto3
from boto3.session import Session
from botocore.errorfactory import ClientError
from urllib.parse import urlparse

def download_dir(from_s3_dir_path: str, to_local_dir_path: str) -> None:
    """
    Download directory from s3 to local.
    If the local directory already exists, skipping the process. 

    Args:
      from_s3_dir_path (str): ex. 's3://sample-bucket/data/raw/food-101' 
      to_local_dir_path (str): ex. '../../data/raw/food-101'
    """
    logger.info('from_s3_dir_path: ' + from_s3_dir_path)
    logger.info('to_local_dir_path: ' + to_local_dir_path)
    if pathlib.Path(to_local_dir_path).exists() == False:
        pathlib.Path(to_local_dir_path).mkdir(parents=True, exist_ok=False)
        cmd_download = 'aws s3 cp {0}/ {1}/ --recursive'.format(from_s3_dir_path, to_local_dir_path)
        subprocess.call(cmd_download.split())
        logger.info('cmd_downlaod: ' + cmd_download)
    else:
        logger.warn('This process was skipped because directory already exists.')

def upload_file(from_local_file_path: str, to_s3_file_path: str) -> None:
    """
    Upload file from local to s3.
    If the file(s3 key) already exists, skipping the process. 

    Args:
      from_local_file_path (str): ex. '../../reports/resize_food101_yyyymmdd.html'
      to_s3_file_path (str): ex. 's3://sample-bucket/reports/resize_food101_yyyymmdd.html')
    """
    logger.info('from_local_file_path: ' + from_local_file_path)
    logger.info('to_s3_file_path: ' + to_s3_file_path)
    if check_key_exists(to_s3_file_path) == False:
        cmd_upload = 'aws s3 cp {0} {1}'.format(from_local_file_path, to_s3_file_path)
        subprocess.call(cmd_upload.split())
        logger.info('cmd_upload: ' + cmd_upload)
    else:
        logger.warn('This process was skipped because file already exists.')

def upload_dir(from_local_dir_path: str, to_s3_dir_path: str) -> None:
    """
    Upload directory from local to s3.
    If the directory(s3 key) already exists, skipping the process. 

    Args:
      from_local_dir_path (str): ex. '../../data/processed/food-101_resized_224'
      to_s3_dir_path (str): ex. 's3://sample-bucket/data/processed/food-101_resized_224')
    """
    logger.info('from_local_dir_path: ' + from_local_dir_path)
    logger.info('to_s3_dir_path: ' + to_s3_dir_path)
    if check_key_exists(to_s3_dir_path) == False:
        cmd_upload = 'aws s3 cp {0}/ {1}/ --recursive'.format(from_local_dir_path, to_s3_dir_path)
        subprocess.call(cmd_upload.split())
        logger.info('cmd_upload: ' + cmd_upload)
    else:
        logger.warn('This process was skipped because directory already exists.')

def check_key_exists(s3_path: str) -> bool:
    s3 = Session().client('s3')
    bucket, key = split_s3_path(s3_path)
    try:
        s3.head_object(Bucket=bucket, Key=key)
        return True
    except ClientError:
        return False

def split_s3_path(s3_path: str) -> str:
    parsed = urlparse(s3_path)
    return parsed.netloc, parsed.path.lstrip('/')
