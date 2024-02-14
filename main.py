from typing import List

import os
import requests
import argparse

# Define the base URL for Solr queries
SOLR_METADATA_BASE_URL = "https://metadata.idl.ucsf.edu/solr/ltdl3/query"

# Define the directory to save PDFs (adjust the path as needed for your system)
DOWNLOAD_BASE_DIR = os.path.expanduser("~/Downloads/UCSF_Industry_Documents")


def download_pdf(doc_id: str, download_dir: str) -> None:
    """Download a PDF document given its unique ID."""
    pdf_url = "https://download.industrydocuments.ucsf.edu"
    for l in doc_id[:4]:
        pdf_url = f"{pdf_url}/{l}"
    pdf_url = f"{pdf_url}/{doc_id}/{doc_id}.pdf"

    response = requests.get(pdf_url)
    try:
        response.raise_for_status()
        pdf_path = os.path.join(download_dir, f"{doc_id}.pdf")
        with open(pdf_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {pdf_path}")
    except requests.exceptions.HTTPError as err:
        print(f"Failed to download {doc_id}: {err}")


def search_solr(query: str, num_pages: int = 1) -> List[str]:
    """Search the UCSF Solr archive and return a list of unique IDs.

    Args:
        query (str): Search query for the Solr archive
        num_pages (int): Number of pages of search results to download

    Returns:
        List[str]: List of unique document IDs
    """
    doc_ids = []
    for i in range(num_pages):
        params = {
            "q": query,
            "wt": "json",
        }
        if i > 0:
            params["start"] = i * 100

        response = requests.get(SOLR_METADATA_BASE_URL, params=params)
        try:
            response.raise_for_status()
            data = response.json()
            # Extract document IDs from the response.
            doc_ids.extend([doc["id"] for doc in data["response"]["docs"]])
        except requests.exceptions.HTTPError:
            break

    return doc_ids


def main(query: str, download_dir: str = DOWNLOAD_BASE_DIR, num_pages: int = 1):
    """Query the Solr archive and download PDFs for the search results.

    Args:
        query (str): Search query for the Solr archive
        num_pages (int): Number of pages of search results to download

    NOTE: Each page of search results contains up to 100 documents.
    """
    download_dir = os.path.join(download_dir, query)
    os.makedirs(download_dir, exist_ok=True)
    doc_ids = search_solr(query, num_pages)
    print(f"Found {len(doc_ids)} documents. Downloading...")
    for id in doc_ids:
        download_pdf(id, download_dir)
    print("All documents downloaded.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download PDFs from the UCSF Industry Documents Library"
    )
    parser.add_argument(
        "--query", required=True, help="Search query for the Solr archive"
    )
    parser.add_argument(
        "--download-dir", default=DOWNLOAD_BASE_DIR, help="Directory to save PDFs"
    )
    parser.add_argument(
        "--num-pages",
        type=int,
        default=1,
        help="Number of pages of search results to download",
    )
    args = parser.parse_args()

    main(**vars(args))
