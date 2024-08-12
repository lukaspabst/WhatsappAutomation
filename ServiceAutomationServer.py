import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def send_scheduled_message():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options, executable_path='/usr/local/bin/chromedriver')
    driver.get('https://web.whatsapp.com')
    time.sleep(15)

    target = '"Contact Name or Number"'
    message = "Good morning! This is a scheduled message."

    search_box = driver.find_element("xpath", '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(target + Keys.ENTER)

    time.sleep(2)

    message_box = driver.find_element("xpath", '//div[@contenteditable="true"][@data-tab="9"]')
    message_box.send_keys(message + Keys.ENTER)

    print("Scheduled message sent!")
    driver.quit()

# Schedule the message to be sent every day at 09:00 AM
schedule.every().day.at("09:00").do(send_scheduled_message)

while True:
    schedule.run_pending()
    time.sleep(1)
