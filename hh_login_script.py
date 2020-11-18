import time
from threading import Thread
from selenium import webdriver #подключение библиотеки автоматизированного управления браузером
from selenium.webdriver.common.keys import Keys #подключение инструмента клавиш
from selenium.webdriver.common.by import By #импорт  поддерживаемых локаторов для поиска по странице
from selenium.webdriver.support import expected_conditions as EC #импорт инструмента распознавания ожидаемых условий

driver = webdriver.Firefox()
driver.get('https://hh.ru/account/login?backurl=%2F')

class InputData():
    def login(self):
        loginInput = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/form/div[1]/input")
        loginInput.send_keys('MAIL')
    
    def password(self):
        passwordInput = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/form/div[2]/span/input")
        passwordInput.send_keys('PASSWORD')

    def submitButton(self):
        driver.implicitly_wait(1)
        button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/form/div[4]/button")
        button.click()
            
    def runall(self):
        if __name__ == '__main__':
            Thread(target = self.login).start()
            Thread(target = self.password).start()
            Thread(target = self.submitButton).start()
     
    
run = InputData()
run.runall()

