import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#function that is called from main
def downloader(query_name, user, passw):

    #start driver
    driver = webdriver.Chrome()
    driver.get('https://fmis.mbta.com/psp/MTFP92/?cmd=start')


    #username
    username = driver.find_element("name", "userid")
    username.send_keys(user)

    #password
    password = driver.find_element("name", "pwd")
    password.send_keys(passw)

    #login
    login = driver.find_element("name", "Submit")
    login.click()

    #search bar
    searchbar = driver.find_element(By.ID, "PTSKEYWORD")
    searchbar.send_keys('Query')

    #click Query Manager, wait 25 seconds before clicking on search result
    searchResultQM = driver.find_element(By.ID, "PTS_INTELLISRCH_RS$0_row_1")
    driver.implicitly_wait(25)
    searchResultQM.click()

    #switch frames, enter query
    driver.switch_to.frame('ptifrmtgtframe')
    query_search = driver.find_element("name", "QRY_VIEWERS_WRK_QRYSEARCHTEXT254")
    query_search.send_keys(query_name)
    search_button = driver.find_element("name", "QRY_VIEWERS_WRK_QRYSEARCHBTN")
    search_button.click()


    #download query
    download_button = driver.find_element("name", "QRYRUNEXCEL$0")
    download_button.click()
    #three minute wait for big files
    time.sleep(180)


    driver.close()