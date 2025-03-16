# Ad Campaign Performance Analyzer 📊

## Overview  
A data-driven solution to analyze digital ad campaign performance, built using **SQL**, **Python automation**, and **Looker Studio dashboards**. The project automates data insertion, performs analysis, and visualizes key campaign metrics in real-time.

---

## Features
- **SQL-based Analysis:** Data storage and querying for ad campaign KPIs.
- **Python Automation:** Automated CSV data insertion into MySQL using Python.
- **Looker Studio Visualization:** Interactive dashboards showcasing CTR, conversions, and ROI.
- **Remote MySQL Database:** Hosted on **Railway**, integrated directly with visualization tools.

---

## Technologies Used
- **Languages:** Python, SQL
- **Tools:** MySQL (hosted on Railway), Looker Studio, Pandas, MySQL Connector, GitHub
- **Visualization:** Looker Studio Dashboard

---

## How It Works

1. **Python Automation:**
   - Reads ad campaign data from CSV.
   - Converts and inserts data into Railway-hosted MySQL DB using Python.
  
2. **SQL Data Storage:**
   - Data stored in a normalized table with key fields: clicks, impressions, conversions, cost, etc.

3. **Visualization:**
   - Looker Studio directly connected to MySQL database.
   - Dashboards visualize campaign metrics (CTR, conversions, ROI).

---

## Repository Structure

```
Ad-Campaign-Analyzer/
├── ad_campaign_data_upload.py        # Python script for automation
├── ad_campaign_data.csv              # Sample dataset
├── SQL_queries.sql                   # SQL queries used
└── README.md                         # Project overview and documentation
```

---

## Looker Studio Dashboard  
👉 [View Dashboard]( https://lookerstudio.google.com/reporting/6faea584-46e9-4bf5-b69b-c8f31fc8197f )

---

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/parasnath-tech/Ad-Campaign-Analyzer.git
```

2. Install Python dependencies:
```bash
pip install pandas
pip install mysql-connector-python
```

3. Update database credentials in `ad_campaign_data_upload.py`.

4. Run the script:
```bash
python ad_campaign_data_upload.py
```

---

## SQL Table Creation Query
```sql
CREATE TABLE ad_campaign_data (
  campaign_id INT PRIMARY KEY,
  clicks INT,
  impressions INT,
  cost FLOAT,
  conversions INT
);
```

---

## License
This project is licensed under the MIT License.

