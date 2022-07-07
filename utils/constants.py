from selenium import webdriver


def chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    return options


browsers_list = {
    "CHROME": chrome_options(),
    "FIREFOX": webdriver.FirefoxOptions()
}
