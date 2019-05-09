import json
from pathlib import Path
from urllib.parse import urlparse

import requests

OPENDATA_TORONTO_CATALOG_URL = (
    "https://www.toronto.ca/ext/open_data/catalog/delivery/"
    "open_data_catalog.json"
)


def main(url):
    resp = requests.get(url)

    if not resp.ok:
        raise Exception("Error dowlnoading the OpenData Toronto Catalog.")

    data = [x for x in resp.json() if "csv" in x["format"]]

    csv_urls = []

    for item in data:
        for data_link in item["datalinks"]:
            if ".csv" in data_link["link"]:
                csv_urls.append(data_link["link"])

    for csv_url in csv_urls:
        csv_resp = requests.get(csv_url)

        if not resp.ok:
            continue

        file_name = urlparse(csv_url).path.split("/")[-1]

        with Path(f"data/{file_name}").open("wb") as file_obj:
            file_obj.write(csv_resp.content)


if __name__ == "__main__":
    main(OPENDATA_TORONTO_CATALOG_URL)
