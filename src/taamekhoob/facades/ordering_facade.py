"""Ordering facade. tamame process sefaresh ro sade mikone"""

from taamekhoob.order.order import Order
from taamekhoob.payment.interface import PaymentGateway
from taamekhoob.delivery.interface import DeliveryService
from taamekhoob.notification.notifier import Notifier
from taamekhoob.facades.kitchen_facade import KitchenFacade


class OrderingFacade:
    """facade asli baraye sabt sefaresh"""

    def __init__(
        self,
        inventory,
        payment: PaymentGateway,
        delivery: DeliveryService,
        notifier: Notifier,
        kitchen: KitchenFacade,
    ) -> None:
        """subsystem haye lazem ro daryaft mikone"""

        self._inventory = inventory
        self._payment = payment
        self._delivery = delivery
        self._notifier = notifier
        self._kitchen = kitchen

    def place_order(self, order: Order) -> dict:
        """tamame marahel sefaresh ro anjam mide"""

        for item, qty in order.items:
            if not self._inventory.check(item, qty):
                self._notifier.send(f"{item.description()} unavailable")

                return {"ok": False, "reason": "out_of_stock"}

        payment_url = self._payment.pay(order.order_id, order.total_cost())
        payment_ok = self._payment.verify(order.order_id)
        if not payment_ok:
            return {"ok": False, "reason": "payment_failed"}

        for item, qty in order.items:
            self._inventory.reserve(item, qty)

        ticket = self._kitchen.queue(order)

        tracking = self._delivery.schedule(order.address, order.items)

        self._notifier.send(f"Order {order.order_id} confirmed")

        return {
            "ok": True,
            "ticket": ticket,
            "tracking": tracking,
            "payment_url": payment_url,
        }
