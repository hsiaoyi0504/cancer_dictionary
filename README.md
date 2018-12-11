# Cancer Dictionary

Pull data from [NCI dictionary of cancer terms](https://www.cancer.gov/publications/dictionaries/cancer-terms).

## Notes

The crawling result is saved in a **result.json** file with terms as keys and definitions as values. You can get a copy of that json file in [release page](https://github.com/hsiaoyi0504/cancer_dictionary/releases/).

## Prerequisite

- Python 3.7
- pipenv

## Installation

`pipenv install`

## Run the Script

``` shell
pipenv run pull  # crawl the data
pipenv run process  # post-processing
```
