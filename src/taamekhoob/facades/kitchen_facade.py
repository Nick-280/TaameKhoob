"""Kitchen facade. modiriate saffhe ashpazkhane va vaziate sefaresh ha"""

from taamekhoob.order.order import Order


class KitchenFacade:
    """facade baraye ashpazkhane- saf, ready va queue"""

    def __init__(self) -> None:
        self._queue = []
        self._ticket_counter = 1000

    def queue(self, order: Order) -> str:
        """sefaresh ro be saf ezafe mikone.
        va ticket ro baraye peigiri bar migardoone"""

        self._ticket_counter += 1
        ticket = f"K-{self._ticket_counter}"
        self._queue.append({"ticket": ticket, "order": order, "status": "pending"})

        return ticket

    def mark_ready(self, ticket: str) -> bool:
        """vaziate sefaresh ro be 'ready' taghir mide.
        dar surat vojud sefaresh True mide vagarna False"""

        for item in self._queue:
            if item["ticket"] == ticket:
                item["status"] = "ready"

                return True
        return False

    def current_queue(self) -> list:
        """list hame sefaresh haye dar entezar ro barmigardoone
        baraye namayesh dar UI"""

        result = []
        for item in self._queue:
            result.append({"ticket": item["ticket"], "status": item["status"]})
        return result
