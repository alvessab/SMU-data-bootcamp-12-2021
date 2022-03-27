# import necessary libraries
from flask import Flask, render_template
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
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


if __name__ == "__main__":
    app.run(debug=True)