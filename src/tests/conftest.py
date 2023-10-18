from selenium import webdriver
import pytest


# @pytest.fixture
# def driver():
#     _driver = webdriver.Chrome()
#     _driver.implicitly_wait(5)
#     yield _driver
#     _driver.quit()


# @pytest.fixture()
# def setup(request):
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(5)
#     request.cls.driver = driver
#     before_failed = request.session.testsfailed
#     yield driver
#     if request.session.testsfailed != before_failed:
#         driver.get_screenshot_as_png()
#     driver.quit()
