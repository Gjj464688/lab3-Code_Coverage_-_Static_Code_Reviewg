from datetime import date

import pytest

from helpers import (
    add_days,
    days_between,
    format_currency,
    is_business_day,
    is_valid_email,
    is_valid_priority,
    slugify,
    truncate_title,
    parse_due_date,
    days_until_due,
)


# ============================================================
# String formatters  (reasonably covered already)
# ============================================================

class TestFormatCurrency:
    def test_zero(self):
        assert format_currency(0) == "$0.00"

    def test_typical_amount(self):
        assert format_currency(19.9) == "$19.90"

    def test_negative_amount(self):
        assert format_currency(-50) == "-$50.00"

    def test_rejects_non_numeric_input(self):
        with pytest.raises(TypeError):
            format_currency("free")


class TestTruncateTitle:
    def test_shorter_than_limit_is_unchanged(self):
        assert truncate_title("Short", max_length=20) == "Short"

    def test_one_over_limit_is_truncated(self):
        title = "123456789012345678901"  # 21 characters
        result = truncate_title(title, max_length=20)
        assert result == "12345678901234567..."


def test_slugify_lowercases_and_hyphenates():
    assert slugify("Buy Groceries Today") == "buy-groceries-today"


def test_slugify_strips_special_characters():
    assert slugify("Renew passport!! (urgent)") == "renew-passport-urgent"


# ============================================================
# Date calculators
#
# NOTE: only the "positive days" path of add_days is tested below.
# The "days < 0" branch is never exercised by any test here — that
# is one of the gaps coverage.py should surface for you.
# ============================================================

class TestDaysBetween:
    def test_typical_range(self):
        assert days_between(date(2026, 3, 1), date(2026, 3, 11)) == 10


@pytest.mark.parametrize(
    "day,expected",
    [
        (date(2026, 8, 24), True),   # Monday
        (date(2026, 8, 29), False),  # Saturday
    ],
)
def test_is_business_day(day, expected):
    assert is_business_day(day) == expected


class TestAddDays:
    def test_add_positive_days(self):
        assert add_days(date(2026, 1, 1), 10) == date(2026, 1, 11)

    def test_crosses_month_boundary(self):
        assert add_days(date(2026, 1, 28), 5) == date(2026, 2, 2)

    def test_add_negative_days(self):
        assert add_days(date(2026, 1, 11), -10) == date(2026, 1, 1)


# ============================================================
# Input validators
#
# NOTE: only the two valid-boundary cases are tested below. The
# invalid/out-of-range/wrong-type cases from Lab 2 are missing here
# on purpose — coverage.py will flag is_valid_priority's rejection
# branches as only partially exercised.
# ============================================================

@pytest.mark.parametrize(
    "email,expected",
    [
        ("user@example.com", True),
        ("no-at-sign.example.com", False),
    ],
)
def test_is_valid_email(email, expected):
    assert is_valid_email(email) == expected


@pytest.mark.parametrize(
    "priority,expected",
    [
        (1, True),   # minimum valid boundary
        (5, True),   # maximum valid boundary
        (0, False),
        (6, False),
        (2.5, False),
        ("3", False),
        (True, False),
    ],
)
def test_is_valid_priority(priority, expected):
    assert is_valid_priority(priority) == expected


# ============================================================
# Parsing / error handling
#
# NOTE: parse_due_date and days_until_due had no tests in the
# starter file. The tests below cover the cases requested in Lab 3.
# ============================================================

def test_parse_due_date_valid():
    assert parse_due_date("2026-10-04") == date(2026, 10, 4)


def test_parse_due_date_malformed_uses_fallback():
    fallback = date(2026, 12, 31)
    assert parse_due_date("not-a-date", fallback) == fallback


def test_days_until_due():
    today = date(2026, 10, 4)
    assert days_until_due("2026-10-14", today) == 10