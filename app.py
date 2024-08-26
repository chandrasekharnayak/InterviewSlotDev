from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Data to simulate bookings
bookings = []

# Mentors and their available times
mentors = {
    'PAT': ['Chandra sir', 'Tushar sir', 'Amir sir'],
    'JAT': ['Chandra sir'],
    'PD': ['Chandra sir']
}

# Mentor-specific time slots
mentor_time_slots = {
    'Chandra sir': ['12pm-1pm', '1pm-2pm', '2pm-3pm', '3pm-4pm', '4pm-5pm', '5pm-6pm', '6pm-7pm'],
    'Tushar sir': ['11am-12pm', '12pm-1pm', '1pm-2pm'],
    'Amir sir': ['3pm-4pm', '4pm-5pm', '5pm-6pm']
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        technology = request.form['technology']
        company_name = request.form['company_name']
        round = request.form['round']
        mentor = request.form['mentor']
        date = request.form['date']
        time = request.form['time']

        # Check if the slot is already booked
        for booking in bookings:
            if booking['date'] == date and booking['time'] == time and booking['mentor'] == mentor:
                return "This slot is already booked! Please choose another slot."

        # Add booking to the list
        bookings.append({
            'name': name,
            'technology': technology,
            'company_name': company_name,
            'round': round,
            'mentor': mentor,
            'date': date,
            'time': time
        })

        return redirect(url_for('dashboard'))

    return render_template('index.html', mentors=mentors)

@app.route('/dashboard')
def dashboard():
    # Group bookings by week for the dashboard
    return render_template('dashboard.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)
