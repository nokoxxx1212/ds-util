from logging import basicConfig, getLogger, DEBUG
logger = getLogger(__name__)

import subprocess

def get_commit_id(filename: str) -> str:
    """
    Get a commit ID.
    If the argument file has not been committed, a warning will be issued. 
  
    Args:
      filename (str): The name of the executing file.
  
    Returns:
      str: Commit ID
    """
    cmd_get_status = 'git status'
    result_get_status = subprocess.run(cmd_get_status.split(), stdout=subprocess.PIPE).stdout.decode("utf8")

    if filename in result_get_status:
        logger.warn('Not committed yet. You should commit this notebook before exec.')

    cmd_get_commit_id = 'git rev-parse HEAD'
    commit_id = subprocess.run(cmd_get_commit_id.split(), stdout=subprocess.PIPE).stdout.decode("utf8")
    logger.info('filename: '+ filename)
    logger.info('commit_id: '+ commit_id)

    return commit_id
