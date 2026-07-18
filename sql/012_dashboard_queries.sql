-- Top recommended crops
SELECT recommended_crop, COUNT(*) recommendations
FROM agri.gold.crop_recommendations
GROUP BY recommended_crop;
