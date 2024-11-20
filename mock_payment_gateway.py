from flask import Flask, request, jsonify
import uuid
import random

app = Flask(__name__)


# Endpoint to mimic payment processing
@app.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.json

    if not data.get('amount') or not data.get('method_id') or not data.get('order_id'):
        return jsonify({"status": "failed", "message": "Missing payment details"}), 400

    # Simulate transaction processing
    transaction_id = str(uuid.uuid4())
    payment_status = random.choice(['approved', 'declined'])

    response = {
        "transaction_id": transaction_id,
        "payment_status": payment_status
    }

    if payment_status == 'approved':
        return jsonify({"status": "success", "data": response}), 200
    else:
        return jsonify({"status": "failed", "data": response}), 400


if __name__ == '__main__':
    app.run(port=5001, debug=True)
