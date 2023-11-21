from selenium import webdriver
from time import sleep
import os
from create_dir_name import dir_save
from generate_name import generate_name
from create_list_website import create_list


print('----------------Ok Vamos gerar seus Screen-shots----------------')
quantity = int(
    input('Digite a quantidade de sites que precisa do screenshot? '))

list_sites = create_list(quantity)

browser = webdriver.Chrome()


for site in list_sites:
    browser.get(site)
    browser.execute_script('document.body.style.overflow = "hidden";')
    sleep(4)
    screenshot_filename = generate_name(site)
    path_save = dir_save()
    browser.get_screenshot_as_file(
        os.path.join(path_save, screenshot_filename))
    print(f" Salvando screenshot como: {screenshot_filename}")

browser.quit()
print("...finalizou")
