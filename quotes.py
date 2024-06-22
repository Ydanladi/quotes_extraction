import requests
from bs4 import BeautifulSoup
import csv

 
store=[] #storage for sprapped dta
for page in range(6): #looping pages
    url=f"https://quotes.toscrape.com/page/{page}/" # link to website to extract data

    # using request to get data
    data=requests.get(url)

    #parsing with beautifulsoup to grab required data
    soup=BeautifulSoup(data.text, "html.parser")

    #grabbing tags for each div's that contains required data
    tagss=soup.find_all('div', class_='quote')

    #looping through each tag to extract, autor's name, and contents
    for tag in tagss:
        quote=tag.find('span', class_='text').text
        Autor=tag.find('small',class_='author').text
        # adding items to a dictionary
        content={
            'quote':quote,
            'Autor':Autor,
            
        }
        store.append(content) #adding to store list
#saving data to csv
field_names = ['quote', 'Autor'] 
with open('content.csv', 'w') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = field_names) 
    writer.writeheader() 
    writer.writerows(store)
    csvfile.close()
print('finished')
        