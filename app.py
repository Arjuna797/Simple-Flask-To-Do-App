from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory task storage
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    data = request.get_json()
    task_name = data.get('task')
    if task_name:
        tasks.append({'task': task_name, 'done': False})
    return jsonify(tasks)

@app.route('/complete', methods=['POST'])
def complete_task():
    data = request.get_json()
    task_name = data.get('task')
    for task in tasks:
        if task['task'] == task_name:
            task['done'] = True
            break
    return jsonify(tasks)

@app.route('/delete', methods=['POST'])
def delete_task():
    data = request.get_json()
    task_name = data.get('task')
    global tasks
    tasks = [task for task in tasks if task['task'] != task_name]
    return jsonify(tasks)

if __name__ == '__main__':
    print("🚀 Flask To-Do App running on http://localhost:9090")
    app.run(host='0.0.0.0', port=9090, debug=True)
