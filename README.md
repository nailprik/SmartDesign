<h1>Тестовое задание SmartDesign</h1>
Микросервис для электронного магазина
<h3>Установка</h3>
Для установки нужно с помощью git клонировать приложение:

```sh
$ git clone https://github.com/nailprik/SmartDesign
$ cd SmartDesign
```

Далее установить необходимые зависимости и модули:

```sh
$ pip install -r requirements.txt
```

<h3>Запуск</h3>
Для запуска нужно запустить файл app.py

```sh
$ python app.py
```

<h3>Реализованные методы</h3>

* Создание нового товара

Добавление нового товара осуществляется с помощью PUT запроса на адрес http://localhost:5000/add
```sh
$ curl --header "Content-Type: application/json"   --request PUT   --data '{"name":"Phone","about":"Smartphone","param":[{"Internet":"5G"},{"Display":"Amoled"}]}'   http://localhost:5000/add
```
Метод возвращает данные из базы данных по новому добавленному товару

```sh
"{\"_id\": 1, \"name\": \"Phone\", \"about\": \"Smartphone\", \"param\": [{\"Internet\": \"5G\"},{\"Display\": \"Amoled\"}]}"
```

* Метод для фильтрации по имени

Метод принимает JSON запрос в формате {"name": %name%} , где %name% - искомоме название
```sh
$ curl --header "Content-Type: application/json"   --request GET   --data '{"name":"Phone"}'   http://localhost:5000/get_name
```
Метод возвращает данные из базы данных по найденным товарам

```sh
"{\"_id\": 1, \"name\": \"Phone\", \"about\": \"Smartphone\", \"param\": [{\"Internet\": \"5G\"},{\"Display\": \"Amoled\"}]}"
```

* Метод нахождения товаров по параметру и его значению

Метод принимает JSON запрос в формате {"param": {%param%: %value%}} , где %param% - искомый параметр, а %value% - его значение.

```sh
$ curl --header "Content-Type: application/json"   --request GET   --data '{"param": {%param%: %value%}}'   http://localhost:5000/get_param
```

Метод возвращает данные из базы данных по найденным товарам

* Метод нахождения товара по id

Метод принимает JSON запрос в формате {"id": %id%} , где %id% - искомый идентификатор

```sh
$ curl --header "Content-Type: application/json"   --request GET   --data '{"id":%id%}'   http://localhost:5000/get_id
```
Метод возвращает данные из базы данных по найденному товару



