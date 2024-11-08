"""Configuration file for pytest fixtures."""

import sys

import pexpect
import pytest
from pyfakefs.fake_filesystem_unittest import Patcher

from app.calculator import Calculator


@pytest.fixture
def calc():
    """Fixture to create a Calculator instance."""
    return Calculator()


@pytest.fixture(autouse=True)
def fake_fs():
    """Automatically initialize pyfakefs for all tests."""
    with Patcher() as patcher:
        yield patcher.fs


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
