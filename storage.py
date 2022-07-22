import pymongo


class StorageSystem:
    def __init__(self, mongo_connection_string):
        self.events_db = pymongo.MongoClient(mongo_connection_string).events
        self.supported_events = ['PairCreated']

    @property
    def PairCreated(self):
        return self.events_db['PairCreated']

    def get_events_by_tx(self, tx):
        document = self.PairCreated.find_one(
            {'event_data.transactionHash': tx},
            {'event_data': 1}
        )
        if document:
            return document['event_data']
        return None

    def get_events_by_contract(self, contract_address):
        cursor = self.PairCreated.find(
            {'event_data.address': contract_address},
            {'event_data': 1})
        output_data = list()
        for document in cursor:
            output_data.append(document['event_data'])
        return output_data
