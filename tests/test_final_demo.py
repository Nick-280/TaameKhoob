import sys

sys.path.append("src")

from taamekhoob.infrastructure.config_manager import ConfigManager
from taamekhoob.infrastructure.db_manager import DBManager
from taamekhoob.infrastructure.logger import Logger
from taamekhoob.menu.factory import MenuItemFactory
from taamekhoob.menu.decorators import ExtraCheese, ExtraMushroom, Milk, Sugar
from taamekhoob.order.builder import OrderBuilder
from taamekhoob.payment.zarinpal_adapter import ZarinpalAdapter
from taamekhoob.delivery.snappbox_adapter import SnappBoxAdapter
from taamekhoob.notification.notifier import EmailNotifier
from taamekhoob.notification.decorators import SMSDecorator
from taamekhoob.facades.kitchen_facade import KitchenFacade
from taamekhoob.facades.ordering_facade import OrderingFacade
from taamekhoob.services.inventory_service import InventoryService

config = ConfigManager()
db = DBManager()
log = Logger()


pizza = MenuItemFactory.create("pizza", size="L")
pizza = ExtraMushroom(pizza)
pizza = ExtraCheese(pizza)

coffee = MenuItemFactory.create("espresso")
coffee = Milk(coffee)
coffee = Sugar(coffee)
coffee = Sugar(coffee)


order = (
    OrderBuilder()
    .add_item(pizza, qty=1)
    .add_item(coffee, qty=2)
    .deliver_to("Babolsar, Pasdaran")
    .pay_with("zarinpal")
    .build()
)
order.order_id = "ORD-001"

facade = OrderingFacade(
    inventory=InventoryService(),
    payment=ZarinpalAdapter(),
    delivery=SnappBoxAdapter(),
    notifier=SMSDecorator(EmailNotifier()),
    kitchen=KitchenFacade(),
)


result = facade.place_order(order)

print(result)
