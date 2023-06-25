from loguru import logger
import pytest

@pytest.mark.unit
@pytest.mark.django_db
def test_frist():
    logger.info('첫번째 테스트 성공')

@pytest.mark.unit
def test_second():
    # import time
    # time.sleep(10)
    logger.info('두번째 테스트 성공')