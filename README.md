# OLX-New-Listing-Notifier

There are 2 ways to save the password for your email in the file:

1. **The first way (NOT RECOMMENDED)** is by assigning your Gmail password to the `email_password` variable. This method is not recommended because if you upload the code anywhere, you risk leaking your email password.

2. **The second way (RECOMMENDED)** takes a little bit more time to set up, but it is far more secure:
   - Go to [myaccount.google.com](https://myaccount.google.com), then click on **Security** and turn on **2-Step Verification**.
   - After turning on 2-Step Verification, go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords) and create a new App Password.
   - Name the app you will be using however you like (e.g., *OLX Notifier*).
   - You will be given a 16-letter password that you need to copy.
   - Create a **System Variable** (Google how to do this on your OS) with the name `OLX_NOTIFIER_PASSWORD` and the value of the password you have copied.
   - Restart your IDE, and you are good to go.
