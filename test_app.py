from app import check_eligibility, add


def test_eligible():
    assert check_eligibility(20) == "Eligible"


def test_not_eligible():
    assert check_eligibility(16) == "Not Eligible"


def test_add():
    assert add(5, 3) == 8