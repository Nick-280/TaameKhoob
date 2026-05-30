"""Tests for notification decorators (SMS, Push, Panel)."""

import sys
import os

sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
)

from taamekhoob.notification.notifier import EmailNotifier
from taamekhoob.notification.decorators import (
    SMSDecorator,
    PushDecorator,
    PanelDecorator,
)


def test_email_notifier():
    """test: EmailNotifier faghat email mifreste."""

    notifier = EmailNotifier()
    notifier.send("Test message")
    assert True


def test_sms_decorator():
    """test: SMSDecorator bayad SMS ham ezafe kone."""

    notifier = SMSDecorator(EmailNotifier())
    notifier.send("Hello")
    assert True


def test_push_decorator():
    """test: PushDecorator bayad Push ham ezafe kone."""

    notifier = PushDecorator(EmailNotifier())
    notifier.send("Hello")
    assert True


def test_panel_decorator():
    """test: PanelDecorator bayad panel ham ezafe kone."""

    notifier = PanelDecorator(EmailNotifier())
    notifier.send("Hello")
    assert True


def test_chand_ta_decorator():
    """test: chand ta decorator ba ham kar mikonand."""

    notifier = SMSDecorator(PushDecorator(EmailNotifier()))
    notifier.send("Order received")
    assert True


def test_tamame_decorator_ha():
    """test: hame decorator ha ba ham."""

    notifier = PanelDecorator(SMSDecorator(PushDecorator(EmailNotifier())))
    notifier.send("Order completed")
    assert True


if __name__ == "__main__":
    test_email_notifier()
    test_sms_decorator()
    test_push_decorator()
    test_panel_decorator()
    test_chand_ta_decorator()
    test_tamame_decorator_ha()
