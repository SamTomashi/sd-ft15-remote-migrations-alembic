from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Specialty, 

DATABASE_URL = "sqlite:///db/clinic.db"

if __name__ == '__main__':
    engine = create_engine(DATABASE_URL, echo=True)

    # Only for first-time setup (before using Alembic)
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

   dentist = Specialty()
