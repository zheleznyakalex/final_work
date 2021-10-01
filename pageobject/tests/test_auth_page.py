from pages.auth_page import AuthPage
import time

def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    page.enter_email("nerone.atreyo@gmail.com")
    page.enter_pass("rohexa98")
    page.btn_click()

    assert page.get_relative_link() == '/all_pets', "login error"

    time.sleep(4)


# запуск теста в терминале: python -m pytest -v --driver Chrome --driver-path C:/Webdrivers/chromedriver.exe