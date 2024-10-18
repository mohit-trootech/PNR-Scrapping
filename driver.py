from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from constants import *
from image_processing import CaptchaImageFiltering
from time import sleep


class PnrScrapper:
    """Scrapper Class Implemented for PNR Scrapping"""

    def __init__(self, pnr: int):
        self.driver = webdriver.Firefox()
        self.create_driver()
        self.pnr = pnr
        self.pnr_input = self.find_element_by_id(PNR_INPUT)
        self.capcha_modal_btn = self.find_element_by_id(CAPTCHA_MODAL)
        self.captcha = None

    def create_driver(self):
        """Create Driver Instance for PNR Scrapping"""
        self.driver.get(PNR_SCRAPPER)

    def fetch_required_elements(self):
        """Fetch Required Elements"""

    def find_element_by_id(self, ID):
        """Fetch Elements with IDs"""
        return self.driver.find_element(By.ID, ID)

    def get_tag_name(self, element):
        """Return Element tag name"""
        return element.tag_name

    def get_element_attribute(self, element, attribute):
        """Return Element Attribute"""
        return element.get_attribute(attribute)

    def enter_pnr_and_open_captcha_modal_condition(self):
        """Check Conditions for PNR Scrapping"""
        if self.get_tag_name(self.pnr_input) == INPUT and self.get_element_attribute(
            self.pnr_input, TYPE
        ) in [TEXT, NUMBER]:
            if (
                self.get_tag_name(self.capcha_modal_btn) == INPUT
                and self.get_element_attribute(self.capcha_modal_btn, TYPE) == BUTTON
            ):
                self.pnr_input.send_keys(self.pnr)
                self.capcha_modal_btn.click()
                if self.capcha_modal_btn.is_displayed():
                    print("Captcha Modal Opened")
        else:
            print("Invalid Input")

    def handle_captcha_image(self):
        """Handle Captcha Image"""
        image = self.find_element_by_id(CAPTCHA_IMAGE)
        sleep(2)
        self.driver.save_screenshot(PAGE_SS)
        sleep(2)
        filter = CaptchaImageFiltering(image)
        solved_captcha = filter.get_solved_capcha_from_image()
        captcha_input = self.find_element_by_id(INPUT_CACHE)
        captcha_input.send_keys(solved_captcha)
        captcha_submit = self.find_element_by_id(CAPTCHA_SUBMIT)
        captcha_submit.click()


if __name__ == "__main__":
    pass
