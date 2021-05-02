
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def getDriver():
    # ヘッドレスモードOFF
    # driver = webdriver.Chrome(ChromeDriverManager().install())

    # ヘッドレスモードON
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    return driver
