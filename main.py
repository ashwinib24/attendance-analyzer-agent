# main.py

import pandas as pd
from datetime import datetime, time
from config import INPUT_FILE, OUTPUT_FILE, ON_TIME_LIMIT, LATE_LIMIT, NAME_COL, TIMESTAMP_COL

def classify_attendance(row):
    timestamp_str = row[TIMESTAMP_COL]

    if pd.isna(timestamp_str) or timestamp_str == '':
        return 'Absent', None

    # Convert timestamp string to datetime object
    try:
        check_in = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S").time()
    except ValueError:
        return 'Invalid Time Format', None

    if check_in <= ON_TIME_LIMIT:
        return 'Present', check_in
    elif check_in <= LATE_LIMIT:
        return 'Late', check_in
    else:
        return 'Absent', check_in

def main():
    # Read the input CSV
    df = pd.read_csv(INPUT_FILE)

    # Apply the classification
    results = df.apply(classify_attendance, axis=1)
    df['Status'] = results.apply(lambda x: x[0])
    df['Check-in Time'] = results.apply(lambda x: x[1] if x[1] else '—')

    # Save to output file
    df[[NAME_COL, 'Status', 'Check-in Time']].to_csv(OUTPUT_FILE, index=False)
    print(f"Attendance report generated and saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
