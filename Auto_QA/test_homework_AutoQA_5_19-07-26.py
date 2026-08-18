import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

#task1 Проверка наличия текста в iframe
PAGE_URL = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"
TARGET_TEXT = "semper posuere integer et senectus justo curabitur."

def get_firefox_options():
    options = Options()
    options.add_argument("--headless")
    return options

@pytest.fixture
def driver():
    firefox = webdriver.Firefox(options=get_firefox_options())
    yield firefox
    firefox.quit()

class TestIframeText:
    def test_text_inside_iframe(self, driver):
        driver.get(PAGE_URL)
        wait = WebDriverWait(driver, timeout=10)
        iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        driver.switch_to.frame(iframe)
        all_elements = driver.find_elements(By.CSS_SELECTOR, "*")
        matching_element = None
        for element in all_elements:
            element_text = element.get_attribute("innerText") or ""
            if TARGET_TEXT.lower() in element_text.lower():
                matching_element = element
                break
        assert matching_element is not None, (f"Элемент '{TARGET_TEXT}' не найден в iframe")
        assert matching_element.is_displayed(), ("Элемент нашелся, но не отображается на странице")
        element_text = matching_element.get_attribute("innerText") or ""
        assert TARGET_TEXT.lower() in element_text.lower(), (f"Текст элемента не совпадает.\nОжидалось: '{TARGET_TEXT}'\nПолучено:  '{element_text}'")


#task2 Тестирование Drag & Drop (Перетаскивание изображения в корзину)
PAGE_URL_DND = "https://www.globalsqa.com/demo-site/draganddrop/"
def get_firefox_options():
    options = Options()
    options.set_preference("network.proxy.type", 0)
    return options


@pytest.fixture
def driver():
    firefox = webdriver.Firefox(options=get_firefox_options())
    firefox.maximize_window()
    yield firefox
    firefox.quit()


def close_gdpr_popup(driver):
    try:
        WebDriverWait(driver, timeout=7).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if button.text.strip() in ("Соглашаюсь", "Agree", "Accept", "OK"):
                button.click()
                WebDriverWait(driver, timeout=5).until(EC.staleness_of(button))
                break
    except Exception:
        pass


def find_demo_iframe(driver):
    for iframe in driver.find_elements(By.TAG_NAME, "iframe"):
        if "photo-manager" in (iframe.get_attribute("src") or ""):
            return iframe
    return None


class TestDragAndDrop:
    def test_dragged_photo_to_trash(self, driver):
        driver.get(PAGE_URL_DND)
        wait = WebDriverWait(driver, timeout=15)
        close_gdpr_popup(driver)
        demo_iframe = wait.until(lambda d: find_demo_iframe(d))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", demo_iframe)
        wait.until(EC.visibility_of(demo_iframe))
        driver.switch_to.frame(demo_iframe)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#gallery li")))
        first_photo = driver.find_element(By.CSS_SELECTOR, "#gallery li:first-child")
        trash = driver.find_element(By.CSS_SELECTOR, "#trash")
        photos_before = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
        assert len(photos_before) == 4, (f"Ожидалось 4 фото, получили: {len(photos_before)}" )
        ActionChains(driver).drag_and_drop(first_photo, trash).perform()
        wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3)
        photos_in_gallery = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
        photos_in_trash = driver.find_elements(By.CSS_SELECTOR, "#trash li")
        assert len(photos_in_gallery) == 3, (f"В галерее должно быть 3 фото, осталось: {len(photos_in_gallery)}")
        assert len(photos_in_trash) == 1, (f"В корзине должно быть 1 фото, найдено: {len(photos_in_trash)}")
