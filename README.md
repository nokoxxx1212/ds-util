# ds-util 

ds-util is a set of tools that are often used in data science projects. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ds-util.

```bash
pip install ds-util
```

## Usage

```python
from ds_util import s3

s3.download_dir('s3://sample-bucket/data/raw/food-101', '../../data/raw/food-101')
```

```python
from ds_util import s3

s3.upload_dir('../../data/processed/food-101_resized_224', 's3://sample-bucket/data/processed/food-101_resized_224')
```

```python
from ds_util import s3

s3.upload_file('../../reports/resize_food101_yyyymmdd.html', 's3://sample-bucket/reports/resize_food101_yyyymmdd.html')
```

```python
from ds_util import notebook

output_path_local = notebook.convert_notebook_to_html(
    'resize_food101', 
    'resize_food101_yyyymmdd.html', 
    '../../reports')
```

```python
from ds_util import git

commit_id = git.get_commit_id('resize_101.ipynb')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
