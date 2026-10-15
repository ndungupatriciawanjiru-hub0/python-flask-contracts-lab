#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)


# GET /contract/<id> -> 200 with contract info, or 404 if the id is unknown
@app.route('/contract/<int:id>')
def get_contract(id):
    # Loop through contracts looking for a matching id
    for contract in contracts:
        if contract["id"] == id:
            # Found: return only the contract text with a 200 status
            return make_response(contract["contract_information"], 200)
    # Not found: empty-bodied 404
    return make_response("", 404)


# GET /customer/<customer_name> -> 204 (no body, data is sensitive) or 404
@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    if customer_name in customers:
        # Customer exists: confirm with 204 and an empty body
        return make_response("", 204)
    # Customer unknown: 404
    return make_response("", 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
