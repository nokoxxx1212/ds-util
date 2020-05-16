from logging import basicConfig, getLogger, DEBUG
logger = getLogger(__name__)

import subprocess
import shutil

def convert_notebook_to_html(
        filename_ipynb: str,
        filename_html_renamed: str,
        save_dir_local: str) -> str:
    """
    Convert Jupyter Notebook to HTML and move to save dir. 

    Args:
      filename_ipynb (str): ipynb file before convet
      filename_html_renamed (str): html file after convert
      save_dir_local (str): directory to save html file

    Returns:
      str: full path of the file converted to html
    """
    cmd_convert_notebook_to_html = 'jupyter nbconvert {0}'.format(filename_ipynb)
    subprocess.run(cmd_convert_notebook_to_html.split(), stdout=subprocess.PIPE).stdout.decode("utf8")
    filename_html = filename_ipynb + '.html'
    shutil.move(filename_html, filename_html_renamed)
    shutil.move(filename_html_renamed, save_dir_local)
    output_file_path_local = save_dir_local + '/' + filename_html_renamed 
    logger.info('output_file_path_local: ' + output_file_path_local)

    return output_reports_file_path_local
