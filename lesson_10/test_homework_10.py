from ..lesson_10.homework_10 import log_event
import logging



def test_success(caplog):
    with caplog.at_level(logging.INFO):
        log_event('User_1', 'success')
    # Checking status and level of log
    assert 'success' and 'INFO' in caplog.text

def test_expired(caplog):
    with caplog.at_level(logging.WARNING):
        log_event('User_2', 'expired')
    # Checking status and level of log
    assert 'expired' and "WARN" in caplog.text

def test_error(caplog):
    with caplog.at_level(logging.ERROR):
        log_event('User_3', 'failed')
    # Checking status and level of log
    assert 'failed' and 'ERROR' in caplog.text

def test_not_string_data(caplog):
    with caplog.at_level(logging.INFO):
        log_event(1, 2)
    # Checking status and level of log
    assert '2' and 'ERROR' in caplog.text

def test_empty_user(caplog):
    with caplog.at_level(logging.ERROR):
        log_event('', 'failed')
    # Checking status and level of log
    assert 'failed' and 'ERROR' in caplog.text