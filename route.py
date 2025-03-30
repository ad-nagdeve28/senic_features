from flask import Blueprint, jsonify, request
from firebase_operation import FirebaseOperation


api = Blueprint('api', __name__)

'''Initializing the clound object'''
fire_cloud = FirebaseOperation()

@api.route('/products', methods=['GET'])
def get_all_products():
    products = fire_cloud.fetch_products()
    return jsonify({product.id : product.to_dict() for product in products})

@api.route('/product/search', methods=['GET'])
def search_product():
    return 