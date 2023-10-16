from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def inicio():
    return jsonify({'message': 'Hola mundo'}), 200


if __name__ == '__main__':
    app.run(debug=True)