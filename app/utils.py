import base64

import requests
from flask import jsonify

from app.constants import STATUS_OK, STATUS_BAD_REQUEST, STATUS_FORBIDDEN


class Response():
    ''' Make response helper '''
    @staticmethod
    def jsonify(status=STATUS_OK, message="", data=None):
        """ Make a response with status.
            Default status=200 mean success.
            If status!=200 then reponse should have a message to show the error.
        """
        output = {}
        if message:
            output["message"] = message
        if data is not None:
            output["data"] = data

        return jsonify(output), status

    @staticmethod
    def bad_request(message="Bad request."):
        """ Return status 400. Bad request. """
        return Response.jsonify(STATUS_BAD_REQUEST, message=message)

    @staticmethod
    def permission_declined(message="Permission declined."):
        """ Return status 403. User dont have permission to do something. Example: user dont own the study. """
        return Response.jsonify(STATUS_FORBIDDEN, message=message)