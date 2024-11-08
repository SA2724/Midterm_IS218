"""Test module for FileManager operations using pyfakefs and pytest."""

import logging
from typing import Any

import pytest

from app.file_manager import FileManager


def test_write_file_positive(fake_fs: Any, caplog: pytest.LogCaptureFixture):
    """Test writing to a file successfully."""
    file_manager = FileManager("test_file.txt")

    with caplog.at_level(logging.INFO):
        file_manager.write_file("Hello, World!")

    # Check if the file exists in the fake filesystem
    assert fake_fs.exists("test_file.txt")

    # Read the content to verify
    with open("test_file.txt", 'r', encoding='utf-8') as file:
        content = file.read()
        assert content == "Hello, World!"

    # Check logging without quotes around the filename
    assert "Successfully wrote to file: test_file.txt" in caplog.text


def test_read_file_positive(fake_fs: Any, caplog: pytest.LogCaptureFixture):
    """Test reading from a file successfully after writing."""
    fake_fs.create_file("test_file.txt", contents="Hello, World!")

    file_manager = FileManager("test_file.txt")

    with caplog.at_level(logging.INFO):
        content = file_manager.read_file()

    assert content == "Hello, World!"

    # Check logging without quotes around the filename
    assert "Successfully read from file: test_file.txt" in caplog.text


def test_delete_file_positive(fake_fs: Any, caplog: pytest.LogCaptureFixture):
    """Test deleting a file successfully."""
    fake_fs.create_file("test_file.txt", contents="Hello, World!")

    file_manager = FileManager("test_file.txt")

    with caplog.at_level(logging.INFO):
        file_manager.delete_file()

    assert not fake_fs.exists("test_file.txt")

    # Check logging without quotes around the filename
    assert "Successfully deleted file: test_file.txt" in caplog.text


def test_read_file_negative(caplog: pytest.LogCaptureFixture):
    """Test reading from a non-existent file."""
    file_manager = FileManager("non_existent_file.txt")

    with caplog.at_level(logging.ERROR):
        with pytest.raises(FileNotFoundError):
            file_manager.read_file()

    # Check logging without quotes around the filename
    assert "File not found: non_existent_file.txt" in caplog.text


def test_delete_file_negative(caplog: pytest.LogCaptureFixture):
    """Test deleting a non-existent file."""
    file_manager = FileManager("non_existent_file.txt")

    with caplog.at_level(logging.WARNING):
        file_manager.delete_file()  # This should not raise an error, just check no error is raised

    # Check logging without quotes around the filename
    assert "File not found for deletion: non_existent_file.txt" in caplog.text
