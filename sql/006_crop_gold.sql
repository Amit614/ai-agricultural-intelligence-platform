CREATE TABLE IF NOT EXISTS agri.gold.crop_recommendations(
field_id STRING,
recommended_crop STRING,
score DOUBLE
) USING DELTA;