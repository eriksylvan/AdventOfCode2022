
import pytest
import day_01
    
testData = {1:[1000,2000,3000],2:[4000],3:[5000,6000],4:[7000,8000,9000,], 5:[10000]}

def test_mostCalories():
    assert day_01.max_calories(testData) == 24000

def test_maxThreeCalories():
    assert day_01.max_3_calories(testData) == 45000
    

@pytest.mark.skip(reason="Skipped for no reason")
def test_skippedTest():
    assert False

# Run tests from terminal:
# $ pytest test/test_day_01.py 




# read more
# https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
