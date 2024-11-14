# comment again
import azure.functions as func
import json
import logging

app = func.FunctionApp()

@app.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    number = req.params.get('number')
    if not number:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = None
        if req_body:
            number = req_body.get('number')

    if number:
        # Pass the number directly to analyze_number without converting it
        response = analyze_number(number)
        return func.HttpResponse(
            json.dumps(response),
            status_code=200,
            mimetype="application/json"
        )
    else:
        # Return error message in JSON format
        response = { "error": "please pass a number in the query string or in the request body" }
        return func.HttpResponse(
             json.dumps(response),
             status_code=200,
             mimetype="application/json"
        )

def analyze_number(num):
    # TODO 1: Code Logic to handle number validation
    try:
        num = int(num)
    except (ValueError, TypeError):
        return { "error": "please enter a valid number" }

    if num <= 0:
        return { "error": "please enter a number greater than 0" }

    # TODO 2: Code Logic to find the sum of digits
    sum_of_digits = sum(int(digit) for digit in str(num))

    # TODO 3: Code Logic to check whether number is prime
    if num <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

    # TODO 4: Code Logic to check whether number is odd
    is_odd = num % 2 != 0

    # TODO 5: Code Logic to check whether number is perfect
    if num <= 1:
        is_perfect = False
    else:
        divisors_sum = 1
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                divisors_sum += i
        is_perfect = divisors_sum == num

    # TODO 6: Code Logic to check whether number is triangular
    is_triangular = False
    if num > 0:
        n = (-1 + (1 + 8 * num) ** 0.5) / 2
        is_triangular = n.is_integer()

    # TODO 7: Replace default values below with the results of the calculations from TODOs 2-6.
    response = {
        "sum_of_digits": sum_of_digits,
        "is_prime": is_prime,
        "is_odd": is_odd,
        "is_perfect": is_perfect,
        "is_triangular": is_triangular
    }

    return response
