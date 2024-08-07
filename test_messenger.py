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
LOGIN_URL = 'https://substack.com/sign_in'
USER_URL = 'https://jonathanpolitzki.substack.com/?utm_source=discover_search'

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Function to log in to Substack
def login():
    driver.get(LOGIN_URL)
    time.sleep(2)
    
    try:
        email_field = driver.find_element(By.NAME, 'email')
        email_field.send_keys(EMAIL)
        email_field.send_keys(Keys.RETURN)
        time.sleep(2)
    except Exception as e:
        print(f"Error finding email field: {e}")
        driver.quit()
        return
    
    # Wait for manual email verification
    print("Please verify your login via email. Press Enter after verification.")
    input()
    
    try:
        if driver.find_elements(By.NAME, 'password'):
            password_field = driver.find_element(By.NAME, 'password')
            password_field.send_keys(PASSWORD)
            password_field.send_keys(Keys.RETURN)
            time.sleep(5)
        else:
            print("Login verification failed or not required. Proceeding...")
    except Exception as e:
        print(f"Error finding password field: {e}")
        driver.quit()
        return

# Function to message the specified user
def message_user():
    driver.get(USER_URL)
    time.sleep(5)
    
    # Print the page source for debugging
    print(driver.page_source)
    
    # Try to find the message button/link
    try:
        # Adjust the following line based on the actual HTML structure
        message_button = driver.find_element(By.LINK_TEXT, 'Message')
        message_button.click()
        time.sleep(5)
        
        subject_field = driver.find_element(By.NAME, 'subject')
        body_field = driver.find_element(By.NAME, 'body')
        
        subject = "Recommendation Exchange"
        body = f"Hi Jonathan, I'd love to be on your recommended list and in exchange, I'll add you to mine. Let me know if you're interested!"
        
        subject_field.send_keys(subject)
        body_field.send_keys(body)
        body_field.send_keys(Keys.RETURN)
        
        time.sleep(2)  # Sleep to avoid triggering spam filters
        print(f"Message sent to Jonathan Politzki")
    except Exception as e:
        print(f"Error: {e}")

# Main function to run the script
def main():
    login()
    message_user()
    driver.quit()

if __name__ == '__main__':
    main()
