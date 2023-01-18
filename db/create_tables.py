from db.config import TABLENAMES


def create_tables(session):
    session.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABLENAMES["CLIENT"]}(
        client_id UUID PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
    );
    """
    )

    session.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABLENAMES["ACCOUNT"]}(
        account_id UUID PRIMARY KEY,
        balance FLOAT,
        owner_id UUID,
        type TEXT,
        rate FLOAT,
        last_update_date TIMESTAMP
    );
    """
    )

    session.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABLENAMES["TRANSACTION"]}(
        transaction_id UUID PRIMARY KEY,
        account_id UUID,
        transaction_type TEXT,
        amount FLOAT,
        date TIMESTAMP
    );
    """
    )
