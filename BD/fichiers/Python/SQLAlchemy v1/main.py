"""
Demonstration de GeoAlchemy 2
"""
__author__ = 'Damien GABRIEL'

import psycopg2
import sqlalchemy as sa
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from Airport import Airport

if __name__ == '__main__':
    engine = create_engine('postgresql://pgm:pgm@localhost/postgis', echo=False)
    insp = sa.inspect(engine)
    if insp.has_table("airport"):
        print("Airport table exists")
        Airport.__table__.drop(engine)
    Airport.__table__.create(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    Marseille_Provence = Airport(name='Marseille Provence', icao='LFML', iata='MRS',
                                 coordinates='POINT(5.21500 43.43667)')
    Paris_Orly = Airport(name='Paris Orly', icao='LFPO', iata='ORY',
                         coordinates='POINT(2.37958 48.72328)')
    session.add(Marseille_Provence)
    session.add(Paris_Orly)
    session.commit()
    # textual query should now be explicit text!
    text_query = text("""
        SELECT ST_DISTANCE(c1.coordinates,
        c2.coordinates) / 1000 as "Distance (km)",
        CASE WHEN degrees(ST_AZIMUTH(c1.coordinates, c2.coordinates)) < 0
        THEN degrees(ST_AZIMUTH(c1.coordinates, c2.coordinates)) + 360
        ELSE
        degrees(ST_AZIMUTH(c1.coordinates, c2.coordinates))
        END AS "Cap"
        FROM Airport c1, Airport c2
        WHERE c1.name = 'Marseille Provence' AND c2.name = 'Paris Orly';
        -- WHERE c1.icao = 'LFML' AND c2.icao = 'LFPO';
        """)
    distance_cap = session.execute(text_query)
    results_as_dict = distance_cap.mappings().all()
    print(results_as_dict)
