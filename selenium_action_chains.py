# pip install msedge-selenium-tools selenium
from platform import architecture
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.action_chains import ActionChains
import time

def main():
    # Find edge version at edge://settings/help
    # Version tested: Version 93.0.961.38 (Official build) (64-bit)
    # Official drivers can be downloaded at: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    edge_driver = 'edgedriver_win64\msedgedriver.exe'

    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("-inprivate")
    driver = Edge(executable_path = edge_driver, options = options) # Modify the path here...
    # Navigate to URL
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    # Wait for resources to load on webpage
    driver.implicitly_wait(5)

    # Instantiation of action constructor
    actions = ActionChains(driver)
    """ Current Variables """
    # Main cookie to click for points
    cookie = driver.find_element_by_id('bigCookie')
    # Current number of cookies
    cookie_count = driver.find_element_by_id('cookies')
    # Current price of upgrades using list comprehension
    items = [driver.find_element_by_id('productPrice' + str(i)) for i in range(1, -1, -1)]
    # Click the main cookie
    actions.click(cookie)
    
    for i in range(5000):
        actions.perform()
        # time.sleep(0.01)
        count = int(cookie_count.text.split(' ')[0])
        # print(count)
        for item in items:
            value = int(item.text.replace(',',''))
            # If upgrade cost is less than current balance
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()


if __name__ == "__main__":
    main()
