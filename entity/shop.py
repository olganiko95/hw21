from entity.base_storage import BaseStorage
from exceptions import TooManyProductsError


class Shop(BaseStorage):

    def __init__(self, items: dict[str, int], capacity: int, max_unique_items: int):
        self.max_unique_items = max_unique_items
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= self.max_unique_items:
            raise TooManyProductsError

        super().add(name, amount)