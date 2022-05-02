# Чек-листы. Patreon
## Команда GoToV
- Варин Дмитрий :sunglasses:
- Ветошкин Артем :blush:
- Ларин Владимир :grinning:
- Нурхаметова Камила :princess:

## Ссылка на проект
[Patreon](https://pyaterochka-team.site/)

## Чек-листы
### Чек-лист №1 (Варин Дмитрий)
#### Тестируемые страницы
1. [Страница входа](https://pyaterochka-team.site/signin)

2. Страницы редактирования:

- [профиля](https://pyaterochka-team.site/edit)

- [автора](https://pyaterochka-team.site/profile/edit/creator_settings)

#### Вход и редактирование профиля
- [x] Войти в существующий аккаунт
    - [ ] Убедиться в появлении ошибки валидации
- [x] Изменить фотографию основного профиля
  - [ ] Загрузить файл, не являющийся картинкой
  - [ ] Убедиться в появлении ошибки валидации
  - [ ] Загрузить файл, являющийся картинкой 
- [x] Изменить фотографию профиля автора, отличную от фото основного профиля
  - [ ] Загрузить файл, не являющийся картинкой
  - [ ] Убедиться в появлении ошибки валидации
  - [ ] Загрузить файл, являющийся картинкой 
- [x] Проверить, что фото автора/основного профиля отличаются
- [x] Сменить пароль 
  - [ ] Проверить, что изменение пароля валидируется
  - [ ] Зайти в аккаунт с новым паролем
  - [ ] Сменить на старый пароль
  - [ ] Войти снова

### Чек-лист №2 (Ларин Владимир)

- [Добавление поста](https://pyaterochka-team.site/post/create)


#### Добавление поста и редактирование поста
- [ ] Войти в существующий аккаунт автора
- [ ] Нажать кнопку `Панель автора` на странице профиля, который открывается после авторизации
- [ ] Нажать кнопку `Добавить пост`
- [ ] Нажать кнопку `Продолжить`
  - [ ] Убедиться в появлении ошибки валидации
- [ ] Ввести "HELLO WORLD" в текстовое поле `Введите заголовок`
- [ ] Ввести "My description" в текстовое поле `Введите описание`
- [ ] Нажать кнопку `Продолжить`
- [ ] Убедиться в создании черновика поста
  - [ ] Заголовок поста должен быть "HELLO WORLD"
  - [ ] Описание поста должно быть "My description"
  - [ ] У статьи нет загруженных файлов
  - [ ] У статьи нет содержимого
- [ ] Навести мышку на обложку
- [ ] Убедиться в появлении кнопки `Заменить обложку`
- [ ] Нажать на кнопку `Заменить обложку` и загрузить обложку с размером файла больше 20 МБ
- [ ] Убедиться в появлении ошибки загрузки изображения
- [ ] Нажать на кнопку `Заменить обложку` и загрузить обложку записи с размером файла 3 МБ
- [ ] Убедиться в смене картинки обложки изображения на загруженную
  - *Примечание:* качество и размер загруженного на сервер и загруженного с сервера файлов может отличаться, автоматическую проверку реализовать с помощью сравнения короткого имени файла  
- [ ]  Нажать на кнопку `+`

![изображение](https://user-images.githubusercontent.com/12639263/166163027-d415a872-7d4b-460a-8e5e-192bfcc0ae3d.png)
- [ ]  Убедиться в появлении нового блока
- [ ]  Выбрать пустой текстовый блок
- [ ]  Нажать клавишу `Backspace`
- [ ]  Убедиться в удалении данного пустого блока
- [ ]  Нажать на иконку ноты

![изображение](https://user-images.githubusercontent.com/12639263/166163019-340191f0-eae7-42fe-901f-ffc332bd00e0.png)
- [ ]  Убедиться в появлении блока `Загрузить аудио`.
- [ ]  Нажать на блок `Загрузить аудио` и загрузить невалидный файла (валидным считается, файл расширения `.ogg`, `.mp3` не более 20 МБ)
- [ ]  Убедиться в появлении ошибки валидации/загрузки
- [ ]  Нажать на блок `Загрузить аудио` и загрузить валидный файла (валидным считается, файл расширения `.ogg`, `.mp3` не более 20 МБ)
- [ ] Убедиться в загрузке файла
- [ ] Нажать на иконку изображения в пустом блоке
- [ ] Убедиться в появлении блока загрузки изображения.
- [ ] Нажать на блок `Заменить изображение` и загрузить невалидный файл (валидным считается, файл расширения `.png`, `.jpg` не более 20 МБ) 
- [ ] Убедиться в появлении ошибки загрузки
- [ ] Нажать на блок `Заменить изображение` и загрузить валидный файл (валидным считается, файл расширения `.png`, `.jpg` не более 20 МБ) 
- [ ] Убедиться в появлении загруженного изображения
- [ ] Нажать на иконку видео-пленки 
- [ ] Убедиться в появлении блока `Загрузить видео`.
- [ ] Нажать на блок `Загрузить видео`. Загрузить невалидный файла (валидным считается, файл с mime-типом `video/mp4` ,`video/mpeg` ,`video/mpeg4-generic` не более 100 МБ)
- [ ] Убедиться в появлении сообщения об ошибке.
- [ ] Нажать на блок `Загрузить видео`. Загрузить валидный файла (валидным считается, файл с mime-типом `video/mp4` ,`video/mpeg` ,`video/mpeg4-generic` не более 100 МБ)
- [ ] Убедиться в загрузке видео.
- [ ] Ввести текст "THIS TEXT" в пустой текстовый блок
- [ ] Убедиться, что иконки аудио, изображения и видео меняются на иконку корзины.
- [ ] Нажать на кнопку `Сохранить`
- [ ] Убедиться в появлении страницы поста, на странице поста должны присутствовать 
    - [ ] загруженной обложки
    - [ ] загруженного изображения
    - [ ] загруженного видео
    - [ ] текстового блока "THIS TEXT"
- [ ] Нажать кнопку `Редактировать`
- [ ] Убедиться в присутствии на странице
  - [ ] загруженной обложки
  - [ ] загруженного изображения
  - [ ] загруженного видео
  - [ ] текстового блока "THIS TEXT"
- [ ] Нажать на кнопку `удалить`
- [ ] Убедиться в появлении предупреждение об удалении.
- [ ] Нажать кнопку `Отмена`
- [ ] Убедиться в сохранении на странице загруженных обложки, изображения, видео и введенного текстового блока "THIS TEXT"
- [ ] Нажать на кнопку `удалить`
- [ ] Нажать на кнопку `удалить`
- [ ] убедиться в переходе в панель автора
- [ ] убедиться в отсутствии поста "HELLO WORLD" в списке постов

### Чек-лист №3 (Ветошкин Артем)
#### Добавление уровня и редактирование уровня
1. [Страница входа](https://pyaterochka-team.site/signin)
2. [Страница аккаунта автора](https://pyaterochka-team.site/profile/edit/creator_settings)
3. [Страница создания уровня](https://pyaterochka-team.site/profile/creator/level/create)
4. [Страница редактирования уровня](https://pyaterochka-team.site/profile/creator/level/edit/2)

- [ ] Войти в существующий аккаунт автора
- [ ] Нажать кнопку `Настройки` в выпадающем меню пользователя
- [ ] Выбрать вкладку `Аккаунт автора`
- [ ] Нажать на иконку `Добавить уровень подписки`
- [ ] Ввести "Первый уровень" в текстовое поле `Название уровня`
- [ ] Ввести "Хорошее преимущество" в текстовое поле `Название преимущества`
- [ ] Нажать на кнопку `Заменить обложку` и загрузить обложку с размером файла больше 20 МБ
- [ ] Убедиться в появлении ошибки загрузки изображения
- [ ] Нажать на кнопку `Заменить обложку` и загрузить обложку записи с размером файла 3 МБ
- [ ] Убедиться в смене картинки обложки изображения на загруженную
- [ ] Нажать на кнопку `Добавить преимущество`
- [ ] Убедиться в появлении дополнительного поля `Название преимущества`
- [ ] Ввести "Второе хорошее преимущество" в текстовое поле `Название преимущества`
- [ ] Ввести "Привет мир" в текстовое поле `Стоимость подписки в месяц, рубли`
- [ ] Убедиться в появлении ошибки об некоректном значении поля
- [ ] Заменить текст в поле `Стоимость подписки в месяц, рубли` на "20"
- [ ] Убедиться в работе предпросмотра уровня
  - [ ] Заголовок карточки должен быть "Первый уровень"
  - [ ] Первое преимущество в карточке должно быть "Хорошее преимущество"
  - [ ] Второе преимущество в карточке должно быть "Второе хорошее преимущество"
  - [ ] Цена уровня подписки должна быть "20"
- [ ] Нажать кнопку `Сохранить`
- [ ] Убедиться в появлении уровня в списке уровней подписки
  - [ ] Заголовок карточки должен быть "Первый уровень"
  - [ ] Первое преимущество в карточке должно быть "Хорошее преимущество"
  - [ ] Второе преимущество в карточке должно быть "Второе хорошее преимущество"
  - [ ] Цена уровня подписки должна быть "20"
- [ ] Нажать кнопку `Редактировать уровень`
- [ ] Ввести "Редактированный уровень" в текстовое поле `Название уровня`
- [ ] Ввести "Редактированное преимущество" в первое текстовое поле `Название преимущества`
- [ ] Нажать на иконку крестика во второе текстовое поле `Название преимущества`
- [ ] Убедиться в исчезновении второго текстового поля `Название преимущества`
- [ ] Нажать на кнопку `Заменить обложку` и загрузить обложку с размером файла больше 20 МБ
- [ ] Убедиться в появлении ошибки загрузки изображения
- [ ] Нажать на кнопку `Заменить обложку` и загрузить обложку записи с размером файла 3 МБ
- [ ] Убедиться в смене картинки обложки изображения на загруженную
- [ ] Нажать на кнопку `Добавить преимущество`
- [ ] Убедиться в появлении дополнительного поля `Название преимущества`
- [ ] Ввести "Третье редактированное преимущество" во новое текстовое поле `Название преимущества`
- [ ] Ввести "Привет мир" в текстовое поле `Стоимость подписки в месяц, рубли`
- [ ] Убедиться в появлении ошибки об некоректном значении поля
- [ ] Заменить текст в поле `Стоимость подписки в месяц, рубли` на "30"
- [ ] Убедиться в работе предпросмотра уровня
  - [ ] Заголовок карточки должен быть "Редактированный уровень"
  - [ ] Первое преимущество в карточке должно быть "Редактированное преимущество"
  - [ ] Второе преимущество в карточке должно быть "Третье редактированное преимущество"
  - [ ] Цена уровня подписки должна быть "30"
- [ ] Нажать кнопку `Сохранить`
- [ ] Убедиться в извенение уровня в списке уровней подписки
  - [ ] Заголовок карточки должен быть "Редактированный уровень"
  - [ ] Первое преимущество в карточке должно быть "Редактированное преимущество"
  - [ ] Второе преимущество в карточке должно быть "Третье редактированное преимущество"
  - [ ] Цена уровня подписки должна быть "30"
- [ ] Нажать кнопку `Редактировать уровень`
- [ ] Нажать кнопку `Удалить`
- [ ] Нажать кнопку `Отменить`
- [ ] Нажать кнопку `Сохранить`
- [ ] Убедиться в неизменности уровня в списке уровней подписки
  - [ ] Заголовок карточки должен быть "Редактированный уровень"
  - [ ] Первое преимущество в карточке должно быть "Редактированное преимущество"
  - [ ] Второе преимущество в карточке должно быть "Третье редактированное преимущество"
  - [ ] Цена уровня подписки должна быть "30"
- [ ] Нажать кнопку `Редактировать уровень`
- [ ] Нажать кнопку `Удалить`
- [ ] Нажать кнопку `Удалить`
- [ ] Убедиться в отсутсвии уровня в списке уровней подписки

### Чек-лист №4 (Нурхаметова Камила)
#### Тестируемые страницы
1. [Страница поиска](https://pyaterochka-team.site/search)
2. [Страница подписки](https://pyaterochka-team.site/payment/21/18)
- [ ] Войти в существующий аккаунт автора
- [ ] Нажать кнопку `Искать` на панели "Найдите новых креаторов"
- [ ] Выбрать категорию "Подкасты" из выпадающего списка `Категории`
  - [ ] Убедиться, что отображаются авторы только выбранной категории (исходя из описания)
- [ ] Выбрать категорию "Любая категория" из выпадающего списка `Категории`
- [ ] Начать набирать "v" в `Поле поиска`
  - [ ] Убедиться, что выводятся только авторы с именем, начинающимся на букву "v"
![Screenshot from 2022-05-01 19-13-17](https://user-images.githubusercontent.com/59199486/166154645-f3a1391a-f28a-46fb-9ba9-ffae442eabbb.png)
- [ ] Выбрать любого автора, нажав на его карточку 
- [ ] Нажать на кнопку `Поделиться аккаунтом`
  - [ ] Убедиться, что выводится информация о том, что ссылка скопирована
![Screenshot from 2022-05-01 19-05-47](https://user-images.githubusercontent.com/59199486/166154404-b4f085af-e10f-425b-a6cd-f3d35a693e14.png)
- [ ] Нажать на кнопку `Выбрать уровень`
- [ ] Убедиться, что открывается страница с предложением об оформлении подписки
- [ ] Нажать на кнопку `Оформить подписку`
- [ ] Убедиться, что открывается страница для заполнения данных карты
- [ ] Найти на странице автора доступную запись и нажать на кнопку `Открыть материал`
- [ ] Убедиться, что открывается запись поста
- [ ] Найти на странице автора закрытую запись (с замочком) и нажать на кнопку `Открыть материал`
- [ ] Убедиться, что открывается страница с предложением об оформлении подписки
- [ ] Нажать на кнопку `Оформить подписку`
- [ ] Убедиться, что открывается страница для заполнения данных карты
