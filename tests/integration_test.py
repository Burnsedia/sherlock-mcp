import pytest
from main import search_username_impl


def test_integration_real_sherlock():
    # Perform a real search with Sherlock CLI (requires Sherlock installed)
    existing_username = (
        "Burnsedia"  # Update with a username known to exist on some platforms
    )

    result = search_username(existing_username)

    # Check that some results are returned for known valid username
    assert result["total_found"] > 0
    assert len(result["found"]) == result["total_found"]

    # Check for expected keys in the output
    for entry in result["found"]:
        assert "site" in entry
        assert "url" in entry
        assert "exists" in entry
        assert entry["exists"] is True


def test_integration_nonexistent_user():
    # Perform a real search with Sherlock CLI for nonexistent user
    nonexistent_user = (
        "clearlydoesnotexist1234"  # Update with a guaranteed non-existent username
    )

    result = search_username(nonexistent_user)

    # Ensure no results are returned for non-existent username
    assert result["total_found"] == 0
    assert result["found"] == []
    assert result["error"] is None


def test_integration_invalid_input():
    # Perform a real search with invalid input
    invalid_input = ""  # Empty input

    result = search_username(invalid_input)

    # Ensure no results and an appropriate error message
    assert result["total_found"] == 0
    assert result["found"] == []
    assert "Invalid username" in result["error"].lower()
