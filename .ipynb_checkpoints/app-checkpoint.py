from flask import Flask, jsonify
import pickle

model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello world!"


@app.route('/api/data1/<int:data1>/data2/<int:data2>/data3/<int:data3>/data4/<int:data4>', methods=['GET'])
def predict2(data1, data2, data3, data4):
    prediction = model.predict([[data1, data2, data3, data4]])

    if prediction[0] == 0:
        name = "Setosa"
    else:
        name = "Versicolor"

    response = {
        'prediction': {
            'type': str(prediction[0]),
            'name': name
        }
    }

    print(prediction[0])
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)