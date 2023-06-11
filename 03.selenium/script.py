URL = ""
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# General Setup
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--headless=new")
chromeOptions.add_argument("--incoginto")

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.google.com")
driver.maximize_window()

timeout = 30
wait = WebDriverWait(driver, timeout)
action = ActionChains(driver)

try:
    # driver.implicitly_wait(20)
    searchBar = wait.until(EC.presence_of_element_located((By.ID, 'APjFqb')))
    searchBar.send_keys("Search something")

    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main")))

    print("Page is ready!")
except Exception:
    print("Loading took too much time!")

sleep(10)
driver.close()