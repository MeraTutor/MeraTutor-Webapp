from flask import Flask, render_template,url_for
import os

app = Flask(__name__)

print("Current working directory:", os.getcwd())
print("Contents of templates folder:", os.listdir('templates'))
#set static folder

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/landing')
def landing():
    return render_template('landing_page.html')

@app.route('/library')
def library():
    return render_template('library-assets.html')

@app.route('/all-students')
def all_students():
    # In a real application, you would fetch this data from a database
    students = [
        {'name': 'John Doe', 'department': 'Computer Science', 'age': 20},
        {'name': 'Jane Smith', 'department': 'Physics', 'age': 22},
        {'name': 'Mike Johnson', 'department': 'Mathematics', 'age': 21},
    ]
    return render_template('all_students.html', students=students)

@app.route('/add-student')
def add_student():
    return render_template('add_student.html')

@app.route('/launch-ai')
def launch_ai():
    return render_template('accordion.html')

@app.route('/all-professors')
def all_professors():
    # In a real application, you would fetch this data from a database
    professors = [
        {'name': 'Dr. Alice Brown', 'department': 'Computer Science'},
        {'name': 'Prof. Bob Wilson', 'department': 'Physics'},
        {'name': 'Dr. Carol Davis', 'department': 'Mathematics'},
    ]
    return render_template('all-professors.html', professors=professors)

if __name__ == '__main__':
    app.run(debug=True)