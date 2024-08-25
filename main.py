import os
import time
from typing import List, Tuple, Union

from config_loader import load_config
from email_sender import create_email, send_email
from scraper import scrape_info

def process_lists(new_ads: List[Tuple[str, str, str]], old_ads: List[Tuple[str, str, str]]) -> List[Tuple[str, str, str]]:
    """Filter new ads that are not in the list of old ads."""

    old_orders_links = {tup[2] for tup in old_ads}

    filtered_orders = [tup for tup in new_ads if tup[2] not in old_orders_links]
    return filtered_orders

def create_subject(time: int) -> str:
    """Generate a dynamic email subject based on alert frequency."""

    if (time == 1):
        suffix = "in the last minute."
    else:
        suffix = f"in the last {time} minutes."

    return f"Check out the new listings uploaded on OLX {suffix}"
    
def main() -> None:
    config = load_config()
    
    link_to_scrape = config['link']
    sender_email = config['sender_email']
    receiver_email = config['receiver_email']
    alert_frequency = config['time_interval']
    email_password = os.environ.get("OLX_NOTIFIER_PASSWORD")

    if (email_password == None):
        raise EnvironmentError("There was a problem loading the email password from the environment variable.")
    
    subject = create_subject(alert_frequency)

    old_ads = []

    while True:
        new_ads = scrape_info(link_to_scrape)

        possibly_new = process_lists(new_ads, old_ads)
        if (possibly_new != []):
            email = create_email(sender_email, receiver_email, subject, possibly_new)
            send_email(email, sender_email, email_password)
            print("Email sent successfully!")
        else:
            print("No new ads found.")

        old_ads = new_ads

        time.sleep(alert_frequency * 60)

if __name__ == "__main__":
    main()