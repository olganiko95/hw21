class BaseError(Exception):
    message = 'Что-то пошло не так'

class NotEnoughSpaceError(BaseError):
    message = 'Недостаточно места'

class NotEnoughProductError(BaseError):
    message = 'Недостаточно товара'


class TooManyProductsError(BaseError):
    message = 'Слишком много товара'

class InvalidRequest(BaseError):
    message = 'Неправильный запрос'

class UnknownStorageError(BaseError):
    message = 'Неизвестный склад'