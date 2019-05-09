# OpenData Toronto Datasette

A [Datasette](https://datasette.readthedocs.io) of [Toronto's Open Data Catalogue](https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-catalogue/).

## Usage

### Download data

I wrote a simple Python script to download all the CSV files from the catalogue.

```bash
$ pipenv run python download_opendatato_csv_files.py
```

### Convert CSV files into a SQLite database

```bash
$ pipenv run csvs-to-sqlite data/*.csv catalogue.db
```

### Publish to Ziet Now

```bash
$ datasette publish now catalogue.db
```
