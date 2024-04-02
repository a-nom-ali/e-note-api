from sqlalchemy import create_engine, Table, Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import MetaData


# This function will create the database and tables
def create_database(uri):
    engine = create_engine(uri)
    Session = sessionmaker(engine)
    metadata_obj = MetaData()
    # session = Session()
    # session.add(User())
    # session.commit()


# Use this function in your local environment to initialize the database.
# For MariaDB, the URI format is typically:
# 'mysql+pymysql://user:password@host:port/dbname'
# Replace 'sqlite:///api_db.sqlite' with your actual MariaDB URI
create_database('sqlite:///api_db.sqlite')