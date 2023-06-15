from loguru import logger
import pytest

@pytest.mark.unit
def test_frist():
    logger.info('첫번째 테스트 성공')

@pytest.mark.django_db
@pytest.mark.unit
def test_second():
    logger.info('두번째 테스트 성공')