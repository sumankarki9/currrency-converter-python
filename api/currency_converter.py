import json

def handler(request):
    params = request.args
    currency_type = params.get('type')
    amount = float(params.get('amount'))
    
    if currency_type == "usd_to_npr":
        result = amount * 135.22
        response = {"USD": amount, "NPR": result}
    elif currency_type == "npr_to_usd":
        result = amount / 135.22
        response = {"NPR": amount, "USD": result}
    else:
        response = {"error": "Invalid conversion type"}
    
    return {
        "statusCode": 200,
        "body": json.dumps(response),
        "headers": {"Content-Type": "application/json"}
    }
