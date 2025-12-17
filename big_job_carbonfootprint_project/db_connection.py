from sqlalchemy import create_engine, text

DATABASE_URL =  "postgresql://postgres:5219--ZmId*@localhost:65432/postgres"

engine= create_engine(DATABASE_URL)


def fetch_all(query, params=None):
    with engine.connect() as conn:
        result = conn.execute(text(query), params or {})
        return [dict(row._mapping) for row in result]

