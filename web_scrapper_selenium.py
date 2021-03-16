from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)

path = "https://www.buycarparts.co.uk/audi/a6-allroad-4ah-c8/136391"
driver.get(path)

main = driver.find_element_by_class_name("all-autoparts")
main_text = main.text

list_text = list(main_text.split('\n'))
last_index = list_text.index("LIGHTING") + 1
list_text = list_text[:last_index]


def get_price(driver):
    try:
        price = driver.find_element_by_class_name("price").text
        price_clean = price.replace("£ ", "").replace(",", ".")
        return price_clean

    except:
        print("Couldn't scrape the price")
        return ""


def navigate_by_word(_driver, word):
    _link = _driver.find_element_by_link_text(word)
    driver.execute_script("arguments[0].click();", _link)
    #_link.click()
    time.sleep(5)


def navigate_by_word_wait(_driver, word):
    try:
        _link = WebDriverWait(_driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, word))
        )
        _link.click()
    finally:
        driver.quit()


def navigate_home():
    driver.get(path)
    time.sleep(1)


def multiple_parts():
    try:
        text = driver.find_element_by_class_name("filter-accessories__title").text
        if "choose a specific" in text or "select product group" in text:
            return True
        else:
            return False

    except:
        return False


def get_price_multiple_parts(el, subel):
    _results = []
    _filters = driver.find_elements_by_class_name("filter-accessories__items-item")
    _path = driver.current_url
    for i in range(len(_filters)):
        _aux = driver.find_elements_by_class_name("filter-accessories__items-item")
        _fil = _aux[i]
        _text = _fil.text
        print(_text)
        if "Show all" in _text:
            print("Show all statement")
        else:
            try:
                _fil.click()
                time.sleep(5)
                _results.append([el, subel, _text, get_price(driver)])
                driver.get(_path)
                time.sleep(5)

            except:
                print("Couldn't scrape: {}".format(_text))

    return _results


results = []

for element in list_text:
    print("Scraping main element {}".format(element))
    navigate_by_word(driver, element)
    current_url = driver.current_url
    system = element

    if current_url == path:
        subsystems = driver.find_element_by_id('selected_custom_subcategory')
        list_subsystems = subsystems.text.split('\n')
        list_subsystems = list_subsystems[12:]

        for subelement in list_subsystems:

            #if 'tools' in subelement or 'repair' in subelement:
            if False:
                pass
            else:
                print(subelement)
                try:
                    navigate_by_word(driver, subelement)
                    if multiple_parts():
                        print(True)
                        aux_results = get_price_multiple_parts(element, subelement)
                        for x in aux_results:
                            results.append(x)

                    else:
                        results.append([element, subelement, "", get_price(driver)])

                except:
                    print("\n\nException on subelement {}, Main system: {}".format(subelement, element))

            navigate_home()
            navigate_by_word(driver, element)

    else:
        try:
            results.append([element, "", "", get_price(driver)])
            #print("Main element {}, subelement {}, Price {}".format(element, element, get_price(driver)))

        except:
            print("\n\nException on element {}" .format(element))

        navigate_home()

    print("{} scraped\n".format(element))


df = pd.DataFrame(data=results, columns=["element", "subelement", "specific part", "price"])
df.to_csv("raw_data.csv", index=False)

driver.quit()
