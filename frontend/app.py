from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def list_todos():
    todos = []  # Retrieve the list of to-do items from the backend API
    return render_template('list_todos.html', todos=todos)

@app.route('/create')
def create_todo():
    return render_template('create_todo.html')

if __name__ == '__main__':
    app.run(debug=True)
