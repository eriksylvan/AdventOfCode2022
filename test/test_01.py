
import pytest
import day_01
    
def test_depthCounter():
    assert day_01.depthIncreaseCounter([199,200,208,210,200,207,240,269,260,263]) == 7

def test_depthCounterSlidingWindow_1():
    assert day_01.depthIncreaseCounterSlidingWindow([199,200,208,210,200,207,240,269,260,263]) == 5

def test_depthCounterSlidingWindow_2():
    assert day_01.depthIncreaseCounterSlidingWindow([1,1,1,2,1,1,1]) == 1

@pytest.mark.skip(reason="Skipped for no reason")
def test_skippedTest():
    assert False

# Run tests from terminal:
# $ pytest test/test_day_01.py 




# read more
# https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
