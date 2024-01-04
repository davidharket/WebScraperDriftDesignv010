from db import WebsiteDataCollector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instantiate the WebsiteDataCollector class
db = WebsiteDataCollector("website.db")
db._setup_database()
# Set up the Chrome WebDriver
driver_path = "C:/Users/bruker/Desktop/chromedriver.exe"
profile_path = "C:/Users/bruker/AppData/Local/Google/Chrome/User Data/Default"
driver = webdriver.Chrome()

# Open the login page
login_url = 'https://secure.similarweb.com/account/login?returnUrl=%2f'
driver.get(login_url)
wait = WebDriverWait(driver, 10)

linkedin_buttion = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div/button[2]')  # Update if field name is different
linkedin_buttion.click()
driver.implicitly_wait(10)


email = driver.find_element(By.ID,'username')  
password = driver.find_element(By.ID, 'password')
email.send_keys('david@harket.no')
password.send_keys('Sodefjed179')
password.send_keys(Keys.ENTER)
driver.implicitly_wait(100)

driver.get("https://pro.similarweb.com/#/research/marketresearch/webmarketanalysis/marketbuilder?returnToState=digitalsuite_marketresearch_webmarketanalysis_mapping")
wait = WebDriverWait(driver, 1000)

by_industry = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-tabs-2"]/div')))

driver.execute_script("arguments[0].click();", by_industry)
dropdown_click = driver.find_element(By.CLASS_NAME, "DropdownButton")
driver.execute_script("arguments[0].click();", dropdown_click)



for i in range(84,209):
    elements = driver.find_elements(By.CLASS_NAME,"DropdownItem")
    category = elements[i].text
    #Insert category in database
    db.insert_category(category)
    elements[i].click()
    for n in range (1, 100):
        website = driver.find_element(By.XPATH, f'//*[@id="react-tabs-3"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[{str(n)}]/div/div/span')
        domain = website.text
        #Insert domain in database
        db.insert_domain(i+1, domain)
        print(domain)
    driver.execute_script("arguments[0].click();", dropdown_click)

# Clean up: close the browser window
driver.quit()