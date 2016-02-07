import requests
import bs4
import os

manga_name=raw_input("Which manga do you wish to download:")
begin=input("Enter first chapter:")
number_chap=input("Enter how many chapters you want:")

#for creating url:
list_of_words=manga_name.split(" ")
m=''
for g in list_of_words:
    m=m+g+'-'
    
manga_name_url=m[:-1]


# making folder
os.chdir('C:\Users\sony\Desktop')
if not os.path.exists("C:\Users\sony\Desktop\manga"):
    os.mkdir('manga')
os.chdir('C:\Users\sony\Desktop\manga')
if not os.path.exists("C:\Users\sony\Desktop\manga"+"\\"+manga_name):
    os.mkdir(manga_name)
os.chdir('C:\Users\sony\Desktop\manga'+"\\"+manga_name)

for k in range(begin,begin+number_chap):
    count=1
    url_page=requests.get('http://www.mangareader.net/'+manga_name_url+'/'+str(k))
    
    
    if not os.path.exists("C:\Users\sony\Desktop\manga"+"\\"+manga_name+'\chapter'+str(k)):
        os.mkdir('chapter'+str(k))
    os.chdir('C:\Users\sony\Desktop\manga'+"\\"+manga_name+'\chapter'+str(k))
    while url_page.status_code==200:
        
        url_soup=bs4.BeautifulSoup(url_page.content)
        img_div=url_soup.find(id='img')
        src=img_div.get('src')
        page=open('page'+str(count)+'.jpeg',"wb+")
        page2=requests.get(src)
        page.write(page2.content)
        page.close()
        count+=1
        url_page=requests.get('http://www.mangareader.net/'+manga_name_url+'/'+str(k)+'/'+str(count))
    os.chdir('C:\Users\sony\Desktop\manga'+"\\"+manga_name)    

        
