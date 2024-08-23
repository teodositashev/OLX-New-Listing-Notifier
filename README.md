# OLX-New-Listing-Notifier

The OLX-New-Listing-Notifier script is designed to alert you about new OLX listings at regular intervals via email. To get started, you'll need a Gmail account to send the notifications. Below is a quick setup guide.

## 1. Install Dependencies

Open your command prompt and run the following commands to install the necessary Python libraries:

```bash
pip install beautifulsoup4
pip install pyyaml
```

## 2. Configure `config.yaml`

In the `config.yaml` file, you will need to specify the following:

- **link**: Your OLX search query.
- **time_interval**: The interval (in minutes) at which you want to be notified.
- **sender_email**: The Gmail account that will send the notifications.
- **receiver_email**: The email account (which can be any email provider) where you want to receive notifications.

## 3. Setting Up Your Gmail

To securely store your email password and avoid potential security risks, follow these steps:

1. **Enable 2-Step Verification**:
   - Go to [myaccount.google.com](https://myaccount.google.com), click on Security, and enable 2-Step Verification.

2. **Create an App Password**:
   - After enabling 2-Step Verification, visit [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).
   - Generate a new App Password. You can name the app anything you like (e.g., OLX Notifier).
   - Copy the 16-character password provided.

3. **Set Up a System Variable**:
   - Create a system environment variable named `OLX_NOTIFIER_PASSWORD` with the value set to the App Password you copied.
   - Restart your IDE to apply the changes.

