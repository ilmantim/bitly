# Обрезка ссылок с помощью Битли

Консольная утилита, сокращающая ссылки. Также может вывести количество кликов сокращенной ссылки.

## Как установить

Создайте файл .env в корневом каталоге проекта и укажите в нём токен для взаимодйствия с API [Bitly](https://app.bitly.com/Bn61cRr7yT8/onboard/).

Например:
BITLY_TOKEN=17c09e20ad155405123ac1977542fecf00231da7

GENERIC ACCESS TOKEN — нужный тип токена. 
Для его получения зарегистрируйтесь на сайте [Bitly](https://app.bitly.com/Bn61cRr7yT8/onboard/) и воспользуйтесь 
[генератором токенов](https://app.bitly.com/Bn61cRr7yT8/onboard/)


Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).