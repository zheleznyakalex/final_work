from urllib.parse import urlparse

class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объекты веб-драйвера, адрес страницы и время ожидания элементов
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

        # self.driver.implicitly_wait(timeout) задаёт максимальное время ожидания в секундах,
        # в течении которого WebDriver пытается найти элемент, если он недоступен сразу же.

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path
    # даёт текущий адрес страницы без привязки к домену

    def wait_for_animation(web_browser, selector):
        """
        Waits until jQuery animations have finished for the given jQuery  selector.
        """
        WebDriverWait (web_browser, 10).until (lambda web_browser: browser.execute_script (
            'return jQuery(%s).is(":animated")' % json.dumps (selector))
                                                                   == False)

    def wait_for_ajax_loading(web_browser, class_name):
        """
        Waits until the ajax loading indicator disappears.
        """
        WebDriverWait (web_browser, 10).until (lambda web_browser: len (web_browser.find_elements_by_class_name (
            class_name)) == 0)