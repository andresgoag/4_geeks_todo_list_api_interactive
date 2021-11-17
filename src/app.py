import json
from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
  { "label": "My first task", "done": False },
  { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
  return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
  decoded_object = json.loads(request.data)
  todos.append(decoded_object)
  return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  if position >= 0 and position < len(todos):
    todos.pop(position)
  return jsonify(todos)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)