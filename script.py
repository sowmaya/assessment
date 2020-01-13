import requests;
from bs4 import BeautifulSoup

# Fetch the html page and parse it
page = requests.get('https://www.billboard.com/charts/hot-100')
soup = BeautifulSoup(page.text, 'html.parser')

# extract titles and artists
title_class = "chart-element__information__song text--truncate color--primary"
artist_class = "chart-element__information__artist text--truncate color--secondary"
title_list = soup.findAll('span', {"class":title_class})
artist_list = soup.findAll('span', {"class":artist_class})


# Strip out html tags around title and artist elements
title_list = map(lambda x : x.text.strip(), title_list)
artist_list = map(lambda x : x.text.strip(), artist_list)

# Crete a mapping of artist and title
title_with_artist = dict(zip(title_list, artist_list))

# sort titles based on len func
result = sorted(title_list,  key=len)

# for the list of sorted title print the artist
for item in result:
    # print the artist name from the title_artist dict
    print title_with_artist[item]