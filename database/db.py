import psycopg2
from psycopg2 import DatabaseError

def get_connection():
    try:
        return psycopg2.connect(
            host='dpg-cp78gdu3e1ms73agd4f0-a.oregon-postgres.render.com',
            user='sysvita_user',
            password='VMIWWKEKiJhLf3qFoKzdOkqX7flD0tVs',
            database='sysvita'
        )
    except DatabaseError as ex:
        raise ex
