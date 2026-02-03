import pytest
from main import _search_username


@pytest.mark.integration
def test_real_sherlock_existing_user():
    result = _search_username("torvalds", ["github"])

    assert result["total_found"] >= 1
    assert len(result["found"]) == result["total_found"]

    for entry in result["found"]:
        assert "site" in entry
        assert "url" in entry


@pytest.mark.integration
def test_real_sherlock_nonexistent_user():
    result = _search_username("clearlydoesnotexist123456", ["github"])

    assert result["total_found"] == 0
    assert result["found"] == []
    assert result["error"] is None


def test_invalid_input():
    result = _search_username("")

    assert result["total_found"] == 0
    assert result["found"] == []
    assert "invalid username" in result["error"].lower()

