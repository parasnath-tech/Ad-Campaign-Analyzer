import pandas as pd
import mysql.connector

# Step 1: Read CSV file
data = pd.read_csv('ad_campaign_data.csv')

# Step 2: Connect to Railway MySQL database
connection = mysql.connector.connect(
    host='ballast.proxy.rlwy.net',        # Your Railway Hostname
    port=38663,                           # Your Railway Port
    user='root',                 # Replace with your Railway username
    password='JIOorQVZejOXBuPTfclVUiCwJEkJLZhW',             # Replace with your Railway password
    database='ad_campaigns'              # Replace with your Railway database name
)

cursor = connection.cursor()

# Step 3: Insert data into MySQL
for index, row in data.iterrows():
    sql = """
    INSERT INTO ad_campaign_data (campaign_id, clicks, impressions, cost, conversions)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        int(row['campaign_id']),
        int(row['clicks']),
        int(row['impressions']),
        float(row['cost']),
        int(row['conversions'])
    )
    cursor.execute(sql, values)

# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()

print("Data inserted successfully!")
