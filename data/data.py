from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/api/data')
def data():
    x = [i for i in range(10)]
    y = [random.randint(0, 100) for _ in range(10)]
    data = [{'x': xi, 'y': yi} for xi, yi in zip(x, y)]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

