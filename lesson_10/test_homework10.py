"""Tests for function log_event."""
import logging
from unittest.mock import patch

from homework_10_log_event import log_event


def test_log_event():
    """Test the log_event function with various statuses."""
    with patch('logging.getLogger') as mock_get_logger:
        logger = mock_get_logger.return_value  # Create mock logger

        # Check status "success"
        log_event('user1', 'success')
        logger.info.assert_called_with(
            'Login event - Username: user1, Status: success',
        )

        # Check status "expired"
        log_event('user2', 'expired')
        logger.warning.assert_called_with(
            'Login event - Username: user2, Status: expired',
        )

        # Check status "failed"
        log_event('user3', 'failed')
        logger.error.assert_called_with(
            'Login event - Username: user3, Status: failed',
        )

        # Check unknown status
        log_event('user4', 'unknown')
        logger.error.assert_called_with(
            'Login event - Username: user4, Status: unknown',
        )


if __name__ == '__main__':
    test_log_event()
    logging.info('Tests passed!')
