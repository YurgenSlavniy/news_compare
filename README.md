# news_compare
`Goal: I want to compare news from all countries of the world`

Автоматический сбор новостей с доступных ресурсов и помещение этих новостей в базу данных (выбрать БД) предположим mySQL.
Приложение работающее с этой базой данных и дающее инструменты для сравнения новосного контента. Тагертирование новостного контента. 

### Амбициозные цели (objectives):
- Собрать новости всех стран мира.
- Реализация веб приложения, в котором пользователь сможет сравнить новости с разных ресурсов, пользуясь инструментами данного приложения
- Реализация телеграмм бота, показывающего новости. 

### ключевые показатели достижения целей (key results). ставятся по SMART (конкретные, измеримые, достижимые, обоснованные и ограниченные по времени)
- количество ресурсов с которых удачно собираются новости (шт)
- количество ВСЕХ собранных новостей в базе данных (число строк в бд)
- количество стран, откуда собираются новости (шт)
- количество ВСЕХ собранных новостей (шт)
- состояние активности веб ресурса: Сайт запущен в режиме отладки = 1 / сайт запущен в режиме веб приложения = 2  / Сайт вообще не запускался = 3 /Сайт переодически запускался и шла работа с кодом = 4
- Телеграмм бот ЗАПУЩЕН=1\НЕЗАПУЩЕН=0
- Документирование наблюдений (количество записей)
- количество шагов (шт)
- количество выполненных шагов (шт)


### Текущие Цели:
- Вспомнить всё, ревизия кода
- создание техзадиния и описательного листа на телеграмм бота 
- запустить локальный сервер и код
- просить помощи от деворя
- собрать заголовки новостей
- собрать новость с текстовым содержанием
- разработать базу данных куда будут помещаться новости
- достать файлы на телеграмм бота которого делал для обучения.
- сделать табличку для key results
- Регулярная работа с административным файлом этим, редактируя эти цели и шаги
- сделать 11 записей в key results

### Первые шаги:

1) `+` Парсер с яндекса. Топ 5 новостей.  `!!!`  Оказывается ни с яндекса ни с мейл ру автоматически собрать данные у меня не получилось. Надо искать источники откуда собирать 5 новостей. 
2) `+` Список СМИ в России и определиться с каких сми собирать новости. Для начала сбор новостей от информационного агенства `РИА новости` - https://ria.ru/
3) `+` Определиться с ресурсами разных стран, откуда брать новости. `!!!` Изучить ресурс https://vsesmi.online где можно ознакомиться с новостными ресурсами разных стран мира - это отличный старт.
4) `+` Список всех стран мира.
5) `+` Политическая карта мира.
6) `+` Работа над сбором новостей с ресурсов из первого списка откуда есть ответ респонс 200
7) создать большой словарь со словарями где будет по странам собраны ссылки и название ресурса.
8) телеграмм бот. реанимировать сущетвующего, найти едьюкейшн бота или создать нового. Бот выдаёт новости, когда пользователь пишет ДА
9) https://github.com/ozandrew/geo-news  - изменить код и спросить Андрея как это правильно сделать
10) `+` Прогнать проект через OKR (Objectives and Key Results — «цели и ключевые результаты»)
11) ревизия кода. Разобраться с папкой проекта. 
12) создание файла key results где будет результирующая таблица. 
13) сделать первую запись в key results
14) найти расположение в ноутбуке своего телеграмм бота
15) повторить 1, 2, 3 урок конспекты по базам данных


# OKR (Objectives and Key Results — «цели и ключевые результаты») OKR 

### Амбициозные цели (objectives):
- Собрать новости всех стран мира.
- Реализация веб приложения, в котором пользователь сможет сравнить новости с разных ресурсов. 
- Реализация телеграмм бота, показывающего новости. 

### ключевые показатели достижения целей (key results). ставятся по SMART (конкретные, измеримые, достижимые, обоснованные и ограниченные по времени)
- количество ресурсов с которых удачно собираются новости (шт)
- количество ВСЕХ собранных новостей в базе данных (число строк в бд)
- количество стран, откуда собираются новости (шт)
- количество ВСЕХ собранных новостей (шт)
- состояние активности веб ресурса: Сайт запущен в режиме отладки / сайт запущен в режиме веб приложения / Сайт вообще не запускался /Сайт переодически запускался и шла работа с кодом 
- Телеграмм бот ЗАПУЩЕН\НЕЗАПУЩЕН

