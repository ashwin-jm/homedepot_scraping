# Importing the required libraries
from selenium import webdriver
from time import sleep
from csv import writer
from selenium.webdriver.common.by import By

# Specify the full path to the ChromeDriver executable
chrome_driver_path = r"C:\Users\Dell\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()

page_url = 'https://www.homedepot.com/b/Smart-Home-Smart-Devices/N-5yc1vZ2fkp3e0'
product_links = []

while 1:
    driver.get(page_url)
    sleep(5)
    # Scrolling the page
    driver.execute_script("window.scrollTo(0, 1000)")
    sleep(5)

    # Extracting product links
    page_product_links = driver.find_elements(By.XPATH, '//div[@class="product-pod--ef6xv"]/a')
    for product in page_product_links:
        product_link = product.get_attribute('href')
        product_links.append(product_link)

    # Locating and clicking the next button
    try:
        next_button = driver.find_elements(By.XPATH, '//li[@class="hd-pagination__item hd-pagination__button"]')[-1]
        next_button.click()
        page_url = driver.current_url
    except Exception as e:
        break

# Extracting product name
def get_product_name():
    try:
        product_name = driver.find_element(By.XPATH, '//h1[@class="sui-h4-bold sui-line-clamp-unset"]').text
    except Exception as e:
        product_name = 'Not available'
    return product_name

# Extracting product price
def get_mrp():
    try:
        mrp = driver.find_elements(By.XPATH, '//div[@class="price-format__large price-format__main-price"]/span')
        mrp = mrp[1].text
    except Exception as e:
        mrp = 'Not available'
    return mrp

# Extracting product rating
def get_rating():
    try:
        rating = driver.find_elements(By.XPATH, '//div[@class="ratings-reviews__accordion-subheader"]/span')[0].text
    except Exception as e:
        rating = 'Not available'
    return rating

# Extracting number of reviews
def get_reviews():
    try:
        reviews = driver.find_elements(By.XPATH, '//div[@class="ratings-reviews__accordion-subheader"]/span')[1].text
    except Exception as e:
        reviews = 'Not available'
    return reviews

# Extracting product description
def get_desc():
    try:
        desc = driver.find_element(By.XPATH, '//ul[@class="sui-text-base sui-list-disc list list--type-square"]').text
    except Exception as e:
        desc = 'Not available'
    return desc


# Writing to a CSV File
with open('homedepot_data.csv','w',newline='', encoding='utf-8') as f:
    theWriter = writer(f)
    heading = ['product_url', 'product_name', 'mrp', 'rating', 'no_of_reviews', 'description']
    theWriter.writerow(heading)
    for product in product_links:
        driver.get(product)
        sleep(5)
        driver.execute_script("window.scrollTo(0, 1000)")
        sleep(8)
        product_name = get_product_name()
        sleep(3)
        mrp = get_mrp()
        sleep(3)
        rating = get_rating()
        sleep(3)
        no_of_reviews = get_reviews()
        sleep(3)
        desc = get_desc()
        sleep(3)
        record = [product, product_name, mrp, rating, no_of_reviews, desc]
        theWriter.writerow(record)

driver.quit()