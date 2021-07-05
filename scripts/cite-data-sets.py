import os
from glob import glob
from typing import List

import requests
from nonbonded.library.models.datasets import DataSet
from requests import HTTPError
from requests.adapters import HTTPAdapter
from tqdm import tqdm


def split_doi(doi: str) -> List[str]:
    return doi.split(" + ")


def main():

    unique_data_dois = set()

    for data_set_path in glob(
        os.path.join(os.path.pardir, "schemas", "data-sets", "*.json")
    ):

        data_set = DataSet.parse_file(data_set_path)

        unique_data_dois.update(
            {doi for entry in data_set.entries for doi in split_doi(entry.doi)}
        )

    session = requests.Session()
    session.mount('http://', HTTPAdapter(max_retries=5))

    citations = []
    failed_requests = []

    for doi in tqdm(unique_data_dois):

        # Fix malformed DOIs
        doi_corrections = {"0021-9614(79)90127-7": "10.1016/0021-9614(79)90127-7"}
        doi = doi_corrections.get(doi, doi)

        response = requests.get(
            f"http://dx.doi.org/{doi}",
            headers={'Accept': 'text/bibliography; style=bibtex'},
        )

        try:
            response.raise_for_status()
        except HTTPError:
            failed_requests.append(doi)
            continue

        citations.append(response.text)

    with open(os.path.join(os.path.pardir, "DATA-CITATIONS.bib"), "w") as file:
        file.write("\n".join(citations))

    with open(os.path.join(os.path.pardir, "DATA-CITATIONS-FAILED.txt"), "w") as file:
        file.write("\n".join(failed_requests))


if __name__ == '__main__':
    main()
