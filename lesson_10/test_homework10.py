"""Tests for function log_event using pytest and pytest-mock."""

from homework_10_log_event import log_event


def test_log_event_success(mocker):
    """Test log_event with status 'success'."""
    mock_logger = mocker.patch('logging.getLogger').return_value
    log_event('user1', 'success')
    mock_logger.info.assert_called_once_with(
        'Login event - Username: user1, Status: success',
    )


def test_log_event_expired(mocker):
    """Test log_event with status 'expired'."""
    mock_logger = mocker.patch('logging.getLogger').return_value
    log_event('user2', 'expired')
    mock_logger.warning.assert_called_once_with(
        'Login event - Username: user2, Status: expired',
    )


def test_log_event_failed(mocker):
    """Test log_event with status 'failed'."""
    mock_logger = mocker.patch('logging.getLogger').return_value
    log_event('user3', 'failed')
    mock_logger.error.assert_called_once_with(
        'Login event - Username: user3, Status: failed',
    )


def test_log_event_unknown(mocker):
    """Test log_event with an unknown status."""
    mock_logger = mocker.patch('logging.getLogger').return_value
    log_event('user4', 'unknown')
    mock_logger.error.assert_called_once_with(
        'Login event - Username: user4, Status: unknown',
    )
