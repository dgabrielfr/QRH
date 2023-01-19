SELECT ST_DISTANCE(c1.coordo, c2.coordo) / 1000 as "Distance (km)",
    CASE WHEN degrees(ST_AZIMUTH(c1.coordo, c2.coordo)) < 0 THEN degrees(ST_AZIMUTH(c1.coordo, c2.coordo)) + 360
    ELSE
    degrees(ST_AZIMUTH(c1.coordo, c2.coordo))
    END AS "Cap"
FROM demoPoint c1, demoPoint c2
WHERE c1.nom = 'LFML' AND c2.nom = 'LFPO';
