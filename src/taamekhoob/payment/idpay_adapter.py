"""Adapter baraye dargah pardakht IDPay"""

from taamekhoob.payment.interface import PaymentGateway


class IdpaySDK:
    """shabih sazie API IDPay
    (third-party - nemishe taghir dad)"""

    def create_transaction(self, order_id: str, price: int) -> dict:
        """ye transaction jadid misaze"""

        return {"id": f"IDP_{order_id}", "link": f"https://idpay.ir/pay/{order_id}"}

    def verify_transaction(self, id: str, status: int) -> bool:
        """vaziate transaction ro check mikone"""

        return status == 200


class IdpayAdapter(PaymentGateway):
    """IdPay ro be PaymentGateway tabdil mikone"""

    def __init__(self) -> None:
        """yek nemoone az IdpaySDK misaze"""

        self.sdk = IdpaySDK()

    def pay(self, amount_toman: int, order_id: str) -> str:
        """pardakht ro shoru mikone va URL vase
        hedayate user ro bar migardoone"""

        result = self.sdk.create_transaction(order_id=order_id, price=amount_toman)
        return result["link"]

    def verify(self, payment_ref: str) -> bool:
        """vaziate pardakht ro check mikone"""

        return self.sdk.verify_transaction(id=payment_ref, status=200)
