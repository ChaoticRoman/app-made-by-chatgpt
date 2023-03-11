import random

from flask import Flask, jsonify

app = Flask(__name__)


def generate_data():
    x = [i for i in range(10)]
    y = [random.randint(0, 100) for _ in range(10)]
    return [{'x': xi, 'y': yi} for xi, yi in zip(x, y)]


@app.route('/api/data')
def data():
    return jsonify(generate_data())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
