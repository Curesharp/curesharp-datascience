from flask import Flask, request, jsonify
import pickle
import traceback
import json


app = Flask(__name__)


@app.route("/")
def home():
    return "Bem vindo a home de Machine Learning da Cure Sharp."


@app.route("/materno", methods=['POST', 'GET'])
def materno():
    if request.method == 'POST':
        try:

            # Pegando path
            with open('./paths.txt', 'r') as arquivo:
                paths = json.load(arquivo)
            path = paths['maternal']

            # Carregando modelo e fazendo predição
            model = pickle.load(open(path, 'rb'))
            user_input = request.get_json()
            prediction = model.predict([user_input])

            result = {
                "riscoGravidez": prediction
            }

            return jsonify(result), 200

        except IOError:
            return jsonify({'trace': traceback.format_exc()})

    else:
        return "Faça uma requisição do tipo POST."


if __name__ == '__main__':
    app.run(debug=True)
