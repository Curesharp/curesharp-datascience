from flask import Flask, request, jsonify, json
import pickle
import traceback
import os
import json


app = Flask(__name__)


@app.route("/")
def home():
    return "Bem vindo a home de Machine Learning da Cure Sharp."


@app.route("/maternal", methods=['POST', 'GET'])
def maternal():
    if request.method == 'POST':
        try:

            # Pegando path
            with open('./paths.txt', 'r') as arquivo:
                paths = json.load(arquivo)
            path = paths['maternal']
            filename = os.path.abspath(path)

            # Carregando modelo e fazendo predição
            model = pickle.load(open(filename, 'rb'))
            user_input = json.loads(request.data)
            prediction = model.predict([[value for key, value in user_input.items()]])

            result = {
                "risco": prediction[0]
            }

            return jsonify(result), 200

        except IOError:
            return jsonify({'trace': traceback.format_exc()})

    else:
        return "Faça uma requisição do tipo POST."


@app.route("/fetal", methods=['POST', 'GET'])
def fetal():
    if request.method == 'POST':
        try:

            # Pegando path
            with open('./paths.txt', 'r') as arquivo:
                paths = json.load(arquivo)
            path = paths['fetal']
            filename = os.path.abspath(path)

            # Carregando modelo e fazendo predição
            model = pickle.load(open(filename, 'rb'))
            user_input = json.loads(request.data)
            prediction = model.predict([[value for key, value in user_input.items()]])

            result = {
                "saudeFeto": prediction[0]
            }

            return jsonify(result), 200

        except IOError:
            return jsonify({'trace': traceback.format_exc()})

        except json.decoder.JSONDecodeError:
            return jsonify({'trace': traceback.format_exc()})

    else:
        return "Faça uma requisição do tipo POST."


if __name__ == '__main__':
    app.run(debug=True)
