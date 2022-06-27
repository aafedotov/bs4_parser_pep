class ParserFindTagException(Exception):

    """Вызывается, когда парсер не может найти тег."""
    pass


class NoneRequestException(Exception):

    """Вызывается, когда пришел пустой ответ от сервера."""
    pass

