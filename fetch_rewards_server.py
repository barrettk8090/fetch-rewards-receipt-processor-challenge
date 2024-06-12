from flask import Flask, request, jsonify
from points_calculator import calculate_total_receipt_points
import uuid 

app = Flask(__name__)

# Use a dictionary to store our receipt data for the purposes of this assignment.
receipts = {}

# Route for processing of receipt JSON. Returns an ID for the specific receipt. 
# Also stores original receipt data in receipts dict.
@app.route('/receipts/process', methods=['POST'])
def process_receipts():
    receipt = request.get_json()
    if receipt is None:
        return jsonify(error="There was an issue processing your receipt. Check to ensure that your receipt JSON matches the requirements."), 400
    receipt_id = str(uuid.uuid4())
    receipts[receipt_id] = receipt
    return jsonify(id=receipt_id), 201


# Route for getting points based on ID.
@app.route('/receipts/<string:id>/points', methods=['GET'] )
def get_points(id):
    receipt_by_id = receipts.get(id)
    if receipt_by_id is None:
        return jsonify(error="Sorry, a receipt with that ID could not be found."), 404
    points = calculate_total_receipt_points(receipt_by_id)
    return jsonify(points=points), 201


if __name__ == '__main__':
    app.run(port=8000)
