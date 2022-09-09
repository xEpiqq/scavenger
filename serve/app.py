from flask import Flask
from flask_cors import CORS, cross_origin


data = {'name': 'jayden', 'email': 'jayden@example.com', 'password': 'cant tell you, son'}

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/", methods=['GET'])
@cross_origin(supports_credentials=True)
def homePage():
    return data

if __name__ == "__main__":
    app.run(debug=True, port=8090)