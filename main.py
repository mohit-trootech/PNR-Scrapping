# Main PNR Scrapping Function
from driver import PnrScrapper
from test import *
import csv
from time import sleep
from selenium.webdriver.common.by import By
from pnr_scrapping.constants import BASE_DIR
from os.path import join


def main():
    """Main PNR Scrapping Function"""
    try:
        print("Welcome to PNR Scrapping")
        pnr_number = 8624468621  # Replace with the actual PNR number
        scrapper = PnrScrapper(pnr_number)
        scrapper.enter_pnr_and_open_captcha_modal_condition()
        scrapper.handle_captcha_image()

        # Wait for the results to load (adjust time as needed)
        sleep(5)

        pnr_output_div = scrapper.driver.find_element(By.ID, "pnrOutputDiv")

        # Extract data from the journey details table
        journey_details_table = pnr_output_div.find_element(
            By.ID, "journeyDetailsTable"
        )
        journey_details_rows = journey_details_table.find_elements(By.TAG_NAME, "tr")[
            1:
        ]  # Skip header row

        journey_data = []
        for row in journey_details_rows:
            (
                train_number,
                train_name,
                boarding_date,
                frm,
                to,
                reserved_upto,
                boarding_point,
                class_,
            ) = row.find_elements(By.TAG_NAME, "td")
            journey_data.append(
                {
                    "train_number": train_number.text,
                    "train_name": train_name.text,
                    "boarding_date": boarding_date.text,
                    "from": frm.text,
                    "to": to.text,
                    "reserved_upto": reserved_upto.text,
                    "boarding_point": boarding_point.text,
                    "class": class_.text,
                }
            )

        # Extract data from the passenger details table
        passenger_details_table = pnr_output_div.find_element(By.ID, "psgnDetailsTable")
        passenger_details_rows = passenger_details_table.find_elements(
            By.TAG_NAME, "tr"
        )[
            1:
        ]  # Skip header row

        passenger_data = []
        for row in passenger_details_rows:
            (
                passenger_number,
                booking_status,
                current_status,
                coach_position,
            ) = row.find_elements(By.TAG_NAME, "td")
            passenger_data.append(
                {
                    "passenger_number": passenger_number.text,
                    "booking_status": booking_status.text,
                    "current_status": current_status.text,
                    "coach_position": coach_position.text,
                }
            )

        # Extract data from the other details table
        other_details_table = pnr_output_div.find_element(By.ID, "otherDetailsTable")
        other_details_row = other_details_table.find_elements(By.TAG_NAME, "tr")[
            1
        ]  # Only one row

        (
            total_fare,
            charting_status,
            remarks,
            train_status,
        ) = other_details_row.find_elements(By.TAG_NAME, "td")
        other_data = {
            "total_fare": total_fare.text,
            "charting_status": charting_status.text,
            "remarks": remarks.text,
            "train_status": train_status.text,
        }

        # Combine data into a single list of dictionaries
        all_data = journey_data + passenger_data + [other_data]

        # Define CSV headers
        csv_headers = [
            "train_number",
            "train_name",
            "boarding_date",
            "from",
            "to",
            "reserved_upto",
            "boarding_point",
            "class",
            "passenger_number",
            "booking_status",
            "current_status",
            "coach_position",
            "total_fare",
            "charting_status",
            "remarks",
            "train_status",
        ]

        # Write data to CSV file
        with open(
            join(BASE_DIR + "/data.csv", "pnr_details.csv"),
            "w",
            newline="",
            encoding="utf-8",
        ) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
            writer.writeheader()
            writer.writerows(all_data)

    except Exception as e:
        print(e)
        error = scrapper.driver.find_element(By.ID, "errorMessage")
        if error:
            print(error.get_attribute("innerHTML"))
        else:
            print(e)


if __name__ == "__main__":
    from time import time

    before = time()
    main()
    after = time()
    print(f"Pnr Fetched in {after - before:.6f}")
