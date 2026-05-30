"""Reporting facade. report haye sade az foroosh va amalkard system"""


class ReportingFacade:
    """facade baraye gereftane report haye sade"""

    def __init__(self) -> None:
        self._sales = []
        self._orders = []
        self._prep_times = []

    def add_sales(self, amount: float) -> None:
        """mablagh foroosh ro zakhire mikone"""

        self._sales.append(amount)

    def add_order(self, item_name: str) -> None:
        """esm item haye foroosh rafte ro zakhire mikone"""

        self._orders.append(item_name)

    def add_prep_time(self, minutes: int) -> None:
        """zamane amade sazi ro zakhire mikone"""

        self._prep_times.append(minutes)

    def daily_sales(self) -> float:
        """majmooe foroosh ro bar migardoone"""

        return sum(self._sales)

    def weekly_sales(self) -> float:
        """majmooe foroosh hafte ghabl ro bar migardoone"""

        return self.daily_sales() * 7

    def monthly_sales(self) -> float:
        """majmooe foroosh mahe ghabl ro bar migardoone"""

        return self.daily_sales() * 30

    def top_items(self, n: int) -> list[str]:
        """porforoosh tarin item ha ro bar migardoone"""

        counts = {}
        for item in self._orders:
            counts[item] = counts.get(item, 0) + 1

        sorted_items = sorted(counts, key=counts.get, reverse=True)
        return sorted_items[:n]

    def avg_prep_time(self) -> float:
        """miyangine zamane amade sazi ro hesab mikone"""

        if not self._prep_times:
            return 0

        return sum(self._prep_times) / len(self._prep_times)
