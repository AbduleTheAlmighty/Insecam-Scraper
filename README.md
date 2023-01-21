# Insecam Webcam Scraper
This Python script uses the Grequests library to quickly scrape links to webcams from the Insecam website, and saves them to a text file.

## Requirements
Python 3
grequests
BeautifulSoup
## Usage
Clone or download the project to your local machine.
Install the required libraries by running `pip install grequests bs4` in your command line.
Run the script by executing `python insecam_scraper.py` in the project directory.
Enter your desired maximum number of simultaneous connections (between 1 and 1000).
The script will begin scraping and saving the webcam links to a file named "links.txt".
The script will also output the amount of time it took to complete the scraping process.
## Note
The script is set to scrape 1000 pages of the Insecam website, each page containing 6 webcams.
The script may take a significant amount of time to complete, depending on your internet connection and the number of simultaneous connections.
The script uses a User-Agent and headers to imitate a web browser, as the Insecam website blocks requests from non-browser sources.
If the script encounters any unsuccessful requests, it will notify you to consider decreasing the maximum number of simultaneous connections.
The script does not handle any errors that may occur during the scraping process except status code, so if an error occurs, the script will terminate.