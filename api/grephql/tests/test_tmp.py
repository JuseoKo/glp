from loguru import logger

def test_frist():
    logger.info('첫번째 테스트 성공')
    x = [2, 2 ,3 ,5]
    for i in range(7):
        print(x[i])



def test_second():
    logger.info('두번째 테스트 성공')