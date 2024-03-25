import os
import requests
from bs4 import BeautifulSoup

# The base URL of the site to ensure absolute URL generation
BASE_URL = "https://www.tug.org/TUGboat/Contents/"
INDEX_URL = "https://www.tug.org/tugboat/contents.html"
DOWNLOAD_DIR = "./tugboat_issues"  # Directory to save the downloaded PDFs

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def get_soup(url):
    """Utility function to get a BeautifulSoup object from a URL."""
    print(f"Retrieving page: {url}")
    response = requests.get(url)
    response.raise_for_status()  # Will stop the script if the request fails
    return BeautifulSoup(response.text, 'html.parser')

def download_pdf(url, filename):
    """Utility function to download a PDF from a URL. Skips download if unauthorized or file already exists."""
    print(f"Checking: {url}")
    # Check if the file already exists
    if os.path.exists(filename):
        print(f"File already downloaded: {filename}")
        return
    try:
        response = requests.get(url)
        # Check for unauthorized access before attempting to download
        if response.status_code == 401:
            print(f"Skipping unauthorized download: {url}")
            return
        response.raise_for_status()  # This will handle other HTTP errors
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err} - URL: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def main():
    index_soup = get_soup(INDEX_URL)
    issue_links = [link.get('href') for link in index_soup.find_all('a') if link.get('href') and "Contents/contents" in link.get('href')]

    if not issue_links:
        print("No issue links found on the index page.")
        return

    for href in issue_links:
        issue_page_url = BASE_URL + href.split('/')[-1]
        issue_soup = get_soup(issue_page_url)
        complete_issue_link = issue_soup.find(lambda tag: tag.name == 'a' and 'Complete issue' in tag.text)
        if complete_issue_link:
            pdf_url = complete_issue_link.get('href')
            # Check if the URL starts with http:// or https://
            if not pdf_url.startswith(('http://', 'https://')):
                pdf_url = "https://www.tug.org" + pdf_url
            pdf_filename = os.path.join(DOWNLOAD_DIR, pdf_url.split('/')[-1])
            download_pdf(pdf_url, pdf_filename)
        else:
            print(f"No 'Complete issue' link found on page: {issue_page_url}")

if __name__ == "__main__":
    main()
