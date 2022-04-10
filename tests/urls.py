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

    def salesmanUrl(self, id: int) -> str:
        return f'https://volchock.ru/salesman/{id}'

    def advertUrl(self, id: int) -> str:
        return f'https://volchock.ru/ad/{id}'

    def searchUrl(self, text: str) -> str:
        return f'https://volchock.ru/search/{text}'

    def categoryUrl(self, text: str) -> str:
        return f'https://volchock.ru/category/{text}'
    
    def personalChatUrl(self, salesmanId: int, advertId: int) -> str:
        return f'https://volchock.ru/profile/chat/{salesmanId}/{advertId}'