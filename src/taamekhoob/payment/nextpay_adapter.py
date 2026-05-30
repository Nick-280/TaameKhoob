"""Adapter baraye dargah pardakht NextPay"""

import random
from taamekhoob.payment.interface import PaymentGateway


class NextPaySDK:
    """shabih sazie API NextPay
    (third-party - nemishe taghir dad)"""

    def init(self, api_key: str, amount_rial: int) -> dict:
        """pardakht ro shoru mikone. (api_key vase
        ehraze hoviat). dict ro ba trans_id va url
        mide"""

        trans_id = f"{random.randint(1000, 9999)}_{amount_rial}"
        return {"trans_id": trans_id, "url": f"https://nextpay.ir/pay/{trans_id}"}

    def check(self, trans_id: str) -> dict:
        """vaziate pardakht ro check mikone.
        trans_id: code transaction ke az dargah
        bargashte. Dict ba status return mikone.
        (mesle "paid")"""

        return {"status": "paid"}


class NextPayAdapter(PaymentGateway):
    """NextPay ro be PaymentGateway tabdil mikone"""

    def __init__(self) -> None:
        """yek nemone az NextPaySDK misaze"""

        self._sdk = NextPaySDK()

    def pay(self, amount_toman: int, order_id: str) -> str:
        """pardakht ro shoru mikone va URL vase
        hedayate user ro bar migardoone"""

        amount_rial = amount_toman * 10
        api_key = "test_api_key_0254"

        result = self._sdk.init(api_key=api_key, amount_rial=amount_rial)

        return result["url"]

    def verify(self, payment_ref: str) -> bool:
        """vaziate pardakht ro check mikone"""

        result = self._sdk.check(trans_id=payment_ref)
        return result.get("status") == "paid"
