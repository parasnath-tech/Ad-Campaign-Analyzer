-- Table Creation Query
CREATE TABLE ad_campaign_data (
  campaign_id INT PRIMARY KEY,
  clicks INT,
  impressions INT,
  cost FLOAT,
  conversions INT
);

-- Sample Query: View All Data
SELECT * FROM ad_campaign_data;

-- Sample Query: Top 3 Campaigns by Conversions
SELECT campaign_id, conversions
FROM ad_campaign_data
ORDER BY conversions DESC
LIMIT 3;

-- Sample Query: Click-Through Rate (CTR)
SELECT campaign_id, 
       (clicks * 100.0 / impressions) AS ctr_percentage
FROM ad_campaign_data;

-- Sample Query: Cost per Conversion
SELECT campaign_id,
       (cost / conversions) AS cost_per_conversion
FROM ad_campaign_data;
