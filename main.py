# Main PNR Scrapping Function
from driver import PnrScrapper


def main():
    """Main PNR Scrapping Function"""

    print("Welcome to PNR Scrapping")
    scrapper = PnrScrapper(8912597236)
    scrapper.enter_pnr_and_open_captcha_modal_condition()
    scrapper.handle_captcha_image()


if __name__ == "__main__":
    main()
