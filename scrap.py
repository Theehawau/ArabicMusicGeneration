import os, requests
from bs4 import BeautifulSoup

os.chdir('/Users/adham/Desktop/music_Gen')
#sheren  <-- name of artist page on https://mp3songs.alarab.com website the rest of the script will download all artist songs
r = requests.get('https://mp3songs.alarab.com/singer-336-جميع_اغاني_والبومات_شيرين_عبد_الوهاب.html')

baseurl = str(r.url)

clist=[]
searchsoup = BeautifulSoup(r.text, 'html.parser')

c = searchsoup.find("ul",{"class" : "artistMediumList musicArtistMedium list"})

url = "https://mp3songs.alarab.com"
i=0
for tables in c.find_all("table"):
    #print(tables)
    
    if i >= 0:
        td = tables.find_all('td')
        
        for table in range(0,len(td) ,5 ) :
            
            a_tags = td[table].find_all('a', href=True)
            
            print(a_tags)
            if len(a_tags) > 0 :
                
                link = url+a_tags[0]['href']
                response = requests.get(link)
                print("link = ",link)
                soup = BeautifulSoup(response.text, 'html.parser')
                singer = soup.find('div',{'class':'Singer_intro'})
                link = singer.find_all('a')[1]['href']
                print("link 2 = ",link)
                response = requests.get(link)
                print("response = ",response.text)
                soup = BeautifulSoup(response.text, 'html.parser')
                link = str(link)
                link = link.replace(' ','%20')
                download = requests.get(str(link))
                
                name = str(link).split('/')
                name = name[-1].replace('.R','')
                name = name.replace('%20','_')        

                artist = str(link).split('/')[-3].replace('%20','_')
                if i == 0:
                    os.mkdir(artist)
                    os.chdir(artist)
                    i=1
                print(name)
                if download.status_code == 200:
                    with open(name, 'wb') as f:
                        f.write(download.content)
                else:
                    print(f"Download Failed For File {name}")

            i+=1

