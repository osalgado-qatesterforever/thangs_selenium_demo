from src.pages.home_page import HomePage
import logging

LOGGER = logging.getLogger(__name__)


class TestLogIn:

    def test_login(self):
        url = "https://thangs.com/"
        email = "osp11@yahoo.com"
        password = "Blablabla"

        home_page = HomePage()
        home_page.get_url(url)
        home_page.click_login_button()
        home_page.enter_email(email)
        home_page.enter_password(password)
        home_page.click_second_login()
