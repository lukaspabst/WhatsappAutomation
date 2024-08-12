from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Specify the path to your Chrome profile
chrome_profile_path = r"C:\Users\xxx\AppData\Local\Google\Chrome\User Data\Profile 1"

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile_path}")

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code (adjust the time if needed)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='3']")))

# Name or number of the contact or group
contact_name = 'Name des Kontakts'
xpath_contact = f"//span[@title='{contact_name}']"

# Find the chat and open it
contact = driver.find_element("xpath", xpath_contact)
contact.click()

time.sleep(5)  # Wait for the chat to load

# XPath for the message input field
message_box_xpath = '//div[@contenteditable="true" and @data-tab="10"]'

# Wait until the message input field is visible
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, message_box_xpath)))

# Enter the message
message_box = driver.find_element("xpath", message_box_xpath)
message = "Nachricht"
message_box.send_keys(message + Keys.ENTER)  # Send message

# Wait to ensure the message is sent
time.sleep(2)  # Short wait to ensure the UI updates

# XPath for the last sent message
last_message_xpath = f"//span[@class='selectable-text invisible-space copyable-text' and contains(text(), '{message}')]"

# Wait to check if the last sent message appears in the chat
#try:
#   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, last_message_xpath)))
print("Message sent!")
#except Exception as e:
#   print("Message not sent. Error:", e)

# Close the browser only after sending the message
driver.quit()
