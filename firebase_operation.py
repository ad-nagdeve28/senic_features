import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import google.cloud.extended_operations_pb2


class FirebaseOperation():

    def __init__(self):
        self.app = firebase_admin.initialize_app(self.firebase_auth())
        self.store = firestore.client()
        self.collection = self.store.collection(u'products')

    def firebase_auth(self):
        return credentials.Certificate('senic-gross-market-firebase-adminsdk-fbsvc-7236c09a61.json')


    def fetch_products(self):
        product = self.collection.get()
        return product

