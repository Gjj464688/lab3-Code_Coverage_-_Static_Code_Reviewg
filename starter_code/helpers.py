"""
helpers.py — a small library of helper functions used as the target for
Lab 2 (Automated Unit Testing) and Lab 3 (Code Coverage & Static Code
Review). Students do not modify this file; they write/extend tests
against it.

Four families of functions:
  - String formatters: format_currency, truncate_title, slugify
  - Date calculators:   days_between, is_business_day, add_days
  - Input validators:   is_valid_email, is_valid_priority
  - Parsing / error handling: parse_due_date  <-- new for Lab 3

parse_due_date is intentionally written with a try/except block so that
Lab 3 has a realistic exception-handling path to target with coverage.py.
"""

import re
from datetime import date, datetime, timedelta


# ---------------------------------------------------------------------------
# String formatters
# ---------------------------------------------------------------------------

def format_currency(amount):
    """Format a number as US currency, e.g. 1000 -> '$1,000.00'."""
    if not isinstance(amount, (int, float)):
        raise TypeError("amount must be a number")
    sign = "-" if amount < 0 else ""
    return f"{sign}${abs(amount):,.2f}"


def truncate_title(title, max_length=20):
    """Truncate a string to max_length, appending '...' if it was cut."""
    if not isinstance(title, str):
        raise TypeError("title must be a string")
    if len(title) <= max_length:
        return title
    if max_length <= 3:
        return title[:max_length]
    return title[: max_length - 3] + "..."


def slugify(text):
    """Convert text to a URL-friendly slug: lowercase, hyphen-separated."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


# ---------------------------------------------------------------------------
# Date calculators
# ---------------------------------------------------------------------------

def days_between(date1, date2):
    """Return the number of days between two date objects (can be negative)."""
    return (date2 - date1).days


def is_business_day(d):
    """Return True if d falls on a Monday-Friday (0-4)."""
    return d.weekday() < 5


def add_days(d, days):
    """Return a new date, days days after (or before, if negative) d."""
    return d + timedelta(days=days)


# ---------------------------------------------------------------------------
# Input validators
# ---------------------------------------------------------------------------

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(email):
    """Return True if email looks like a syntactically valid address."""
    if not isinstance(email, str) or not email:
        return False
    return bool(_EMAIL_RE.match(email))


def is_valid_priority(priority):
    """Return True if priority is an integer in the inclusive range 1-5."""
    if isinstance(priority, bool):
        return False
    if not isinstance(priority, int):
        return False
    return 1 <= priority <= 5


# ---------------------------------------------------------------------------
# Parsing / error handling  (new for Lab 3 — exception-handling target)
# ---------------------------------------------------------------------------

def parse_due_date(date_str, fallback=None):
    """
    Parse a 'YYYY-MM-DD' string into a date object.

    If date_str is missing, malformed, or not a real calendar date,
    the except block below returns `fallback` instead of raising —
    this is exactly the kind of branch coverage.py tends to show as
    untested when a test suite only exercises the "happy path".
    """
    if not date_str:
        return fallback
    try:
        parsed = datetime.strptime(date_str, "%Y-%m-%d")
        return parsed.date()
    except ValueError:
        return fallback


def days_until_due(date_str, today=None):
    """
    Return the number of days between today and the parsed due date,
    or None if the date string could not be parsed.
    """
    due = parse_due_date(date_str)
    if due is None:
        return None
    if today is None:
        today = date.today()
    return (due - today).days
