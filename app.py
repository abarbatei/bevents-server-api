import http
import os
from storage import StorageSystem
from flask import Flask, request

app = Flask(__name__)

storage = StorageSystem(os.environ['MONGO_DB_CONNECTION_STRING'])


@app.route('/')
def index():
    return 'Home page'


@app.route('/get-events/tx/<tx_hash>', methods=['GET'])
def get_events_tx(tx_hash=None):
    if not tx_hash:
        return 'success', 200
    res = storage.get_events_by_tx(tx_hash)
    if res:
        return res, 200, {'Content-Type': 'application/json; charset=utf-8'}

    return '', http.HTTPStatus.NO_CONTENT


@app.route('/get-events/query', methods=['GET'])
def get_events():
    contract_address = request.args.get('address')
    result = storage.get_events_by_contract(contract_address=contract_address)

    response = {
        "found_count": len(result),
        'events': result
    }
    return response, 200, {'Content-Type': 'application/json; charset=utf-8'}


if __name__ == '__main__':
    app.run()
