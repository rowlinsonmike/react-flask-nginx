from flask import Blueprint
from flask import jsonify,request,current_app


def hello():
    bp = Blueprint('hello', __name__)
    @bp.route('/', methods=['GET'])
    def handler():
        def handleGET():
            return "Hello, World!"
        methods = {
                'GET': handleGET, 
            }
        if request.method in methods:
            return methods[request.method]()
        else: 
            return jsonify({"error":"unsupported method"})
    return bp
