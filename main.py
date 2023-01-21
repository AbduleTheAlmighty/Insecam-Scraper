import grequests
from bs4 import BeautifulSoup
from time import perf_counter

headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8","Accept-Language":"en-US,en;q=0.8","Cache-Control":"max-age=0","Connection":"keep-alive","Sec-GPC":"1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

def getWebcams(responses): #Parses the responses it's given and saves all webcams to "links.txt"
  with open("links.txt", "a") as file:# It appends to the existing text, so remember to clear the file before running this function
    for r in responses:
      if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        webcams = soup.find_all("img", {"class": "thumbnail-item__img img-responsive"}) #Finds the webcams
        for i in webcams:
          file.write(f'{i["src"]}\n')
      else:
        print("\033[31mError, consider decreasing the max connections.\033[0m") #Notifies you of unsuccessful requests

def scrapeWebcams(MAX_CONNECTIONS):
  urlsList = [f"http://www.insecam.org/en/byrating/?page={i}" for i in range(1,1001)]
  
  for x in range(1,1001, MAX_CONNECTIONS):
    rs = (grequests.get(u, headers=headers, stream=False, timeout=30) for u in urlsList[x:x+MAX_CONNECTIONS])
    getWebcams(grequests.map(rs)) #Sends the requests and parses the responses

if __name__ == "__main__":
  MAX_CONNECTIONS = 0
  while 1>MAX_CONNECTIONS or MAX_CONNECTIONS>1000:
    try:
      MAX_CONNECTIONS = int(input("What is your desired max connections? (Must be between 1 and 1000) "))
      if 1>MAX_CONNECTIONS or MAX_CONNECTIONS>1000:
        print("\033[31mError, the max connections must be between 1 and 1000.\033[0m")
    except:
      print("\033[31mError, max connections must be a number.\033[0m")
  start = perf_counter()
  print("Starting scraping webcams.")
  scrapeWebcams(MAX_CONNECTIONS)
  stop = perf_counter()
  print("Finished scraping Insecam webcams in", int(stop - start), "seconds.")