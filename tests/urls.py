class Urls():
    BASE_URL = 'https://volchock.ru'
    PROFILE_URL = 'https://volchock.ru/profile'
    PROFILE_ARCHIVE_URL = 'https://volchock.ru/profile/archive'
    PROFILE_FAVORITE_URL = 'https://volchock.ru/profile/favorite'
    PROFILE_CART_URL = 'https://volchock.ru/profile/cart'
    PROFILE_MESSAGES_URL = 'https://volchock.ru/profile/chat'
    PROFILE_PAID_URL = 'https://volchock.ru/profile/promotion'
    PROFILE_SETTINGS_URL = 'https://volchock.ru/profile/settings'
    NEW_ADVERT_URL = 'https://volchock.ru/newAd'

    def __init__(self) -> None:
        pass

    def salesman_url(self, id: int) -> str:
        return f'https://volchock.ru/salesman/{id}'

    def advert_url(self, id: int) -> str:
        return f'https://volchock.ru/ad/{id}'

    def search_url(self, text: str) -> str:
        return f'https://volchock.ru/search/{text}'

    def category_url(self, text: str) -> str:
        return f'https://volchock.ru/category/{text}'

    def personal_chat_url(self, salesmanId: int, advertId: int) -> str:
        return f'https://volchock.ru/profile/chat/{salesmanId}/{advertId}'

    def promotion_url(self, id: int) -> str:
        return f'https://volchock.ru/ad/{id}/upgrade'
