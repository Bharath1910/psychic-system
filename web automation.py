from selenium import webdriver

inp1 = str(input("search:-  "))

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

searchbox = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys(inp1)

searchbutton = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/div[2]/div[1]/div[3]/center/input[1]')
searchbutton.click()


