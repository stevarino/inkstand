from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

grid_url = "http://localhost:4444/wd/hub"

def main():
  options = get_options()
  print(options)
  driver = webdriver.Remote(
          command_executor=grid_url,
          options=options)
  print(driver.command_executor._client_config.remote_server_addr)

  driver.get("http://www.python.org")
  assert "Python" in driver.title
  elem = driver.find_element(By.NAME, "q")
  elem.clear()
  elem.send_keys("pycon")
  elem.send_keys(Keys.RETURN)
  assert "No results found." not in driver.page_source
  driver.close()

def get_options():
  options = webdriver.ChromeOptions()
  options.add_argument('--no-sandbox') 
  options.add_argument('--headless')
  options.add_argument('--disable-dev-shm-usage')
  return options


if __name__ == '__main__':
  main()
