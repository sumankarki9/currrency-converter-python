from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')

# Existing conversion logic here...


def convert_usd_to_npr(usd):
    return 135.22 * usd

def convert_npr_to_usd(npr):
    return npr / 135.22

@app.route('/convert', methods=['GET'])
def convert():
    currency_type = request.args.get('type')  # Query parameter 'type'
    amount = request.args.get('amount')  # Query parameter 'amount'

    if not amount or not currency_type:
        return jsonify({"error": "Invalid input. Please provide both 'type' and 'amount'."}), 400

    try:
        amount = float(amount)
        if currency_type == 'usd_to_npr':
            result = convert_usd_to_npr(amount)
            return jsonify({"USD": amount, "NPR": round(result, 2)})

        elif currency_type == 'npr_to_usd':
            result = convert_npr_to_usd(amount)
            return jsonify({"NPR": amount, "USD": round(result, 2)})

        else:
            return jsonify({"error": "Invalid conversion type. Use 'usd_to_npr' or 'npr_to_usd'."}), 400
    except ValueError:
        return jsonify({"error": "Invalid amount. Please provide a numeric value."}), 400

if __name__ == '__main__':
    app.run(debug=True)
