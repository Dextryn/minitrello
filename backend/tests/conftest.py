import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from MiniTrello.backend.app.main import app
from MiniTrello.backend.app.database import Base, get_db

SERVER = "localhost"
TESTDATABASE = "MiniTrelloDB_test"

SQLALCHEMY_DATABASE_URL = (
    f"mssql+pyodbc://@{SERVER}/{TESTDATABASE}"
    "?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
)

test_engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine,
)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function")
def client():
    return TestClient(app)
