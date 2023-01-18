from cassandra.cluster import Cluster, ExecutionProfile, ConsistencyLevel, EXEC_PROFILE_DEFAULT
from cassandra.auth import PlainTextAuthProvider
from db.create_tables import create_tables
from db.config import *

exec_profile = ExecutionProfile(
            consistency_level=ConsistencyLevel.ONE,
        )
auth_provider = PlainTextAuthProvider(username=CASSANDRA_USER, password=CASSANDRA_PASSWORD)
cluster = Cluster(
            contact_points=[CASSANDRA_HOST],
            port=CASSANDRA_PORT,
            execution_profiles={ EXEC_PROFILE_DEFAULT: exec_profile },
            auth_provider=auth_provider,
        )


session = cluster.connect()

session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS nbd
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': 2 }
        """
    )

session.set_keyspace('nbd')


create_tables(session)
