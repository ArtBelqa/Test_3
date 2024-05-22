from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.maximize_window()
    driver.get("https://www.roseltorg.ru/")

    wait = WebDriverWait(driver, 5)

    # Перейти в раздел 44-ФЗ
    section_44fz = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.menu__link[href="/search/44fz"]')))
    section_44fz.click()

    # Найти тендер по номеру 0372200286524000027
    search_field = driver.find_element(By.CSS_SELECTOR, 'input.search-autocomplete__keywordinput-light')
    search_field.send_keys("0372200286524000027")
    search_field.send_keys(Keys.RETURN)

    time.sleep(2)

    # Перейти на страницу с тендером 0372200286524000027
    tender_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.search-results__link[href="/procedure/0372200286524000027"]')))
    tender_link.click()

    time.sleep(3)

    # Нажать на кнопку «Подать заявку»
    apply_button = driver.find_element(By.CSS_SELECTOR,'a.button.button--large.button--blue.button--main-action.procedura-podat-zayavku')
    apply_button.click()

    time.sleep(5)

    # Нажать на кнопку «Продолжить работу»
    continue_button = driver.find_element(By.CSS_SELECTOR,'a.button.button--blue[href="https://gos.roseltorg.ru/#procedures"]')
    continue_button.click()

    time.sleep(10)

finally:
    driver.quit()
