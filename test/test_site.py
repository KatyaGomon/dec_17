from itertools import product


import time
from pages.homepage import HomePage
from pages.product import  ProductPage


def test_open_s6(driver):
    homepage = HomePage(driver)         # driver.get("https://demoblaze.com/")
    homepage.open()
    homepage.click_galaxy_s6()    # galaxy_s6 = driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]') # galaxy_s6.click()
    product_page = ProductPage(driver)       # title = driver.find_element(By.CSS_SELECTOR, 'h2')  # assert title.text == 'Samsung galaxy s6'
    product_page.check_title_is('Samsung galaxy s6')



def test_two_monitors(driver):
    homepage = HomePage(driver)    # driver.get("https://demoblaze.com/")
    homepage.open()
    homepage.click_monitor()    # monitor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''') # monitor_link.click()
    time.sleep(2)
    homepage.check_that_products_count(2)    # monitors = driver.find_elements(By.CSS_SELECTOR, '.card') # assert len(monitors) == 2