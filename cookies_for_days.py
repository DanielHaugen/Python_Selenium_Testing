# pip install msedge-selenium-tools selenium
from platform import architecture
from msedge.selenium_tools import Edge, EdgeOptions
from datetime import datetime as dt
import time

def get_time() -> str:
    return dt.now().strftime("%Y-%m-%d %H:%M:%S") + " -"

def main():
    # Find edge version at edge://settings/help
    # Version tested: Version 93.0.961.38 (Official build) (64-bit)
    # Official drivers can be downloaded at: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    edge_driver = 'edgedriver_win64\msedgedriver.exe'

    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("-inprivate")
    driver = Edge(executable_path = edge_driver, options = options)
    # Navigate to URL
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    # Wait for resources to load on webpage
    driver.implicitly_wait(5)

    """ Current Variables """
    # Main cookie to click for points
    cookie = driver.find_element_by_id('bigCookie')
    # Current price of upgrades using list comprehension
    products = set(driver.find_elements_by_class_name("product"))
    upgrades_section = driver.find_element_by_id('upgrades')
    
    check_upgrades = False
    while True:
        cookie.click()
        
        for product in products:
            try:
                tmp_classes = product.get_attribute('class').split()
                if 'enabled' in tmp_classes:
                    time.sleep(0.1)
                    # click an upgrade
                    product.click()
                    check_upgrades = True   
            except:
                products.remove(product)
                check_upgrades = True
                break # Can't continue to iterate on size change, so break
            
        
        if check_upgrades:
            for upgrade in driver.find_elements_by_class_name("crate.upgrade"):
                products.add(upgrade)
                check_upgrades = False
            print(get_time(), len(products))

if __name__ == "__main__":
    main()
