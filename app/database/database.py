from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

# Creating the database URL string using the configuration variables
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Creating a database engine by passing the database URL string to create_async_engine function.
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, autocommit=False, autoflush=False)

# All the declarative models will inherit from this base class
Base = declarative_base()


async def get_async_db():
    """Dependency function to get an async database session."""

    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
