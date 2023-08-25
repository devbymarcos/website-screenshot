from selenium import webdriver
from time import sleep
import uuid
from urllib.parse import urlparse


def generate_name(url):
    parsed_url = urlparse(url)
    domain = parsed_url.hostname
    unique_name = f"{domain}_{uuid.uuid1()}.png"
    return unique_name


print('----------------Ok Vamos gerar seus Screen-shots----------------')
quantity = int(
    input('Digite a quantidade de sites que precisa do screenshot? '))
sites = []

for i in range(quantity):
    item = input(f"digite o site {i+1}: ")
    if item == "":
        item = input(f"Voce não inseriu o site numero {i+1}: ")
        sites.append(item)

    else:
        sites.append(item)

browser = webdriver.Chrome()

for site in sites:
    browser.get(site)
    sleep(4)
    screenshot_filename = generate_name(site)
    browser.get_screenshot_as_file(screenshot_filename)
    print(f" Salvando screenshot como: {screenshot_filename}")

browser.quit()
print("...finalizou")
