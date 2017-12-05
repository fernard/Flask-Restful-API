from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return  {'message': 'Store not found'}, 404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message': 'Store %s already exists' % name}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except Exception:
            return {'message': 'An error occured while creating'}, 500
        return {'message': 'Store has been created'}, 201

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete()
            except Exception:
                return {'message': 'An error occured while deleting'}, 500

        return {'message': 'Store has been deleted'}, 200



class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}

