CREATE VIEW IF NOT EXISTS agri.gold.v_farm_summary AS
SELECT farm_id, crop, yield FROM agri.gold.farm_metrics;
