
import pytest


from src.auth import password_validator


class TestPassword:

    def test_no_capital(self):
        nocapital = "abcdef123!"
        assert password_validator(nocapital) is False
    
    def test_no_number(self):
        nonumber = "Abcdefgh!"
        assert password_validator(nonumber) is False
    
    def test_no_specialcharacter(self):
        nospecialcharacter = "Abcdefgh2"
        assert password_validator(nospecialcharacter) is False

    def test_passwordlength(self):
        short = "Aa1!"
        assert password_validator(short) is False
    
    def test_correctpassword(self):
        correct = "teSting12!"
        assert password_validator(correct) is True

