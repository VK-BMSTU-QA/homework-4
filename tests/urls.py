class Urls:
    BASE_URL = 'https://a06367.ru/'
    PROFILE_URL = 'https://a06367.ru/profile'
    SETTINGS_URL = 'https://a06367.ru/settings'
    LOGIN_URL = 'https://a06367.ru/login'
    SIGNUP_URL = 'https://a06367.ru/signup'

    # TODO: добавьте сюда свои урлы
    def get_film_url(self, name):
        return f'https://a06367.ru/film/{name}'
