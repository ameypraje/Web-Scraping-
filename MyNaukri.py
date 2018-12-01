import sys
import pandas as pd
from selenium import webdriver

# city name to gather search from that particular city
city=input('Enter city name:- ')

# selenium webdriver for chrome
req=webdriver.Chrome(executable_path='C:/Users/Amey Raje/PycharmProjects/WebScrapping/chromedriver')

data=[]

# Method to fetch number of pages for a particular search!
def page_to_fetch():

    try:

        req.get('https://www.naukri.com/solid-edge-spm-design-autocad-unigraphics-jobs-in-'+city)
        total_pages = req.find_elements_by_xpath('//span[@class="cnt"]')
        Number_of_pages=total_pages[0].text.split(" ")[-1]

        #Number of pages
        actual_pages=int(int(Number_of_pages)/50)
        return actual_pages

    # In case of an error
    except Exception as e:
        req.close()
        sys.exit('city not present')

# Method to fetch data from each page
def data_to_fetch():

    # Storing actual pages in variable
    a=page_to_fetch()

    for i in range(1,a+2):
        if i==1:
            req.get('https://www.naukri.com/solid-edge-spm-design-autocad-unigraphics-jobs-in-'+city)
            print('fetching from page 1')
        else:
            req.get('https://www.naukri.com/solid-edge-spm-design-autocad-unigraphics-in-'+city+str(i))
            print('fetching from page'+str(i))

        # finding elements by Xpath
        design=req.find_elements_by_xpath('//li[@class="desig"]')
        company=req.find_elements_by_xpath('//span[@class="org"]')
        exp=req.find_elements_by_xpath('//span[@class="exp"]')
        skills=req.find_elements_by_xpath('//span[@class="skill"]')

        for i in range(int(len(design))):
            d={}
            d['Designation']=design[i].text
            d['Company']=company[i].text
            d['Experiance']=exp[i].text
            d['Skills']=skills[i].text
            data.append(d)
    return data

# Storing raw data to dataframe for further processing
def to_dataframe():
    data_to_fetch()
    df1=pd.DataFrame(data)

    # creating a csv file using pandas
    df1.to_csv('solid-edge-spm-design-autocad-unigraphics'+city+'.csv',index=False)


to_dataframe()
# closing connection
req.close()

csv_file1=pd.read_csv('solid-edge-spm-design-autocad-unigraphics'+city+'.csv')
