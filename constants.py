# PNR Scrapping Constants Required for Scrapping and Logical Analysis
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))

# Required Urls
PNR_SCRAPPER = "https://www.indianrail.gov.in/enquiry/PNR/PnrEnquiry.html"

# Element IDs
PNR_INPUT = "inputPnrNo"
CAPTCHA_MODAL = "modal1"
CAPTCHA_IMAGE = "CaptchaImgID"
CAPTCHA_SUBMIT = "submitPnrNo"
INPUT_CACHE = "inputCaptcha"


# Element & Types Required
INPUT = "input"
BUTTON = "button"
IMAGE = "img"
SRC = "src"
TEXT = "text"
TYPE = "type"
NUMBER = "number"
SUBMIT = "submit"
CAPTCHA_IMAGE_TEMPORARY = path.join(BASE_DIR + "/static/", "captcha.png")
PAGE_SS = path.join(BASE_DIR + "/static/", "screenshot.png")
