import json
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha


driver = webdriver.Chrome('c:/users/salex/desktop/chromedriver.exe')
driver.get('https://2captcha.com/auth/login')

email = driver.find_element_by_name('email')
password = driver.find_element_by_name('password')

email.send_keys('salex8490@gmail.com')
password.send_keys('khISBSKgV0Ko' + Keys.RETURN)

work = driver.find_element_by_link_text('StartWork')
work.click()

captcha_type = driver.find_element_by_id('captcha_type')
captcha_type.click()

normal_captcha = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id=\"captcha_type\"]/option[2]")))
normal_captcha.click()

start = driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
start.click()

for x in range(0, 10):
    start_time = datetime.datetime.utcnow()
    while(datetime.datetime.utcnow().second < start_time.second - 18):
        try:
            img = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.ID, "capimg")))

            image = img.get_attribute("src")

            solver = TwoCaptcha('b9611f767e716190f08a5d10303cdcb0')
            result = solver.normal(image)

            m_result = json.dumps(result)
            json_object = json.loads(m_result)
            code = json_object["code"]

            solve = driver.find_element_by_id('code')
            solve.send_keys(code + Keys.ENTER)
        except:
            pass
    else:
        solve = driver.find_element_by_id('code')
        solve.send_keys(Keys.ALT, "Q")
        x += 1

driver.quit()