SELECT nom, ST_AsText(coordo) as coordonnees, 
	ST_DISTANCE(coordo,poi)/1000 as Distance_KM 
FROM demoPoint,
	(select ST_MakePoint(2,45)::geography as poi) as poi 
WHERE ST_DWithin(coordo, poi, 400 * 1000) 
ORDER BY ST_Distance(coordo, poi)
LIMIT 10;