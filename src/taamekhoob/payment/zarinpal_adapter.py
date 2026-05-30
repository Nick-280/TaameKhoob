"""Adapter baraye dargah pardakht Zarinpal"""

from taamekhoob.payment.interface import PaymentGateway


class ZarinpalSDK:
    """shabih sazie API Zarinpal
    (third-party - nemishe taghir dad)"""

    def request_payment(self, amount: int, callback: str) -> dict:
        """darkhast pardakht. dict ro ba authority
        va URL barmigardoone"""

        authority = f"AUTH_{amount}"
        return {"authority": authority, "url": f"https://zp.ir/pay{authority}"}

    def verify(self, authority: str, amount: int) -> dict:
        """tayid pardakht. dict ro ba status va
        ref_id barmigardoone"""

        return {"status": "OK", "ref_id": f"REF_{authority}"}


class ZarinpalAdapter(PaymentGateway):
    """Zarinpal ro be PaymentGateway tabdil mikone"""

    def __init__(self) -> None:
        """yek nemoone az ZarinpalSDK misaze"""

        self.sdk = ZarinpalSDK()

    def pay(self, amount_toman: int, order_id: str) -> str:
        """pardakht ro shoru mikone va URL vase
        hedayate user ro bar migardoone"""

        amount_rial = amount_toman * 10
        result = self.sdk.request_payment(
            amount=amount_rial, callback="https://myshop.ir/callback"
        )

        return result["url"]

    def verify(self, payment_ref: str) -> bool:
        """vaziate pardakht ro check mikone"""

        result = self.sdk.verify(payment_ref, amount=0)
        return result.get("status") == "OK"
