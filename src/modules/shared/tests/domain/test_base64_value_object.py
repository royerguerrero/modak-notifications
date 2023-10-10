"""Test Base64File value object"""

# Testing
import pytest

# Domain
from src.modules.shared.domain import Base64File


@pytest.mark.unit
def test_from_bytes():
    bytes_ = b'hello world'
    base64_file = Base64File.from_bytes(bytes_)
    assert base64_file.value == 'aGVsbG8gd29ybGQ='


@pytest.mark.unit
def test_to_bytes():
    base64_file = Base64File('aGVsbG8gd29ybGQ=')
    bytes_ = base64_file.to_bytes()
    assert bytes_ == b'hello world'


@pytest.mark.unit
def test_invalid_base64():
    with pytest.raises(ValueError):
        Base64File('invalid base64 string')
