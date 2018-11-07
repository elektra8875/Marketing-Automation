from bs4 import BeautifulSoup
import request
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re

new_urls = deque(['http://www.themoscowtimes.com/contact_us/index.php'])

processed_urls = set()

emails = set()

while len(new_urls):

	url = new_urls.popleft()
	processed_urls.add(url)
	parts = urlsplit(url)
	base_url = "{0.scheme}://{0.netloc}".format(parts)
	path = url[:url.rfind('/')+1] if '/' in parts.path else url

	print("Processing %s" % url)
	try:
	    response = requests.get(url)
	except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
	      continue

	new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
	emails.update(new_emails)

	soup = BeautifulSoup(response.text)

	for anchor in soup.find_all("a"):
	    link = anchor.attrs["href"] if "href" in anchor.attrs else ''

	    if link.startswith('/'):
	        link = base_url + link
	    elif not link.startswith('http'):
                link = path + link

	    if not link in new_urls and not link in processed_urls: 
	          new_urls.append(link)
