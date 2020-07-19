from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="Users/Rohanmahto/Documents/__pycache__/coronaupdate/corno.ico",
        timeout=15
    )
def getdata(url):
    r=requests.get(url)
    return r.text
if __name__== "__main__":
    while True:
        #notifyMe("rohan","you are so good")
        myhtmldata=getdata('https://www.mohfw.gov.in/')
        soup=BeautifulSoup(myhtmldata, 'html.parser')
    #print(soup.prettify())
        mydatastr=''
    #print(soup.prettify())
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            mydatastr+=tr.get_text()
        mydatastr=mydatastr[1:]
        itemlist=mydatastr.split("\n\n")

        states=["Bihar","Uttar Pradesh","Delhi","Assam","Tamil Nadu"]
        for item in itemlist[0:35]:
            print(item)
            datalist=item.split("\n")
            
            if datalist[1] in states:
                nTitle="Cases of Covid-19"
                nText=f"State :{datalist[1]} & Active:{datalist[2]}\nCured :{datalist[3]}\nDeath :{datalist[4]} & Confirmed Cases :{datalist[5]}"
                notifyMe(nTitle,nText)
                time.sleep(18)
        time.sleep(3600)


