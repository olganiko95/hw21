from entity.abstract_storage import AbstractStorage
from exceptions import InvalidRequest, UnknownStorageError


class Request:
    def __init__(self, request: str, storages: dict[str, AbstractStorage]):
        split_request: list[str] = request.strip().lower().split(' ')
        if len(split_request) != 7:
            raise InvalidRequest
        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.departure = split_request[4]
        self.destination = split_request[6]

        if self.departure not in storages or self.destination not in storages:
            raise UnknownStorageError