# import necessary libraries
from flask import Flask, render_template
import pandas as pd
import numpy as np
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pymongo
import pandas as pd


#Create an instance of our Flask app.
app = Flask(__name__)


# webscrape route
@app.route("/scrape")
def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    #get news title and text
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html)

    news_title = soup.find_all("div", {"class": "content_title"})[0].text.strip()
    news_text= soup.find_all("div", {"class": "article_teaser_body"})[0].text.strip()   

    #get featured image
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html)
    for image in soup.find_all("a", {"class": "showimg fancybox-thumbs"}):
        image_url = image["href"]
    featured_image_url = url + image_url

    #mars facts
    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html)
    
    dfs = pd.read_html(html)
    mars_info = dfs[1]
    mars_info = mars_info.rename(columns={0:"category", 1:"mars_info"})
    mars_info.to_html("mars_info.html")

    #hemisphere data
    url = "https://marshemispheres.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html)

    items = soup.find_all("div", {"class": "item"})
    
    #loop through page to get titles and image links for all 4 items
    #list of dictionaries
    hemisphere_image_urls = []
    for item in items:
        #go to page when clicking on image
        image_link = url+item.find("a")["href"]
        url2 = image_link
        browser.visit(url2)
        html2 = browser.html
        soup2 = BeautifulSoup(html2)
        
        #get title
        title = soup2.find("h2", {"class":"title"}).text.strip('Enhanced').strip()
        #get image url (full size)
        img_url = url + soup2.find("img", {"class":"wide-image"})["src"]
        
        #put into dictionary item
        hemisphere_image_urls.append({"title": title, "img_url": img_url})
        
        #return to starting page
        url = "https://marshemispheres.com/"
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html)
    
    #dictionary needed for jinja:
    mars_data = {}
    mars_data["news_title"]=news_title
    mars_data["news_text"]=news_text
    mars_data["featured_image_url"]=featured_image_url
    mars_data["mars_info"]=mars_info.to_html()
    mars_data["hemisphere_image_urls"]=hemisphere_image_urls

    browser.quit()


#MONGODB AND INDEX ROUTE

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

# Drops collection if available to remove duplicates
db.data.drop()

# Creates a collection in the database and inserts two documents
db.team.insert_many(mars_data)

if __name__ == "__main__":
    app.run(debug=True)