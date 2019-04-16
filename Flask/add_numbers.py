from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route(r"/", methods=["GET"])
def addition():
    try:
        a = int(request.args.get("a", None))
        b = int(request.args.get("b", None))
        return jsonify(result=a + b)
    except TypeError:
        return app.response_class(
            response="Należy podać parametr a i b",
            status=400)
    except ValueError:
        return app.response_class(
            response="a i b muszą być liczbami całkowitymi",
            status=406)


@app.errorhandler(404)
def pageNotFound(e):
    return app.response_class(
        response="Podano niepoprawny adres URL",
        status=404)


if __name__ == "__main__":
    app.run(debug=False, port=8080)
