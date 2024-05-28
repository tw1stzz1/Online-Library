# Сайт - онлайн библиотека фантастики
На сайте можно почитать книги жанра фантастика и скачать их. Книги взяты с сайта [tululu](https://tululu.org).

### Запуск сайта онлайн
Для запуска сайта онлайн и ознакомлением с его функционалом вы можете воспользоваться этой [ссылкой](https://tw1stzz1.github.io/Online-Library/pages/index1.html)

### Запуск сайта оффлайн
Для запуска сайта оффлайн вам нужно скачать его
1. На github странице этого проекта нажмите на кнопку Code
2. Выйдет три варианта скачивания - клонировать файлы проекта на компьютер с помощью ссылки, клонировать с помощью приложения GitHub Desktop или скачать zip-архив. Остальные шаги будут описывать установку через приложение [GitHub Desktop](https://central.github.com/deployments/desktop/desktop/latest/win32)
3. После того как вы нажмете на кнопку Open with GitHub Desktop, у вас откроется приложение GitHub Desktop (если оно установлено на компьютер) в котором откроется окно клонирования репозитория. В нем будет поле local path в котором вы сможете выбрать путь установки нажав на кнопку Choose...
4. После нажмите на кнопку Clone для установки
5. Затем откройте этот репозиторий в Проводнике и откройте папку pages.
6. Откройте любой из файлов в ней и пользуйтесь сайтом!
### Редактирование кода
Для редактирования сайта вам нужно установить его как в шаге "Запуск сайта оффлайн"

Затем установите зависимости используя pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
После установки зависимотей вы можете запустить сайт коммандой:
```
python render_website.py
```
Эта комманда выдает ссылку на сайт:
```
Serving on http://127.0.0.1:5500
```
Редактировать сайт вы можете в файле `template.html`.
Входные данные берутся из файла `books_parameters.json`

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
