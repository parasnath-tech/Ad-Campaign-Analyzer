Ad Campaign Performance Analyzer 📊
Overview
A data-driven solution to analyze digital ad campaign performance, built using SQL, Python automation, and Looker Studio dashboards. The project automates data insertion, performs analysis, and visualizes key campaign metrics in real-time.

Features
SQL-based Analysis: Data storage and querying for ad campaign KPIs.
Python Automation: Automated CSV data insertion into MySQL using Python.
Looker Studio Visualization: Interactive dashboards showcasing CTR, conversions, and ROI.
Remote MySQL Database: Hosted on Railway, integrated directly with visualization tools.
Technologies Used
Languages: Python, SQL
Tools: MySQL (hosted on Railway), Looker Studio, Pandas, MySQL Connector, GitHub
Visualization: Looker Studio Dashboard
How It Works
Python Automation:

Reads ad campaign data from CSV.
Converts and inserts data into Railway-hosted MySQL DB using Python.
SQL Data Storage:

Data stored in a normalized table with key fields: clicks, impressions, conversions, cost, etc.
Visualization:

Looker Studio directly connected to MySQL database.
Dashboards visualize campaign metrics (CTR, conversions, ROI).
Repository Structure
bash
Copy
Edit
Ad-Campaign-Analyzer/
├── ad_campaign_data_upload.py        # Python script for automation
├── ad_campaign_data.csv              # Sample dataset
├── SQL_queries.sql                   # SQL queries used
└── README.md                         # Project overview and documentation
Looker Studio Dashboard
👉 View Dashboard

How to Run the Project
Clone the repository:

bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/Ad-Campaign-Analyzer.git
Install Python dependencies:

nginx
Copy
Edit
pip install pandas mysql-connector-python
Update database credentials in ad_campaign_data_upload.py.

Run the script:

nginx
Copy
Edit
python ad_campaign_data_upload.py
