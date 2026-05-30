"""Tests for payment adapters (Zarinpal, IDPay, NextPay)."""

import sys
import os

sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
)

from taamekhoob.payment.zarinpal_adapter import ZarinpalAdapter
from taamekhoob.payment.idpay_adapter import IdpayAdapter
from taamekhoob.payment.nextpay_adapter import NextPayAdapter


def test_zarinpal_pay_returns_url():
    """test: Zarinpal pay bayad URL bargardoone."""
    gateway = ZarinpalAdapter()

    url = gateway.pay(amount_toman=250000, order_id="ORD-001")

    assert url.startswith("https://")
    assert "zp.ir" in url


def test_zarinpal_verify_success():
    """test: Zarinpal verify bayad True bargardoone."""
    gateway = ZarinpalAdapter()

    result = gateway.verify(payment_ref="AUTH_123")

    assert result is True


def test_idpay_pay_returns_url():
    """test: IDPay pay bayad URL bargardoone."""
    gateway = IdpayAdapter()

    url = gateway.pay(amount_toman=250000, order_id="ORD-001")

    assert url.startswith("https://")
    assert "idpay.ir" in url


def test_idpay_verify_success():
    """test: IDPay verify bayad True bargardoone."""
    gateway = IdpayAdapter()

    result = gateway.verify(payment_ref="IDP_ORD-001")

    assert result is True


def test_nextpay_pay_returns_url():
    """test: NextPay pay bayad URL bargardoone."""
    gateway = NextPayAdapter()

    url = gateway.pay(amount_toman=250000, order_id="ORD-001")

    assert url.startswith("https://")
    assert "nextpay.ir" in url


def test_nextpay_verify_success():
    """test: NextPay verify bayad True bargardoone."""
    gateway = NextPayAdapter()

    result = gateway.verify(payment_ref="TOKEN_123")

    assert result is True


def test_all_gateways_have_same_interface():
    """test: hame dargah ha yek interface ro daran."""
    gateways = [ZarinpalAdapter(), IdpayAdapter(), NextPayAdapter()]

    for g in gateways:
        assert hasattr(g, "pay")
        assert hasattr(g, "verify")
        assert callable(g.pay)
        assert callable(g.verify)


if __name__ == "__main__":
    test_zarinpal_pay_returns_url()
    test_zarinpal_verify_success()
    test_idpay_pay_returns_url()
    test_idpay_verify_success()
    test_nextpay_pay_returns_url()
    test_nextpay_verify_success()
    test_all_gateways_have_same_interface()
