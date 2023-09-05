import csv
from selenium import webdriver

# Set the URL of the website you want to scrape
url = "https://tommyhilfiger.nnnow.com/tommy-hilfiger-men-tshirts"

# Create a new Chrome web driver
chrome_driver_path = r"C:\Users\Dell\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigate to the website
driver.get(url)

# Find all the links to T-shirts
t_shirt_links = driver.find_elements_by_css_selector("a.nw-productview nwc-anchortag")

# Create a list to store the data we scraped
t_shirts = []

# Iterate over the T-shirt links and scrape the data
for link in t_shirt_links:
    # Navigate to the T-shirt page
    driver.get(link)

    # Get the name of the T-shirt
    t_shirt_name = driver.find_element_by_css_selector("div.nw-productview-producttitle").text

    # Get the price of the T-shirt
    t_shirt_price = driver.find_element_by_css_selector("span.nw-priceblock-amtnw-priceblock-sellingpriceis-having-discount").text

    # Remove the currency symbol from the price
    t_shirt_price = t_shirt_price.replace("Rs.", "")

    # Create a dictionary to store the data for each T-shirt
    t_shirt = {
        "link": link,
        "name": t_shirt_name,
        "price": t_shirt_price
    }

    # Add the dictionary to the list of T-shirts
    t_shirts.append(t_shirt)

# Save the data to a CSV file
with open("t_shirts.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["link", "name", "price"])
    for t_shirt in t_shirts:
        csvwriter.writerow(t_shirt.values())

# Close the web driver
driver.close()