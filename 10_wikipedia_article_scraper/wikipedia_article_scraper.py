import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# The link to the wikipedia article you want to scrape
base_url = "https://en.wikipedia.org/wiki/Machine_learning"
response = requests.get(base_url)

# Check if the page is downloaded regularly
if response.status_code == 200:
    print(f"Response Status: {response.status_code}")
    
    html = response.content
    print(html[:100])
    
    # Definging the scraper
    soup = BeautifulSoup(html, 'lxml')
    
    # save the page in html file to inspect it more easily 
    # and verify our content and the web page
    with open("wikipedia-article.html", "wb") as file:
        file.write(soup.prettify('utf-8'))
        
    # All definition are in the div with role note
    div_notes = soup.find_all("div", {"role": "note"})
    
    # Getting all the link
    div_links = []
    for div in div_notes:
        anchors = div.find_all('a')
        div_links.extend(anchors)
    
    # Join the sub-urls with the base url
    note_urls = [urljoin(base_url, l.get('href')) for l in div_links]
    
    # save the definitions into a list
    par_text = []
    for i, url in enumerate(note_urls, 1):
        note_resp = requests.get(url)
        if note_resp.status_code == 200:
            print(f"{i}#URL: {url}")
        else:
            print(f"Status_code {note_resp.status_code}: Skipping URL #{i}: {url}")
            continue
        note_html = note_resp.content
        note_soup = BeautifulSoup(note_html, 'lxml')
        note_pars = note_soup.find_all("p")
        text = [p.text for p in note_pars]
        par_text.append(text)

    page_text = ["".join(text) for text in par_text]
    text_dict = dict(zip(note_urls, page_text))
    df = pd.DataFrame(text_dict, index=list(range(1))).transpose()
    df.to_csv('wikipedia_article.csv')
else:
    print(f"ERROR! Response Status: {response.status_code}")