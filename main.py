from selenium import webdriver

username = "your email"
password = "your password"

url = "https://auth.udacity.com/sign-in"

driver = webdriver.Chrome("C:/Users/hasna/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("revealable-password").send_keys(password)
driver.find_element_by_css_selector(".vds-form-fieldset>:last-child>:last-child").click()


print("logged in sucessefully")



