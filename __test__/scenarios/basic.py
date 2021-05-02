def show_page(driver):
    driver.get('http://localhost:3000/')
    driver.implicitly_wait(10)


def click_account_icon(driver):
    button = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/header/div/div/button')
    button.click()
