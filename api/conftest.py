import pytest
from testcontainers.postgres import PostgresContainer

@pytest.fixture(scope="session", autouse=True)
def postgres() -> None:
    with PostgresContainer("postgres:13.3").with_bind_ports(5431, 5431) as pg:
        yield pg