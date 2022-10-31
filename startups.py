#packages for streamlit
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

@st.experimental_singleton
def installff():
  os.system('sbase install geckodriver')
  os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

#chrome_driver = os.path.abspath(os.path.dirname(__file__)) + '/chromedriver'
#service = webdriver.Chrome(ChromeDriverManager().install())
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless')
#options.add_argument('--no-sandbox')
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
_browser = webdriver.Chrome(options=options, service=service)
usr=st.secrets['usr']
psw=st.secrets['psw']

@st.experimental_singleton
def loginDealroom(_browser,usr,psw):
    # Go to Dealroom Login page
    _browser.get('https://app.dealroom.co/dashboard')
    time.sleep(5)
    _browser.find_element(By.CLASS_NAME, 'cw__button-text').click()
    time.sleep(4)
    _browser.find_element(By.CSS_SELECTOR, "button[data-testid='user-menu-button-login']").click()
    #browser.get('https://accounts.dealroom.co/login?state=hKFo2SBZMDc2bnE5d2ZyMW56RXRaQ3BlU2w3dmxVa1FHRVhieqFupWxvZ2luo3RpZNkgV3JpQ1NCdmliRWFXc3d3XzEwenpHRTZ2VkRBbTN0S0KjY2lk2SAyYlM4WE9zY0F6cGw3Z0lZT0cxZTVEaHVmZjVPOGd0Mw&client=2bS8XOscAzpl7gIYOG1e5Dhuff5O8gt3&protocol=oauth2&audience=https%3A%2F%2Fapi.dealroom.co%2Fapi%2Fv2&redirect_uri=https%3A%2F%2Fapp.dealroom.co&scope=openid%20profile%20email&response_type=code&response_mode=query&nonce=d0ttcWJMZTBzVU1pVE1ILTdDTzg3Zm4xM3l1bzlPZC1qV3EzTFE1bW85cQ%3D%3D&code_challenge=feGVFv_6zPOm9tDeaT_aP2UZhqjJfMU-lY73b_Zns30&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtcmVhY3QiLCJ2ZXJzaW9uIjoiMS45LjAifQ%3D%3D')
    time.sleep(3)
    _browser.find_element(By.ID,'1-email').send_keys(usr)
    time.sleep(1)
    _browser.find_element(By.ID,'1-password').send_keys(psw)
    time.sleep(1)
    _browser.find_element(By.CLASS_NAME,'auth0-label-submit').click()
    time.sleep(5)
    _browser.get('https://app.dealroom.co/searches/55376')
    time.sleep(3)
    return _browser

browser=loginDealroom(_browser,usr,psw)
st.write("Signed in and ready to go...")

def getJobInfo(j):
    title = ''
    company = ''
    location = ''
    company_funding = ''
    title = j.find_element(By.CSS_SELECTOR, "h5[class='type-element type-element--h5 entity-overview__link']").text
    st.write(title)
    company = j.find_element(By.CSS_SELECTOR,"h3[class='type-element type-element--h3 entity-overview__heading']").text
    location = j.find_element(By.CLASS_NAME,'entity-overview__heading__medium').text
    company_funding = j.find_element(By.CLASS_NAME,'entity-overview__heading__strong').text
    return [title,company,location,company_funding]
    

def getDealroomJobs():
    browser.get('https://app.dealroom.co/jobs/f/company_status/anyof_operational/employees_max/anyof_500/employees_min/anyof_60/founder_strength/anyof_Has%20exceptional%20founder/job_locations/anyof_United%20States_Remote/job_types/anyof_Backend%20development_Data%20Science%20%26%20Engineering_Design_Android%20Development_iOS%20Development_Full-stack%20development_Frontend%20development_DevOps/last_funding_month/anyof_jul_aug_sep_oct_nov_dec/last_funding_round/anyof_SERIES%20B/last_funding_year/anyof_2022/vc_backed/anyof_VC%20Backed?sort=&row_index=100')
    time.sleep(2)
    st.write("Searching Dealroom with following search requirement...")
    st.write('https://app.dealroom.co/jobs/f/company_status/anyof_operational/employees_max/anyof_500/employees_min/anyof_60/founder_strength/anyof_Has%20exceptional%20founder/job_locations/anyof_United%20States_Remote/job_types/anyof_Backend%20development_Data%20Science%20%26%20Engineering_Design_Android%20Development_iOS%20Development_Full-stack%20development_Frontend%20development_DevOps/last_funding_month/anyof_jul_aug_sep_oct_nov_dec/last_funding_round/anyof_SERIES%20B/last_funding_year/anyof_2022/vc_backed/anyof_VC%20Backed?sort=&row_index=100')
    browser.maximize_window()
    time.sleep(5)
    st.write("This can take a second but hey just take the time to practice some gratitude...")
    time.sleep(10)
    #html = browser.find_element(By.CLASS_NAME, 'infinite-grid')
    #html.send_keys(Keys.END)
    #actions = ActionChains(browser)
    #browser.execute_script("window.scrollTo(0, 40000);")
    #browser.execute_script("scroll(0, 3000)")
    jobs = browser.find_elements(By.CLASS_NAME,'infinite-grid-list-item')
    st.write("Series B startup roles: ", len(jobs))

    l=[]
    #jobData = [['title','company','location','company_funding']]
    for j in jobs:
        title = j.find_element(By.CSS_SELECTOR, "h5[class='type-element type-element--h5 entity-overview__link']").text
        st.write(title)
        company = j.find_element(By.CSS_SELECTOR,"h3[class='type-element type-element--h3 entity-overview__heading']").text
        location = j.find_element(By.CLASS_NAME,'entity-overview__heading__medium').text
        company_funding = j.find_element(By.CLASS_NAME,'entity-overview__heading__strong').text
        #actions.move_to_element(j).perform()
        #try:
        #    jobData.append(getJobInfo(j))
        #except:
        #    pass
        time.sleep(1)
        tup=(title,company,location,company_funding)
        l.append(tup)
    df = pd.DataFrame(l,columns=['title','company','location','venture funding'])
    #df = pd.DataFrame(jobData[1:],columns=jobData[0])
    return df

jobs = getDealroomJobs()
st.table(jobs)
jobs_consolidated = jobs.groupby("company").agg({"title": 'count'})
jobs_consolidated = jobs_consolidated.rename_axis('Company')
jobs_consolidated = jobs_consolidated.reset_index()
jobs_consolidated["Count of Open Roles"] = jobs_consolidated["title"]
jobs_consolidated = jobs_consolidated.drop("title", axis=1)
st.table(jobs_consolidated)
