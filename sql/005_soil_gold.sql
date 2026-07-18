CREATE TABLE IF NOT EXISTS agri.gold.field_fertility
USING DELTA AS
SELECT field_id,
AVG((nitrogen+phosphorus+potassium)/3) avg_npk,
AVG(moisture) avg_moisture
FROM agri.bronze.soil_raw
GROUP BY field_id;