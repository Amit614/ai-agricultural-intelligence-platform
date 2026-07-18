CREATE TABLE IF NOT EXISTS agri.gold.knowledge_registry(
category STRING,
knowledge_key STRING,
title STRING,
content STRING
) USING DELTA;