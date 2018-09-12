from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#ojo deben descargar el driver para xu sistema operativo
reemail = 'juanzjck1996@gmail.com'


browser = webdriver.Chrome('/Users/juansalazar/Documents/IdPayerAPi/bot/autologinbot/chromedriver')
browser.get(('file:///Users/juansalazar/Documents/IdPayerAPi/bot/index.html'))

# fill in campo and hit the next button

campo = browser.find_element_by_id('PayboxRemail')
campo.send_keys(reemail)
campo = browser.find_element_by_id('PayboxSendmail')
campo.send_keys(reemail)

campo = browser.find_element_by_id('PayboxRename')
campo.send_keys(reemail)

campo = browser.find_element_by_id('PayboxSendname')
campo.send_keys(reemail)

campo = browser.find_element_by_id('PayboxAmount')
campo.send_keys(20)

campo = browser.find_element_by_id('PayboxDescription')
campo.send_keys("prueba")

nextButton = browser.find_element_by_id('pay')
nextButton.click()


# wait for transition then continue to fill items

# WebDriverWait(browser, 10).until( EC.presence_of_element_located((By.NAME, "password")))



signInButton = browser.find_element_by_id('completar')
signInButton.click()





