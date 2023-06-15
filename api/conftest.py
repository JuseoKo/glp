import pytest
from testcontainers.postgres import PostgresContainer

@pytest.fixture(scope="session", autouse=True)
def postgres() -> None:
    with PostgresContainer("postgres:13.3", port=5432, user='ls').with_bind_ports(5432, 5432) as pg:
        yield pg