import os
from config_loader import load_config
from scraper import scrape_info
from email_sender import create_email, send_email

def main():
    config = load_config()
    
    #TODO validate the data (sort link by newest if it hasnt been done, regex check if sender is gmail, receiver is email, if site isnt olx, if env. var isnt setup)
    link_to_scrape = config['link']
    sender_email = config['sender_email']
    receiver_email = config['receiver_email']
    alert_frequency = config['time_interval']
    email_password = os.environ.get("OLX_NOTIFIER_PASSWORD")
    
    scraped_info = scrape_info(link_to_scrape)
    
    #TODO change it to be a loop every alert_frequency seconds, check if there is an intersection of old and new listings and if there is none
    #then go to 2nd page of the search
    if scraped_info:
        subject = "Check out the new listings uploaded on OLX"      #add in the last 1min or minutes depending on if its 1 or less
        email = create_email(sender_email, receiver_email, subject, scraped_info)
        send_email(email, sender_email, email_password)
        print("Email sent successfully!")
    else:
        print("No new ads found.")

if __name__ == "__main__":
    main()
