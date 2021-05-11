from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time

executable_path={"executable_path": "webdriver/chromedriver"}
browser=Browser("chrome", **executable_path, headless=False)
url = "https://mars.nasa.gov/news/"
browser.visit(url)
html = browser.html
soup = bs(html,"html.parser")
#print(soup.prettify())


results = soup.find_all('li', class_="slide")
#print(results)

title_list = []
txt_list = []
link_list = []
for result in results:

    try:
        title_list.append(result.find(class_="content_title").text)
        txt_list.append(result.find(class_="rollover_description_inner").text)
        link_list.append(result.a['href'])

    except AttributeError as e:
        print(e)

news_title = title_list[0]
news_p = txt_list[0]
news_l = link_list[0]

print(news_title)
print(news_p)
print(news_l)

url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)

browser.find_by_css('.fancybox').click()
time.sleep(5)
browser.click_link_by_partial_text('more info')
#browser.links.find_by_partial_text('more info').click()


html = browser.html
soup = bs(html,"html.parser")
#print(soup.prettify())

results = soup.find_all(class_="download_tiff")
print(results)

image_link = results[1].a['href']
featured_image_url = "https:" + image_link
print(featured_image_url)

from IPython.display import Image
#from IPython.core.display import HTML
Image(url= featured_image_url)

url = "https://twitter.com/MarsWxReport"
browser.visit(url)


html = browser.html
soup = bs(html,"html.parser")
#print(soup.prettify())


import re
mars_weather=soup.find(text=re.compile("InSight sol"))
print(str(mars_weather))

url = "https://space-facts.com/mars/"

tables = pd.read_html(url)
#tables

mars_table_df = tables[0]
mars_table_df.columns = ["Description", "Info"]
mars_table_df

mars_table_df.set_index('Description', inplace=True)
mars_table_df

#mars_table_df.to_html('table.html')

mars_html_table = mars_table_df.to_html()
mars_html_table = mars_html_table.replace("\n", "")
mars_html_table

hemisphere_img_urls = []

url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
time.sleep(2)
browser.click_link_by_partial_text('Cerberus')
#browser.links.find_by_partial_text('Cerberus').click()
time.sleep(2)
html = browser.html
soup = bs(html,"html.parser")
#print(soup.prettify())

results_link_01 = soup.find(class_="downloads").a['href']
print(results_link_01)

results_title_01 = soup.find('h2', class_="title").text
print(results_title_01)

browser.back()

dictionary_entry_01 = {"title":results_title_01, "image url": results_link_01}
hemisphere_img_urls.append(dictionary_entry_01)

Image(url= results_link_01)

url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
time.sleep(2)
browser.click_link_by_partial_text('Schiaparelli')
#browser.links.find_by_partial_text('Schiaparelli').click()
time.sleep(2)
html = browser.html
soup = bs(html,"html.parser")
#print(soup.prettify())

results_link_02 = soup.find(class_="downloads").a['href']
print(results_link_02)

results_title_02 = soup.find('h2', class_="title").text
print(results_title_02)

browser.back()

dictionary_entry_02 = {"title":results_title_02, "image url": results_link_02}
hemisphere_img_urls.append(dictionary_entry_02)

Image(url= results_link_02)

url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
time.sleep(2)
browser.click_link_by_partial_text('Syrtis')
#browser.links.find_by_partial_text('Syrtis').click()
time.sleep(2)
html = browser.html
soup = bs(html,"html.parser")
#print(soup.prettify())

results_link_03 = soup.find(class_="downloads").a['href']
print(results_link_03)

results_title_03 = soup.find('h2', class_="title").text
print(results_title_03)

browser.back()

dictionary_entry_03 = {"title":results_title_03, "image url": results_link_03}
hemisphere_img_urls.append(dictionary_entry_03)

Image(url= results_link_03)

url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
time.sleep(2)
browser.click_link_by_partial_text('Valles')
#browser.links.find_by_partial_text('Valles').click()
time.sleep(2)
html = browser.html
soup = bs(html,"html.parser")
#print(soup.prettify())

results_link_04 = soup.find(class_="downloads").a['href']
print(results_link_04)

results_title_04 = soup.find('h2', class_="title").text
print(results_title_04)

browser.back()

dictionary_entry_04 = {"title":results_title_04, "image url": results_link_04}
hemisphere_img_urls.append(dictionary_entry_04)

Image(url= results_link_04)

hemisphere_img_urls