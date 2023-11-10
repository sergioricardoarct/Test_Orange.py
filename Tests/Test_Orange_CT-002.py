from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(4)
driver.maximize_window()

# login
driver.find_element(By.XPATH, '//*[@name="username"]').send_keys('Admin')
driver.find_element(By.XPATH, '//*[@name="password"]').send_keys('admin123')
driver.find_element(By.XPATH, '//*[@type="submit"]').click()
dashgbord = driver.find_element(By.CSS_SELECTOR, 'span h6 ')
assert dashgbord.is_displayed()

# click pim
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
driver.find_element(By.XPATH, '//*[@class="oxd-button oxd-button--medium oxd-button--secondary"]').click()

# preencher funci e copiar id
driver.find_element(By.XPATH, '//*[@name="firstName"]').send_keys('Sergio')
driver.find_element(By.XPATH, '//*[@name="middleName"]').send_keys('Ricard')
driver.find_element(By.XPATH, '//*[@name="lastName"]').send_keys('Nas')

# copiar Id

driver.find_element(By.CSS_SELECTOR,
                    'div.oxd-grid-2.orangehrm-full-width-grid > div > div > div:nth-child(2) > input').click()
ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
driver.find_element(By.XPATH, '// button[@type="submit" ]').click()

validacao1 = driver.find_element(By.CSS_SELECTOR, 'div.oxd-topbar-header-title h6.oxd-text')
assert validacao1.is_displayed()

# zerar lista
driver.find_element(By.XPATH, '//a[contains(text(),"Employee List")]').click()
# driver.find_element(By.XPATH,'//i[@class="oxd-icon bi-caret-up-fill"]').click()    - se a tela não maximizar
driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > input').click()
ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

driver.find_element(By.XPATH,
                    '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]').click()
id_pesquisa = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div > span').text
resulrado = '(1) Record Found'
assert id_pesquisa == resulrado
#feito