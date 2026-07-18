CREATE TABLE IF NOT EXISTS agri.gold.disease_alerts(
field_id STRING,
crop STRING,
disease STRING,
risk STRING,
event_time TIMESTAMP
) USING DELTA;