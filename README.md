# attendance-analyzer-agent
AI-powered attendance report generator

Attendance Analyzer Agent
An AI-powered autonomous agent that reads raw attendance data from a CSV file, classifies entries as **Present**, **Late**, or **Absent** based on predefined time thresholds, and generates a structured attendance report automatically — no manual effort required.

Problem Statement
Manual attendance tracking is time-consuming, error-prone, and inefficient — especially in educational institutions or organizations where daily records are required. This project automates the process using a lightweight and configurable Python agent.

Proposed Solution
The system processes raw timestamped attendance data, checks each entry against defined rules (like late cut-off time), and generates a final report in CSV format. It can be easily adapted to integrate with Google Sheets, email systems, or dashboards in the future.

Tech Stack
Python 3.13
Pandas – for data processing and logic
Datetime module – for time parsing and comparison
VS Code – code editor

Project Structure
attendance-analyzer-agent/
├── main.py # Main logic to process attendance
├── config.py # Configurable rules and file paths
├── data/
│ └── raw_attendance.csv # Sample input data
├── output/
│ └── attendance_report.csv # Final attendance report
├── README.md # Project documentation
├── requirements.txt # Libraries to install

How to Run

1. Clone the Repository
   ```bash
   git clone https://github.com/ashwinib24/attendance-analyzer-agent.git
   cd attendance-analyzer-agent

2. Install Dependencies
bash
Copy
Edit
pip install pandas openpyxl

3. Place your raw CSV inside the /data folder

4. Run the Script
bash
Copy
Edit
python main.py

5. Check the Output
Open /output/attendance_report.csv

Sample Output
Name	   Status	   Check-in Time
Alice	   Present	   08:55:00
Bob	     Late	       09:15:00
Charlie	 Absent	        —

