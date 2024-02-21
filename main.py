from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://tinder.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
driver.maximize_window()
driver.implicitly_wait(30)


def accept_cookies():
    try:
        accept_button = driver.find_element(By.XPATH,
                                            value='//*[@id="o-2009197528"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
        accept_button.click()
    except NoSuchElementException:
        print("accept cookies not found")
    time.sleep(1.2)


def login_with_google():
    login_button = driver.find_element(By.XPATH,
                                       value='//*[@id="o-2009197528"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
    login_button.click()
    time.sleep(1.5)

    cont_with_google = driver.find_element(By.XPATH,
                                           value='//*[@id="o557388692"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[1]/div')
    cont_with_google.click()
    time.sleep(5)

    base_window = driver.window_handles[0]
    google_new_window = driver.window_handles[1]
    driver.switch_to.window(google_new_window)
    email = driver.find_element(By.XPATH, value='//*[@id="identifierId"]')
    email.send_keys("@gmail.com")
    time.sleep(0.8)
    next_button = driver.find_element(By.XPATH, value='//*[@id="identifierNext"]/div/button/span')
    next_button.click()
    time.sleep(2)
    password = driver.find_element(By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys("")
    time.sleep(0.8)
    pw_next_button = driver.find_element(By.XPATH, value='//*[@id="passwordNext"]')
    pw_next_button.click()
    time.sleep(2)

    driver.switch_to.window(base_window)


def allow_location():
    allow_location_button = driver.find_element(By.XPATH,
                                                value='//*[@id="o557388692"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
    allow_location_button.click()
    time.sleep(2)


def disallow_notifications():
    no_interested_button = driver.find_element(By.XPATH,
                                               value='//*[@id="o557388692"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
    no_interested_button.click()
    time.sleep(2)


def swipe():
    try:
        print("Try swipe")
        hearth_button = driver.find_element(By.CSS_SELECTOR,
                                            value='.Bdc\\(\\$c-ds-border-gamepad-like-default\\)')
        hearth_button.click()
        global likes
        likes += 1
    except NoSuchElementException:
        print("NoSuchElementException when swipe")
    except ElementClickInterceptedException:
        print("ElementClickInterceptedException")
        try:
            explore = driver.find_element(By.XPATH,
                                          value='/html/body/div[1]/div/div[1]/div/aside/nav[1]/div/a')
            explore.click()
            print("Explore click")
        except:
            print("Explore not found.")
            try:
                print("Try no interested button")
                no_interested = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div[2]/button[2]/div[2]/div[2]')
                no_interested.click()
                print("No interested click")
            except:
                body = driver.find_element(By.XPATH,
                                              value='/html/body')
                body.click()
                print("Body click")

    time.sleep(3)


accept_cookies()
login_with_google()
allow_location()
disallow_notifications()
likes = 0
while likes < 10:
    swipe()

driver.quit()
