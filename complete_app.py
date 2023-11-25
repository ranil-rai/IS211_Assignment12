
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key for production

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    # Dummy data - Replace with database queries
    students = [{'id': 1, 'first_name': 'John', 'last_name': 'Doe'}]
    quizzes = [{'id': 1, 'subject': 'Python Basics', 'question_count': 5, 'date_given': '2023-01-01'}]
    return render_template('dashboard.html', students=students, quizzes=quizzes)

@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        # Add logic to insert the student into the database
        flash('New student added.')
        return redirect(url_for('dashboard'))
    return render_template('add_student.html')

@app.route('/quiz/add', methods=['GET', 'POST'])
def add_quiz():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        # Add logic to insert the quiz into the database
        flash('New quiz added.')
        return redirect(url_for('dashboard'))
    return render_template('add_quiz.html')

@app.route('/student/<int:student_id>')
def view_results(student_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    # Dummy data - Replace with database queries
    results = [{'quiz_id': 1, 'subject': 'Python Basics', 'score': 85}]
    return render_template('view_results.html', student_id=student_id, results=results)

@app.route('/results/add', methods=['GET', 'POST'])
def add_result():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        # Add logic to insert the quiz result into the database
        flash('New quiz result added.')
        return redirect(url_for('dashboard'))
    # Dummy data - Replace with database queries
    students = [{'id': 1, 'first_name': 'John', 'last_name': 'Doe'}]
    quizzes = [{'id': 1, 'subject': 'Python Basics', 'question_count': 5, 'date_given': '2023-01-01'}]
    return render_template('add_result.html', students=students, quizzes=quizzes)

if __name__ == '__main__':
    app.run(debug=True)
