# Maintain a list to store executing functions and their status
executing_functions = []

def is_function_executing(function_id):
    for function in executing_functions:
        if function['function_id'] == function_id:
            return True
    return False

@app.route('/function', methods=['POST'])
def handle_function_request():
    function_id = request.json['function_id']
    if is_function_executing(function_id):
        # It's a warm start
        # Place the request in a wait queue
        # ...
    else:
        # It's a cold start
        # Create a container, fetch code from registry, and execute the function
        # ...
