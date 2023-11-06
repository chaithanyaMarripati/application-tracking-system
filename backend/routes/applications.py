from flask import Request, jsonify
from backend.utils.userIdFromtoken import getUseridFromtoken

def getApplications(request:Request, Users):
    """
    Gets user's applications data from the database

    :return: JSON object with application data
    """
    try:
        userid = getUseridFromtoken(request)
        user = Users.objects(id=userid).first()
        applications = user["applications"]
        return jsonify(applications)
    except:
        return jsonify({"error": "Internal server error"}), 500
