from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hanle_todos():
    response_body = jsonify(todos)
    return response_body

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position >= len(todos):
        response_body = {'message': 'Tarea fuera de rango'}
        return response_body
    del todos[position]
    return jsonify(todos)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)