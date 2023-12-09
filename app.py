from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)
tasks = [
    {"id": 1, "title": "Task 1", "description": "This is task 1", "done": False},
    {"id": 2, "title": "Task 2", "description": "This is task 2", "done": False},
]


# GET - Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


# GET - Retrieve a specific task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'task': task[0]})


# POST - Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201


# PUT - Update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Task not found'}), 404
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get(
        'description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


# PATCH - Partially update an existing task
@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def partial_update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Task not found'}), 404
    if 'title' in request.json:
        task[0]['title'] = request.json['title']
    if 'description' in request.json:
        task[0]['description'] = request.json['description']
    if 'done' in request.json:
        task[0]['done'] = request.json['done']
    return jsonify({'task': task[0]})


# DELETE - Delete an existing task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Task not found'}), 404
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
