from flask import Flask, jsonify, request, send_file
from flask_mongoengine import MongoEngine
from flask_cors import CORS, cross_origin
import yaml,io,os,openai,PyPDF2
from backend.utils.jsonResponse import jsonResponse
from backend.utils.tokenFromHeader import tokenFromHeader
from backend.utils.userIdFromtoken import getUseridFromtoken 
from backend.routes.login import loginRoute
from backend.routes.logout import logoutRoute
from backend.routes.signup import signupRoute
from backend.middleware.beforeRequest import beforeRequestMiddleware
from backend.routes.applications import getApplications,addApplication,updateApplication,deleteApplication
from backend.routes.search import searchRoute
from backend.routes.recommend import recommendRoute 
from dotenv import load_dotenv

load_dotenv()

existing_endpoints = ["applications", "resume","recommend"]


def create_app():
    app = Flask(__name__)

    # make flask support CORS
    CORS(app)
    app.config["CORS_HEADERS"] = "Content-Type"

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonResponse("Page not Found",404)

    @app.errorhandler(405)
    def page_not_allowed(e):
        return jsonResponse("Method not allowed",405)
   
    @app.errorhandler(500)
    def internal_server_error(e):
        print("error",e)
        return jsonResponse("server error",500)

    @app.route("/")
    @cross_origin()
    def health_check():
        return jsonResponse("Server up and running",200)

    @app.before_request
    def middleware():
        return beforeRequestMiddleware(request,existing_endpoints,Users) 

    def get_token_from_header():
        return tokenFromHeader(request)


    def get_userid_from_header():
        return getUseridFromtoken(request)

    @app.route("/users/signup", methods=["POST"])
    def sign_up():
        return signupRoute(request,Users)
       
    @app.route("/users/login", methods=["POST"])
    def login():
       return loginRoute(request,Users)


    @app.route("/users/logout", methods=["POST"])
    def logout():
        return logoutRoute(request ,Users)

    # get data from the CSV file for rendering root page
    @app.route("/applications", methods=["GET"])
    def get_data():
        return getApplications(request,Users)


    @app.route("/applications", methods=["POST"])
    def add_application():
        return addApplication(request,Users)

    @app.route("/applications/<int:application_id>", methods=["PUT"])
    def update_application(application_id):
        return updateApplication(request,application_id,Users)
        

    @app.route("/applications/<int:application_id>", methods=["DELETE"])
    def delete_application(application_id):
        return deleteApplication(request,application_id,Users)

    # search function
    # params:
    #   -keywords: string
    @app.route("/search")
    def search():
        return searchRoute(request)
          
    @app.route("/recommend", methods=["GET"])
    def recommend_resume():
        return recommendRoute(request,Users)
        
    @app.route("/resume", methods=["POST"])
    def upload_resume():
        """
        Uploads resume file or updates an existing resume for the user

        :return: JSON object with status and message
        """
        try:
            userid = get_userid_from_header()
            try:
                file = request.files["file"].read()
            except:
                return jsonify({"error": "No resume file found in the input"}), 400

            user = Users.objects(id=userid).first()
            if not user.resume.read():
                # There is no file
                user.resume.put(file)
                user.save()
                return jsonify({"message": "resume successfully uploaded"}), 200
            else:
                # There is a file, we are replacing it
                user.resume.replace(file)
                user.save()
                return jsonify({"message": "resume successfully replaced"}), 200
        except Exception as e:
            print(e)
            return jsonify({"error": "Internal server error"}), 500

    @app.route("/resume", methods=["GET"])
    def get_resume():
        """
        Retrieves the resume file for the user

        :return: response with file
        """
        try:
            userid = get_userid_from_header()
            try:
                user = Users.objects(id=userid).first()
                if len(user.resume.read()) == 0:
                    raise FileNotFoundError
                else:
                    user.resume.seek(0)
            except:
                return jsonify({"error": "resume could not be found"}), 400

            response = send_file(
                user.resume,
                mimetype="application/pdf",
                attachment_filename="resume.pdf",
                as_attachment=True,
            )
            response.headers["x-filename"] = "resume.pdf"
            response.headers["Access-Control-Expose-Headers"] = "x-filename"
            return response, 200
        except:
            return jsonify({"error": "Internal server error"}), 500

    return app


app = create_app()
with open("application.yml") as f:
    info = yaml.load(f, Loader=yaml.FullLoader)
    username = info["username"]
    password = info["password"]
    app.config["MONGODB_SETTINGS"] = {
        "db": "sefall23",
        "host":f"mongodb+srv://{username}:{password}@sefall23proj3.wwrtycq.mongodb.net/"
    }
    print(app.config["MONGODB_SETTINGS"],"mongodb settings ")

db = MongoEngine()
db.init_app(app)


class Users(db.Document):
    """
    Users class. Holds full name, username, password, as well as applications and resumes
    """

    id = db.IntField(primary_key=True)
    fullName = db.StringField()
    username = db.StringField()
    password = db.StringField()
    authTokens = db.ListField()
    applications = db.ListField()
    resume = db.FileField()

    def to_json(self):
        """
        Returns the user details in JSON object

        :return: JSON object
        """
        return {"id": self.id, "fullName": self.fullName, "username": self.username}


if __name__ == "__main__":
    app.run(debug=True)
