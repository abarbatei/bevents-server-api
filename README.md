# bevents-server-api
A basic webserver API POC for general use in the [blockchain-event-processor](https://github.com/abarbatei/blockchain-event-processor) project.

Server is made with [Flask](https://flask.palletsprojects.com/), 
retrieves data from the MongoDB specified in the [bevents-index-processor MongoDB setup](https://github.com/abarbatei/bevents-index-processor#mongodb-setup-and-interaction)

Connection to the MongoDB server requires a corresponding [MongoDB connection string](https://www.mongodb.com/docs/manual/reference/connection-string/) to be set in an environment variable named  `MONGO_DB_CONNECTION_STRING`.

## Functionality

Currently the server supports following routes:

***
`/get-events/tx/<tx_hash>`
- *tx_hash* - a transaction hash for an event stored vy the project
- example (considering the flask server running locally): 
```
wget "http://127.0.0.1:5000/get-events/tx/0x96de10f8d6dc1989657d4f98ad9aa31bdc6cd51cef26bb4f3ca10aa776c324a9"
``` 
Response
```json
{
    "address": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",
    "args": {
        "": 82340,
        "pair": "0xF0E091271Fc75ca7a808eAc7045Ee42459D39690",
        "token0": "0x8B0d396A5FF25253e80Ac7589260122c2868c091",
        "token1": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    },
    "blockHash": "0x746fc57d70250ce1d84fdfef411a7b5a53897dacc2031db5e4ba7138ce7a60de",
    "blockNumber": 15191467,
    "event": "PairCreated",
    "logIndex": 576,
    "transactionHash": "0x96de10f8d6dc1989657d4f98ad9aa31bdc6cd51cef26bb4f3ca10aa776c324a9",
    "transactionIndex": 273
}

```
If the TX is not found, the API returns `204 NO CONTENT`

***
`/get-events/query?address=<smart_contract_address>`
- *address* - the smart contract on-chain address that emitted the event 

Response format
```
{
  "found_count": <number of events found that were emitted by this smart contract>,
  "events": <list of the actual events in the format shown above>
}
```
Example query (considering the flask server running locally):
```
wget "http://127.0.0.1:5000/get-events/query?address=0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
``` 

Example response
```json
{
    "events": [
        {
            "address": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",
            "args": {
                "": 82340,
                "pair": "0xF0E091271Fc75ca7a808eAc7045Ee42459D39690",
                "token0": "0x8B0d396A5FF25253e80Ac7589260122c2868c091",
                "token1": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
            },
            "blockHash": "0x746fc57d70250ce1d84fdfef411a7b5a53897dacc2031db5e4ba7138ce7a60de",
            "blockNumber": 15191467,
            "event": "PairCreated",
            "logIndex": 576,
            "transactionHash": "0x96de10f8d6dc1989657d4f98ad9aa31bdc6cd51cef26bb4f3ca10aa776c324a9",
            "transactionIndex": 273
        },
        ...
        {
            "address": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",
            "args": {
                "": 82340,
                "pair": "0xF0E091271Fc75ca7a808eAc7045Ee42459D39690",
                "token0": "0x8B0d396A5FF25253e80Ac7589260122c2868c091",
                "token1": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
            },
            "blockHash": "0x746fc57d70250ce1d84fdfef411a7b5a53897dacc2031db5e4ba7138ce7a60de",
            "blockNumber": 15191467,
            "event": "PairCreated",
            "logIndex": 576,
            "transactionHash": "0x96de10f8d6dc1989657d4f98ad9aa31bdc6cd51cef26bb4f3ca10aa776c324a9",
            "transactionIndex": 273
        }
    ],
    "found_count": 102
}

```
---

## Setup

Project requires 
- all previous requirements/setups for all projects included in the [blockchain-event-processor](https://github.com/abarbatei/blockchain-event-processor)
- copy/download the project, ensure the required environment variables are set and deploy the project. Example shell launch:
```shell
git clone https://github.com/abarbatei/bevents-server-api
cd ./bevents-server-api
pip install -r /requirements.txt
./start.sh
```

The `start.sh` script just sets the required environment variable, as mentioned above.