# config.py

from datetime import time

# === Attendance Rules ===
ON_TIME_LIMIT = time(9, 0)     # Before or at 09:00 is "Present"
LATE_LIMIT = time(9, 30)       # Between 09:01 and 09:30 is "Late"
# After 09:30 or blank = Absent

# === File Paths ===
INPUT_FILE = 'data/raw_attendance.csv'
OUTPUT_FILE = 'output/attendance_report.csv'

# === Column Names in CSV ===
NAME_COL = 'Name'
TIMESTAMP_COL = 'Timestamp'
