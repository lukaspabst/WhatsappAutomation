import random
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Schedule the script to run at a random time between 7:00 AM and 8:00 AM
now_utc = datetime.utcnow()
# Get the current time
now_euw = now_utc + timedelta(hours=2)

# Calculate the start and end times for the window
start_time = now_euw.replace(hour=22, minute=0, second=0, microsecond=0)
end_time = now_euw.replace(hour=23, minute=0, second=0, microsecond=0)

# Calculate a random time within the window
random_time = start_time + timedelta(seconds=random.randint(0, int((end_time - start_time).total_seconds())))

# Calculate the delay needed to reach that time
delay = (random_time - now_euw).total_seconds()

print(f"Script will run at approximately {random_time.strftime('%H:%M:%S')}")
print("That is in " + str(delay) + " seconds")
# Sleep until the calculated random time
time.sleep(delay)
chrome_profile_path = "/home/ubuntu/chrome-profile/Default"
# Set up the Chrome driver and options
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
chrome_options.add_argument("--window-size=1920x1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://web.whatsapp.com')
try:
    # Open WhatsApp Web


    # Wait for the QR code element
    qr_code_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='landing-main']"))
    )
    print("QR code element found.")
    time.sleep(15)
    # Take a screenshot of the QR code element
    qr_code_element.screenshot('qr_code.png')
    print("Screenshot saved as qr_code.png.")

except TimeoutException:
    print("QR code element not found within the specified time. Continuing with the script.")

# Example: Send a message to a contact (replace with actual contact details and message)
contact_name = 'Kontakt'
message_text = "Nachricht"

try:
    # Find the contact by name and send a message
    xpath_contact = f"//span[@title='{contact_name}']"

    # Find the chat and open it
    contact = driver.find_element("xpath", xpath_contact)
    contact.click()
    time.sleep(5)
    message_box_xpath = '//div[@contenteditable="true" and @data-tab="10"]'

    # Wait until the message input field is visible
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, message_box_xpath)))

    # Enter the message
    message_box = driver.find_element("xpath", message_box_xpath)
    # Send the message by simulating the Enter key
    message_box.send_keys(message_text + Keys.ENTER)  # Send message
    print("Message sent.")
    time.sleep(2)
except TimeoutException:
    print("Could not find the contact or message box within the specified time.")
# Quit the driver
driver.quit()