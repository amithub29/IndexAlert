#Index Alert

It sends Sensex and Nifty updates to specified phone numbers via Whatsapp.

## Dependencies

### External Packages
- `twilio`: Required for sending SMS messages using the Twilio API.
- `dotenv`: Required for loading environment variables from a .env file.

### Built-in Modules
- `os`: Provides functions for interacting with the operating system.
- `urllib.request`: Provides functions for working with URLs and making HTTP requests.
- `re`: Provides support for regular expressions.


## Configuration

### Environment Variables

This application requires certain environment variables to be set in order to function properly. These variables are typically stored in a `.env` file located in the root directory of the project.

### Creating the `.env` File

To set up the `.env` file, follow these steps:

1. Create a new file named `.env` in the root directory of the project.
2. Open the `.env` file in a text editor.
3. Copy and paste the following template into the `.env` file:

```plaintext
# Sample .env file content
account_id=YOUR_TWILIO_ACCOUNT_ID
auth_token=YOUR_TWILIO_AUTH_TOKEN
from_number=whatsapp:+1234567890
to_number=whatsapp:+9876543210
