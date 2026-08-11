import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

db_url = os.getenv("DB_URL")
engine = create_async_engine(db_url, echo=True)
SessionLocal = sessionmaker(
    bind=engine, 
    expire_on_commit=False, 
    class_=AsyncSession)