from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
import json

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)


class Product(db.Document):
    # Модель товара
    id = db.IntField(primary_key=True)
    name = db.StringField(required=True)
    about = db.StringField()
    param = db.ListField()


def add_prod(name, about, param):
    # Функция для добавления нового товара в базу данных с автоинкрементированием id
    new_prod = Product(name=name, about=about, param=param)
    if Product.objects.order_by("-id").first():
        last = Product.objects.order_by("-id").first()
        new_prod.id = last.id + 1
    else:
        new_prod.id = 1
    new_prod.save()
    return new_prod


@app.route('/add', methods=['POST'])
def add():
    # Метод добавления товара
    record = json.loads(request.data)
    new_prod = add_prod(record['name'], record['about'], record['param'])
    return jsonify(new_prod.to_json())


@app.route('/get_id', methods=['GET'])
def get_id():
    # Метод поиска товара по id
    id = json.loads(request.data)['id']
    products = Product.objects(id=id)
    if not products:
        return jsonify({'Error': 'Not Found'})
    else:
        return jsonify(products.to_json())


@app.route('/get_name', methods=['GET'])
def get_name():
    # Метод поиска товаров по части названия
    name = json.loads(request.data)['name']
    products = Product.objects(name__contains=name)
    if not products:
        return jsonify({'Error': 'Not Found'})
    else:
        return jsonify(products.to_json())


@app.route('/get_param', methods=['GET'])
def get_param():
    # Метод поиска товаров по параметру и его значению
    param = json.loads(request.data)['param']
    products = Product.objects(__raw__={'param': param})
    if not products:
        return jsonify({'Error': 'Not Found'})
    else:
        return jsonify(products.to_json())


if __name__ == '__main__':
    app.run(debug=True)
