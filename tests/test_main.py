import json
import tempfile
import pytest
from unittest.mock import patch, MagicMock
from main import search_username_impl


class TestSearchUsername:
    @patch("main.subprocess.run")
    def test_search_username_success(self, mock_subprocess):
        # Mock successful Sherlock --version check
        version_mock = MagicMock(returncode=0, stdout="Sherlock 0.16.0", stderr="")
        # Mock successful Sherlock search run
        search_mock = MagicMock(returncode=0, stdout="", stderr="")
        mock_subprocess.side_effect = [version_mock, search_mock]

        # Mock the JSON data
        mock_data = {
            "Burnsedia": {
                "github": {"url": "https://github.com/Burnsedia", "exists": True},
                "twitter": {"url": "https://twitter.com/baileyburnsed", "exists": True},
            }
        }

        with (
            patch("main.tempfile.NamedTemporaryFile") as mock_temp,
            patch("main.json.load", return_value=mock_data) as mock_json_load,
            patch("main.os.unlink") as mock_unlink,
        ):
            mock_temp.return_value.__enter__.return_value.name = "/tmp/test.json"
            mock_temp.return_value.__enter__.return_value = MagicMock()

            result = search_username_impl("Burnsedia")

        assert result["total_found"] == 2
        assert len(result["found"]) == 2
        sites = [f["site"] for f in result["found"]]
        assert "github" in sites
        assert "twitter" in sites
        assert result["error"] is None

    @patch("main.subprocess.run")
    def test_search_username_sherlock_not_found(self, mock_subprocess):
        # Mock Sherlock not found
        mock_subprocess.side_effect = [FileNotFoundError, MagicMock(returncode=1)]

        result = search_username_impl("cypher")

        assert result["total_found"] == 0
        assert result["found"] == []
        assert "Sherlock CLI not found" in result["error"]

    @patch("main.subprocess.run")
    def test_search_username_timeout(self, mock_subprocess):
        # Mock successful --version check
        version_mock = MagicMock(returncode=0, stdout="Sherlock 0.16.0", stderr="")
        # Mock timeout on search
        from subprocess import TimeoutExpired

        mock_subprocess.side_effect = [
            version_mock,
            TimeoutExpired(cmd=["sherlock"], timeout=300),
        ]

        result = search_username_impl("cypher")

        assert result["total_found"] == 0
        assert result["found"] == []
        assert "timed out" in result["error"]

    @patch("main.subprocess.run")
    def test_search_username_json_decode_error(self, mock_subprocess):
        # Mock successful --version and search run
        version_mock = MagicMock(returncode=0, stdout="Sherlock 0.16.0", stderr="")
        search_mock = MagicMock(returncode=0, stdout="", stderr="")
        mock_subprocess.side_effect = [version_mock, search_mock]

        # Mock JSON decode error
        with (
            patch("main.tempfile.NamedTemporaryFile") as mock_temp,
            patch(
                "main.json.load",
                side_effect=json.JSONDecodeError("Invalid JSON", "", 0),
            ) as mock_json_load,
            patch("main.os.unlink") as mock_unlink,
        ):
            mock_temp.return_value.__enter__.return_value.name = "/tmp/test.json"
            mock_temp.return_value.__enter__.return_value = MagicMock()

            result = search_username_impl("Burnsedia")

        assert result["total_found"] == 0
        assert result["found"] == []
        assert "Failed to parse Sherlock output" in result["error"]
