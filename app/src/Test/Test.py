# Import the necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the URL of the page you want to visit
url = "https://steamdb.info/graph/"

# Use the Chrome web driver and initialize the page
driver = webdriver.Chrome()
driver.get(url)

# Use the XPATH you provided to find all of the links on the page
Apps = driver.find_element(By.XPATH, '//*[@id="table-apps"]/tbody')
Games = Apps.find_element(By.CLASS_NAME, 'app')
Infos = Games.find_element(By.CLASS_NAME, 'app')

# Loop through each link and open it in a new tab
for Game in Games:
  print(Game.text)

# Close the driver to end the script
driver.close()