from selenium import webdriver

username = "hasnae.bilil@gmail.com"
password = "Ihsane1986!"

url = "https://github.com/login"

driver = webdriver.Chrome("C:/Users/hasna/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_id("login_field").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_name("commit").click()


print("logged in sucessefully")


