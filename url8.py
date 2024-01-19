from selenium import webdriver

url = "http://www.nidec-precision.co.th/Vendor"

# Set up the Selenium WebDriver (make sure to download the appropriate WebDriver for your browser)
driver = webdriver.Chrome()  # You can use other browser drivers (e.g., Firefox, Edge) based on your preference

try:
    # Open the website
    driver.get(url)

    # Execute JavaScript code (replace the example code with your JavaScript)
    javascript_code = "alert('Hello from Python!');"
    driver.execute_script(javascript_code)

finally:
    # Close the browser window
    driver.quit()
