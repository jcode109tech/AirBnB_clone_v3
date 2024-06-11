#!/usr/bin/pyhton3 


from flask import jsonify, request
from api.v1.views import app_views
from models import storage

@app_views.route('/status', methods=['GET'])
def get_status():
    """Return the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def get_stats():
    """
        Returns count of class objects
    """
    if request.method == 'GET':
        responce = {}
        To_count = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in To_count.items():
            responce[value] = storage.count(key)
        return jsonify(responce)

