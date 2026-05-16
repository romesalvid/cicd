from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # run headless in CI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Point to your ChromeDriver
service = Service("/snap/bin/chromedriver")  # <-- adjust path if needed

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
