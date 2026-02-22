import gspread
from google.oauth2.service_account import Credentials

# Scopes define what this automation is allowed to access
# Sheets + Drive are required to read/write spreadsheets
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Path to service account credentials
CREDS_FILE = "credentials.json"

# Spreadsheet name (must match exactly the Google Sheets name)
SHEET_NAME = "Crypto_Automation_Report"


def connect_sheet():
    """
    Authenticates using a Google Service Account and
    returns the first worksheet of the target spreadsheet.
    """

    # Load credentials from JSON key file
    credentials = Credentials.from_service_account_file(
        CREDS_FILE,
        scopes=SCOPES
    )

    # Authorize gspread client
    client = gspread.authorize(credentials)

    # Open spreadsheet by name and return the first worksheet
    sheet = client.open(SHEET_NAME).sheet1

    return sheet
