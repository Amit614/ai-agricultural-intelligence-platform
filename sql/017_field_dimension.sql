CREATE TABLE IF NOT EXISTS agri.gold.dim_field(
field_id STRING,
farm_id STRING,
field_name STRING,
area_hectares DOUBLE
) USING DELTA;