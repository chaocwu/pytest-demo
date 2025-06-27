import random
import pytest


def test_passed():
    assert True


def test_failed():
    assert random.choice([True, False]), "This test passed or failed randomly"


@pytest.mark.skip(reason="This test is skipped")
def test_skipped():
    assert True


def test_broken():
    raise Exception("This test is broken")


def probabilistic_success(success_rate: float) -> bool:
    return random.random() < success_rate


@pytest.mark.parametrize("run_id", range(100))
def test_success_rate(run_id: int):
    success = probabilistic_success(0.95)
    assert success, f"测试 {run_id} 失败"
