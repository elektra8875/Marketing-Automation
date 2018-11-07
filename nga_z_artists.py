
import requests
import csv
from bs4 import BeautifulSoup
# collect first page of artist lists

# page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

# soup = BeautifulSoup(page.text,'html.parser')

# Remove bottom links

# last_links = soup.find(class_='AlphaNav')
# last_links.decompose()


# create a file to write to, make headers roq
# f = csv.writer(open('z-artist-names.csv', 'w'))
# f.writerow(['Name', 'Link'])

# Pull all text from the BodyText div
# artist_name_list = soup.find(class_='BodyText')

# Pull text from all instances of <a> tag within BodyText div
# artist_name_list = soup.find(class_='BodyText')


# Pull text from all instances of <a> tag within BodyText div
# artist_name_list_items = artist_name_list.find_all('a')

# create for loop to print out all artists names

# for artist_name in artist_name_list_items:
	# names = artist_name.contents[0]
	# links = 'https://web.archive.org' + artist_name.get('href')
	# print(names)
	# print(links)
	
# add each artist's name and associated row
# f.writerow([names, links])

f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []

for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)


for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')

        f.writerow([names, links])
                                 
