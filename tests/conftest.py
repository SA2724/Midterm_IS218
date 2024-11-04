"""Test fixtures for the Calculator application."""

import sys
import pexpect
import pytest

from app.calculator import Calculator


@pytest.fixture
def calc():
    """Fixture to create a Calculator instance."""
    return Calculator()


@pytest.fixture
def repl():
    """Fixture to start the Calculator REPL application."""
    # Path to the main.py script
    script = 'main.py'

    # Start the REPL application
    try:
        child = pexpect.spawn(
            sys.executable,
            [script],
            encoding='utf-8',
            timeout=5
        )
        child.expect('Welcome to the Calculator REPL.*')
    except pexpect.exceptions.ExceptionPexpect as e:
        pytest.fail(f"Failed to start REPL: {e}")

    yield child
    child.terminate()
