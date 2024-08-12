from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Configure Chrome options for headless execution
chrome_profile_path = "/chrome-profile"
# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile_path}")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
options.add_argument("--window-size=1920x1080")

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')
print("Open WhatsApp!")
# Wait for the QR code to appear
try:
    qr_code_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='landing-main']"))
    )
    print("QR code element found.")
    time.sleep(15)
    qr_code_element.screenshot('qr_code.png')
    print("Screenshot saved as qr_code.png.")

except TimeoutException:
    print("QR code element not found within the specified time. Continuing with the script.")

# Wait for the user to scan the QR code (adjust the time if needed)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='3']")))

# Name or number of the contact or group
contact_name = 'Kontakt Name'
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
message = "xxxx"
message_box.send_keys(message + Keys.ENTER)  # Send message

# Wait to ensure the message is sent
time.sleep(2)  # Short wait to ensure the UI updates

# XPath for the last sent message
last_message_xpath = f"//span[@class='selectable-text invisible-space copyable-text' and contains(text(), '{message}')]"

# Wait to check if the last sent message appears in the chat
#try:
#    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, last_message_xpath)))
#    print("Message sent!")
#except Exception as e:
#    print("Message not sent. Error:", e)

# Close the browser only after sending the message
driver.quit()
