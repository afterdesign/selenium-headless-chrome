"""
Chrome headless simple test
"""

from selenium import webdriver


def remote_chrome_webdriver_setup():
    """
    Create Chrome driver.

    :rtype: WebDriver
    """

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    chrome_capabilities = options.to_capabilities()

    driver = webdriver.Remote(
        command_executor='http://192.192.1.201:4444/wd/hub',
        desired_capabilities=chrome_capabilities
    )
    return driver


def grab_screenshot(driver):
    """
    Grab screenshot

    :param WebDriver driver: Remote webdriver object
    """
    driver.get('http://afterdesign.net')
    driver.implicitly_wait(10)
    driver.get_screenshot_as_file('main-page.png')


if __name__ == '__main__':
    grab_screenshot(
        remote_chrome_webdriver_setup()
    )
