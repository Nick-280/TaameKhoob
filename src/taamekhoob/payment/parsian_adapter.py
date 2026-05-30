"""Adapter baraye dargah pardakht Parsian"""

from taamekhoob.payment.interface import PaymentGateway


class parsianSDK:
    """shabih sazie API Parsian
    (third-party - nemishe taghir dad)"""

    def request(self, mablagh: int, mobile: str) -> dict:
        """darkhaste pardakht"""

        link = f"https://parsian.ir/pay/{mablagh}_{mobile}"
        return {"url": link, "code": 5289}

    def check(self, code: int) -> dict:
        """pardakht ro check mikone"""

        return {"status": "OK"}


class ParsianAdapter(PaymentGateway):
    """Parsian ro be PaymentGateway tabdil mikone"""

    def __init__(self):
        """yek nemone az NextPaySDK misaze"""

        self._sdk = parsianSDK()

    def pay(self, amount_toman: int, order_id: str) -> str:
        """pardakht ro shoru mikone va URL vase
        hedayate user ro bar migardoone"""

        mablagh_rial = amount_toman * 10

        result = self._sdk.request(mablagh=mablagh_rial, mobile="09112345678")

        return result["url"]

    def verify(self, payment_ref: str) -> bool:
        """vaziate pardakht ro check mikone"""

        result = self._sdk.check(code=5289)
        return result.get("status") == "OK"
