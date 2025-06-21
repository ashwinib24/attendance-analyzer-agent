import pandas as pd
from datetime import datetime, time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# === Config ===
INPUT_FILE = 'data/raw_attendance.csv'
OUTPUT_FILE = 'output/attendance_report.csv'
NAME_COL = 'Name'
TIME_COL = 'Timestamp'

ON_TIME_LIMIT = time(9, 0)
LATE_LIMIT = time(9, 30)

# === Attendance classification logic ===
def classify_attendance(row):
    timestamp_str = row[TIME_COL]
    if pd.isna(timestamp_str) or str(timestamp_str).strip() == '':
        return 'Absent', None
    try:
        check_in = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S").time()
        if check_in <= ON_TIME_LIMIT:
            return 'Present', check_in
        elif check_in <= LATE_LIMIT:
            return 'Late', check_in
        else:
            return 'Absent', check_in
    except:
        return 'Absent', None

# === Google Sheets export ===
def export_to_google_sheet(df):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # Replace with your actual sheet ID
    sheet = client.open_by_key("1z6ewK37iOww3xA3D1SDi6Iu6rtZz_Gb1zDfNFSe1q-s").sheet1

    sheet.clear()
    df = df.fillna("")  # Convert NaN to empty strings

    sheet.insert_row(df.columns.tolist(), 1)
    for i, row in df.iterrows():
        cleaned_row = [str(cell) if isinstance(cell, (datetime, time)) else cell for cell in row.tolist()]
        sheet.insert_row(cleaned_row, i + 2)


# === Main script ===
def main():
    df = pd.read_csv(INPUT_FILE)

    results = df.apply(classify_attendance, axis=1)
    df['Status'] = results.apply(lambda x: x[0])
    df['Check-in Time'] = results.apply(lambda x: x[1] if x[1] else '—')

    df[[NAME_COL, 'Status', 'Check-in Time']].to_csv(OUTPUT_FILE, index=False)
    print(f"Attendance report generated and saved to {OUTPUT_FILE}")

    export_to_google_sheet(df)

if __name__ == "__main__":
    main()
