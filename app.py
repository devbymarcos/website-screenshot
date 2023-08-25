from selenium import webdriver
from time import sleep

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
    slice_one = site[8:]
    slice_end = slice_one[0:-5]
    screenshot_filename = slice_end + ".png"
    browser.get_screenshot_as_file(screenshot_filename)
    print(f" Salvando screenshot como: {screenshot_filename}")

browser.quit()
print("...finalizou")
