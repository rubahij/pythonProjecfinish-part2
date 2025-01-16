from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)  # תיקון כאן: שימוש נכון ב __name__
app.secret_key = 'supersecretkey'  # נדרש עבור שימוש ב-session

# דף הבית
@app.route('/')
def home():
    return render_template('HOME.html')

# כניסה למערכת
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # בדוק את פרטי המשתמש (לדוגמה: מול בסיס נתונים)
        if email == 'test@example.com' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('personal_page'))
        else:
            return render_template('login.html', error='פרטי התחברות שגויים')
    return render_template('login.html')

# יצירת קשר
@app.route('/callus')
def callus():
    return render_template('CALLUS.html')

# צוות הרופאים
@app.route('/ourdoctors')
def our_doctors():
    return render_template('ourDOCTORS.html')

# יצירת חשבון
@app.route('/createaccount', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # כאן ניתן להוסיף לוגיקה לשמירת חשבון
        return redirect(url_for('login'))
    return render_template('CreateAccount.html')

# אזור אישי
@app.route('/personalpage')
def personal_page():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('PersonalPage.html')

# קביעת תור
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        doctor_name = request.form.get('doctorName')
        treatment_type = request.form.get('treatmentType')
        appointment_date = request.form.get('appointmentDate')
        appointment_time = request.form.get('appointmentTime')

        # בדיקה אם כל השדות מלאים
        if not (doctor_name and treatment_type and appointment_date and appointment_time):
            error = "יש למלא את כל השדות כדי לקבוע תור"
            return render_template('BOOKING.html', error=error)

        # טיפול בנתונים - למשל שמירה למסד נתונים
        return f"תור נקבע בהצלחה: {doctor_name}, {treatment_type}, {appointment_date}, {appointment_time}"

    return render_template('BOOKING.html')

# היסטוריית טיפולים
@app.route('/mybooking')
def my_booking():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('MYBOOKING.html')

if __name__ == '__main__':
    app.run(debug=True)
