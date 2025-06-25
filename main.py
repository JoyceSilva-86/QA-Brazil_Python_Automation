import time
import data
import helpers
from data import PHONE_NUMBER

from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)

        WebDriverWait(self.driver, 2).until(lambda d: True)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        WebDriverWait(self.driver, 2).until(lambda d: True)
        assert routes_page.get_from_location_value() == data.ADDRESS_FROM
        assert routes_page.get_to_location_value() == data.ADDRESS_TO

        time.sleep(5)


    def test_select_plan(self):
       self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 2).until(lambda d: True)
        routes_page.click_taxi_option()
        WebDriverWait(self.driver, 2).until(lambda  d: True)
        routes_page.click_comfort_icon()
        WebDriverWait(self.driver, 2).until(lambda d: True)
        assert routes_page.click_comfort_active()
        time.sleep(5)

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 2).until(lambda d: True)
        routes_page.click_taxi_option()
        WebDriverWait(self.driver, 2).until(lambda d: True)
        routes_page.click_comfort_icon()
        WebDriverWait(self.driver, 2).until(lambda d: True)
        routes_page.click_number_text(data,PHONE_NUMBER)
        WebDriverWait(self.driver, 2).until(lambda d: True)
        assert data.PHONE_NUMBER in routes_page.number_confirm()
        time.sleep(5)

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 2).until(lambda d: True)
        routes_page.click_taxi_option()
        WebDriverWait(self.driver, 2).until(lambda d: True)
        routes_page.click_comfort_icon()
        WebDriverWait(self.driver, 2).until(lambda d: True)
        routes_page.click_add_card(data.CARD_NUMBER, data.CARD_CODE)
        WebDriverWait(self.driver, 2).until(lambda d: True)
        assert "Cartão" in routes_page.confirm_card
    def test_comment_for_driver(self):
        # Adicionar em S8
        print("função criada para definir o motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("função criada para definir pedido de cobertor")
        pass

    def test_order_2_ice_creams(self):
        # Adicionar em S8
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            print("função criada para definir pedido de sorvete")
        pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("função criada para definir modelo de carro")
        pass


