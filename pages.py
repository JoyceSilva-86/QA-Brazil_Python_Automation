from html.parser import commentclose
from logging import exception

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
from helpers import retrieve_phone_code
import time

class UrbanRoutesPage:
    #Seção DE e PARA
from_field = (By.ID, 'from')
to_field = (By.ID, 'to')

taxi_option_locator = (By.XPATH, '//button[contains(text(),"Chamar")]')
comfort_icon_locator = (By.XPATH, '//im[@src="/static/media/kids.875fd8d4.sgv"]')
comfort_active = (By.XPATH, '//*[@id="root"/div/div[3]/div[3]/div[2]/div[1]/div[5]')

number_text_locator = (By.CSS_SELECTOR, '.np-button')
number_enter = (By.ID, 'phone')
number_confirm = (By.CSS_SELECTOR, '.button.full')
number_code = (By.ID, 'code')
code_confirm = (By.XPATH, '//button[contains(text(),"Confirmar")]')
number_finish = (By.CSS_SELECTOR, '.np-text')

add_metodo_pagamento = (By.CSS_SELECTOR, '.np-button')
add_card = (By.CSS_SELECTOR, '.pp-plus')
number_card = (By.ID, 'number')
code_card = (By.CSS_SELECTOR, 'input.card-input#code')
add_finish_card = (By.XPATH, '//button[contains(text(),"Adicionar")]')
close_button_card = (By.CSS_SELECTOR, '.payment-picker.open .close-button')
confirm_card = (By.CSS_SELECTOR,'.pp-value-text')

add_comment = (By.ID, 'Comment')
switch_blanquet = (By.CSS_SELECTOR, '.switch')
switch_blaquet_active = (By.CSS_SELECTOR, '#root > div') #terminar

add_icecream = (By.CSS_SELECTOR, '.counter-plus')
qnt_icecream = (By.CSS_SELECTOR, '.counter-value')
call_taxi_button = (By.CSS_SELECTOR, '.smart-button')
pop-up = (By.CSS_SELECTOR, '.order-header-title')


def __init__(self, driver):
    self.driver = driver

def enter_from_location(self, from_text):
    WebDriverWait(self.driver, 3).until(Ec.visibility_of_element_located(self.from_field))
    self.driver.find_element(*self.from_field).send_keys(from_text)

def enter_to_location(self, to_text):
    WebDriverWait(self.driver, 3).until(Ec.visibility_of_element_located(self.to_field))
    self.driver.find_element(*self.to_field).send_keys(to_text)

def enter_locations(self, from_text, to_text):
    self.enter_from_location(from_text)
    self.enter_to_location(to_text)

def get_from_location_value(self):
    return WebDriverWait(self.driver, 3).until(Ec.visibility_of_element_located(self.from_field).get_attribute('value')

def get_to_location_value(self):
    return WebDriverWait(self.driver, 3).until(Ec.visibility_of_element_located(self.to_field).get_attribute('value')

def click_taxi_option(self):
    self.driver.find_element(*self.taxi_option_locator).click()

def click_comfort_icon(self):
    self.driver.find_element(*self.comfort_icon_locator).click()

def click_comfort_active(self):
    try:
    active_button = WebDriverWait(self.driver, 10).until(Ec.visibility_of_element_located(self.comfort_active))
    return "active" in active_button.get_attribute("class")
    except:
    return False

def click_number_text(self, telefone):
    self.driver.find_element(*self.number_text_locator).click()
    self.driver.find_element(*self.number_enter).send_keys(telefone)
    self.driver.find_element(*self.number_confirm).click()

    code = retrieve_phone_code(self.driver)
    code_input = WebDriverWait(self.driver, 3).until(Ec.visibility_of_element_located(self.number_code))

