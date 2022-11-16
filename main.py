from entity.abstract_storage import AbstractStorage
from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import BaseError

store = Store(items={'картошка': 10, 'печенье':20}, capacity=100)
shop = Shop(items={'печенье': 5}, capacity=100, max_unique_items=5)

storages: dict[str, AbstractStorage] = {'склад': store,
                                        'магазин': shop}

def main():
    print('Добрый день!\n')

    while True:

        for storage_name, storage in storages.items():
            print(f'В {storage_name} хранится: \n{storage.get_items()}')

        raw_request: str = input(f'Введите запрос в формате "Доставить 3 печенье из склад в магазин"\n'
                                 'Введите "stop" или "стоп", чтобы закончить:')

        if raw_request in ["stop", "стоп"]:
            break

        try:
            request = Request(request=raw_request, storages=storages)
        except BaseError as e:
            print(e.message)
            continue

        courier = Courier(request=request, storages=storages)
        try:
            courier.move()
        except BaseError as e:
            print(e.message)

if __name__ == '__main__':
    main()