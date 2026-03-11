from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def dashboard():
    conn = get_db_connection()
    expenses = conn.execute('SELECT * FROM expenses').fetchall()

    labels = []
    amounts = []

    for expense in expenses:
        labels.append(expense['category'])
        amounts.append(expense['amount'])

    conn.close()

    return render_template(
        'dashboard.html',
        expenses=expenses,
        labels=labels,
        amounts=amounts
    )
    
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/add', methods=('GET','POST'))
def add_expense():
    if request.method == 'POST':
        category = request.form['category']
        amount = request.form['amount']
        description = request.form['description']

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)',
            (category, amount, description)
        )
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('add_expense.html')

if __name__ == "__main__":
    app.run(debug=True)