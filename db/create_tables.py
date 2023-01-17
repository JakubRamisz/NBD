def create_tables(session):
    session.execute(
    """
    CREATE TABLE IF NOT EXISTS clients(
        client_id UUID PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
    );
    """
    )
