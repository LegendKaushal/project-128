import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import csv
import pandas as pd

#START_URL =  "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
#browser = webdriver.Chrome(executable_path= r"C:\Users\Ravic\Desktop\c-127\chromedriver_win32\chromedriver.exe")
#browser.get(START_URL)

bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars' 
page = requests.get(bright_stars_url) 
print(page) 
soup = bs(page.text,'html.parser') 
star_table = soup.find('table')

time.sleep(10)
#temp_list = []

temp_list= [] 
table_rows = star_table.find_all('tr') 
for tr in table_rows: 
    td = tr.find_all('td') 
    row = [i.text.rstrip() for i in td] 
    temp_list.append(row)
    Star_names = [] 
    Distance =[] 
    Mass = [] 
    Radius =[] 
    Lum = []
    for i in range(1,len(temp_list)): 
        Star_names.append(temp_list[i][1]) 
        Distance.append(temp_list[i][3]) 
        Mass.append(temp_list[i][5]) 
        Radius.append(temp_list[i][6]) 
        Lum.append(temp_list[i][7])

    df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity']) 
    print(df2) 
    df2.to_csv('bright_stars.csv')


#def scrape():
#    headers = ["V Mag","Proper name","Bayer designation","Distance(ly)","Spectral class","Mass","Radius","Luminosity"]
 #   planet_data = []
 #   soup = bs(browser.page_source,"html.parser")
 #   for table_tag in soup.find_all("table_tag",attrs={"class","wikitable sortable jquery-troubleshooter"}):
  #      tbody_tags = table_tag.find_all("tbody")
   #    
    #    for tbody_tags in tbody_tags:
     #       for tr_tags in tbody_tags.find_all("tr"):
      #          td_tags = tr_tags.find_all("td")
       #         for index,td_tags in enumerate(index,td_tags):
        #            if index == 0:
         #                   temp_list.append(tbody_tags.find_all("a")[0].contents[0])
          #          else:
           #             try:
            #                temp_list.append(tbody_tags.contents[0])
             #           except:
              #              temp_list.append("")
            #
            #planet_data.append(temp_list)
       #
    #with open("book_3.csv","w") as f:
     #   csv_writer = csv.writer(f)
      #  csv_writer.writerow(headers)
       # csv_writer.writerows(planet_data)
#
#scrape()


#temp_list= [] table_rows = star_table.find_all('tr') for tr in table_rows: td = tr.find_all('td') row = [i.text.rstrip() for i in td] temp_list.append(row)
#
#Star_names = [] Distance =[] Mass = [] Radius =[] Lum = []
#
#for i in range(1,len(temp_list)): Star_names.append(temp_list[i][1]) Distance.append(temp_list[i][3]) Mass.append(temp_list[i][5]) Radius.append(temp_list[i][6]) Lum.append(temp_list[i][7])

#df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity']) print(df2) df2.to_csv('bright_stars.csv')