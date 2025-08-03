import os
from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData, insert, select
from sqlalchemy.orm import declarative_base, Session

# Base for ORM mapping (optional, but helpful)
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

# Create engine
def get_engine():
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    db = os.getenv("POSTGRES_DB", "postgres")

    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url, echo=True)

# Integration test
def test_insert_user():
    engine = get_engine()
    Base.metadata.create_all(engine)  # Create table if not exists

    with Session(engine) as session:
        # Insert user
        new_user = User(first_name="John", last_name="Doe")
        session.add(new_user)
        session.commit()

        inserted_id = new_user.id

        # Query inserted user
        user = session.query(User).filter_by(id=inserted_id).first()
        assert user.first_name == "John" and user.last_name == "Doe"
