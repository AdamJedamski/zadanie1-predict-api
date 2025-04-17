from flask import Flask, request, jsonify
from model import predict

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict_route():
    x1 = request.args.get('x1', 0)
    x2 = request.args.get('x2', 0)

    prediction = predict(x1, x2)

    return jsonify({
        'prediction': prediction,
        'features': {
            'x1': float(x1) if x1 else 0,
            'x2': float(x2) if x2 else 0
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)