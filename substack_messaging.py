import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Replace with your Substack login credentials
EMAIL = 'politzki18@gmail.com'
PASSWORD = 'Jon12345'

# URLs
LOGIN_URL = 'https://substack.com/sign-in'
EXPLORE_URL = 'https://substack.com/explore'

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Function to log in to Substack
def login():
    driver.get(LOGIN_URL)
    time.sleep(2)
    
    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys(EMAIL)
    email_field.send_keys(Keys.RETURN)
    time.sleep(2)
    
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)

# Function to fetch writers
def fetch_writers():
    driver.get(EXPLORE_URL)
    time.sleep(5)
    
    # Adjust the following line based on the actual HTML structure
    writers = driver.find_elements(By.CSS_SELECTOR, '.substack-card')
    writer_ids = [writer.get_attribute('data-id') for writer in writers]
    writer_names = [writer.text for writer in writers]
    return list(zip(writer_ids, writer_names))

# Function to message a writer
def message_writer(writer_id, writer_name):
    message_url = f'https://substack.com/write/{writer_id}/message'
    driver.get(message_url)
    time.sleep(5)
    
    subject_field = driver.find_element(By.NAME, 'subject')
    body_field = driver.find_element(By.NAME, 'body')
    
    subject = "Recommendation Exchange"
    body = f"Hi {writer_name}, I'd love to be on your recommended list and in exchange, I'll add you to mine. Let me know if you're interested!"
    
    subject_field.send_keys(subject)
    body_field.send_keys(body)
    body_field.send_keys(Keys.RETURN)
    
    time.sleep(2)  # Sleep to avoid triggering spam filters
    print(f"Message sent to writer {writer_name}")

# Main function to run the script
def main():
    login()
    writers = fetch_writers()
    if writers:
        for i, (writer_id, writer_name) in enumerate(writers[:10]):
            message_writer(writer_id, writer_name)
            time.sleep(2)
    else:
        print("No writers found or error fetching writers.")
    
    driver.quit()

if __name__ == '__main__':
    main()

