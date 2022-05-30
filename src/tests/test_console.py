import click.testing
import pytest

from pyrandomwiki import console

@pytest.fixture
def runner():
    return click.testing.CliRunner()

@pytest.fixture
def mock_requests_get(mocker):
    return mocker.patch("requests.get")

def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
