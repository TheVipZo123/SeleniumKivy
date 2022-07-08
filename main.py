# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium.webdriver.common.by import By
import docx
import Word
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
list_of_lists_of_pages = []
number = int(Word.list_of_list[2])


driver = webdriver.Chrome(executable_path='C:/Users/Samsung/Documents/chromedriver_win32/chromedriver.exe')
driver.set_window_size(1120, 550)
driver.get("https://google.com.br/")
a = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
a.send_keys(Word.list_of_list[0] + " " + Word.list_of_list[1])
driver.implicitly_wait(5000)
a.submit()
while number != 0:
    driver.implicitly_wait(5000)
    c = (driver.find_element_by_tag_name("body").text)
    # print(driver.find_element_by_tag_name("body").text)
    list_of_lists_of_pages += [c]
    driver.implicitly_wait(5000)
    if number != 1:
        driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div/div[4]/div/div[3]/table/tbody/tr/td[12]/a/span[2]").click()
        driver.implicitly_wait(5000)
    number = number - 1
driver.quit()
Novo_Documento = docx.Document()
num = 0
while len(list_of_lists_of_pages) > num:
    Novo_Documento.add_paragraph(list_of_lists_of_pages[num])
    num = num + 1
Novo_Documento.save('File D '+ Word.list_of_list[0] + " " + Word.list_of_list[1] + '.docx')