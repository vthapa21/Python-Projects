from GoogleNews import GoogleNews
import pandas as pd



news =GoogleNews(period='1d')
Country = str(input("Enter a Country- "))
news.search(Country)
res =news.result()


#Displaying the important  bits
for i in res:
    print("Title- ", i["title"])
    
    print("News- ", i["desc"])
    print("\n")
    print("Read Full News- ", i["link"])
    print("\n")
    
