# TUGboat Downloader

This repository contains a script for downloading PDFs from the [TUGboat](https://www.tug.org/TUGboat/) archive, specifically targeting the "Complete issue" PDFs. TUGboat is the Communications of the [TeX Users Group](https://www.tug.org/), and this script aims to facilitate access to its rich library of articles for personal use and research.

## How to Use

To use the script, follow these steps:

1. **Clone this repository** to your local machine using `git clone`.
2. **Install the required Python libraries** by running `pip install -r requirements.txt` in your terminal. This script requires `requests` and `beautifulsoup4` to function.
3. **Run the script** with Python by executing `python tugboat_downloader.py` in your terminal. The script will start downloading all available "Complete issue" PDFs from the TUGboat archive into a folder named `tugboat_issues` in your current directory.

## Requirements

- Python 3.6 or newer.
- `requests` and `beautifulsoup4` libraries.

A `requirements.txt` file is included in the repository. Install the required libraries by running:

    pip install -r requirements.txt

## Notes

This repository directly hosts the PDF files as they are expected to remain unchanged over time.
Consequently, incorporating [Git Large File Storage (LFS)](https://git-lfs.github.com/) would introduce an unnecessary technical complexity and requirement.
By avoiding Git LFS, we aim to keep the repository accessible and simple for all users, ensuring straightforward cloning and fetching processes without the need for additional Git configurations.

There is BibTeX data available for all the articles: http://ftp.math.utah.edu/pub/tex/bib/tugboat.html.

## Legal and Ethical Considerations

Please use this script responsibly and ethically. The script is intended for personal use and educational purposes only. Ensure you comply with TUGboat's terms of service and copyright policies before downloading content. This script is not endorsed by or affiliated with TUGboat or the TeX Users Group.

Downloading materials from TUGboat should be done with respect to the website's `robots.txt` file and within the limits of fair use. Be mindful not to overload their servers with high volumes of requests in a short period.

## Contribution

Contributions to the script or documentation are welcome. Please create a pull request or open an issue if you have suggestions for improvements or have identified bugs.

## License

This project is released under the MIT License. See the `LICENSE` file for more details.
The PDFs inside `tugboat_issues` are [licensed by the TeX Users Group](https://tug.org/TUGboat/tubperm.html).

## Acknowledgments

- TUGboat, for providing a comprehensive archive of valuable TeX-related documents.
- The TeX Users Group, for their ongoing contributions to the TeX community.
