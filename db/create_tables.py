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

    session.execute(
    """
    CREATE TABLE IF NOT EXISTS accounts(
        account_id UUID PRIMARY KEY,
        balance FLOAT,
        owner_id UUID,
        type TEXT,
        rate FLOAT,
        last_update_date TIMESTAMP
    );
    """
    )
