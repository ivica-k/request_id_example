from flask import Blueprint, request, current_app
from flask_restful import Resource, Api

simple_blueprint = Blueprint("simple", __name__)
api = Api(simple_blueprint)



class GetHeadersWorking(Resource):
    def get(self):
        return {
            "status":  "headers",
            "message": request.headers  # this will raise TypeError: Object of type EnvironHeaders is not JSON serializable but will show the request_id
        }
    
    
class GetHeadersNotWorking(Resource):
    def get(self):
        return {
            "status":  "headers",
            "message": list(request.headers)
        }
    
api.add_resource(GetHeadersWorking, "/working")
api.add_resource(GetHeadersNotWorking, "/notworking")
