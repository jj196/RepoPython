from flask import  Flask,jsonify, abort

app = Flask(__name__)

tasks = [
    {
    'id': 1,
        'title': u'Acceso Correcto',
        'description': u'Se reconocio la huella',
        'done': False
    },
    {
        'id': 0,
        'title': u' Acceso Incorrecto',
        'description': u'Huella incorrecta',
        'done': False
    }
]


@app.route('/prueba/tasks/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'tasks': task[0]})

@app.route('/')
def index():
        return 'hola mundo'


if __name__ == '__main__':
    app.run(debug=True, port=8080)