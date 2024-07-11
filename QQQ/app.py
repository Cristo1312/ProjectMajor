from flask import Flask, request, render_template, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessario per usare i messaggi di flash

teams = []
matches = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit_teams', methods=['GET', 'POST'])
def submit_teams():
    global teams, matches
    if request.method == 'POST':
        teams = request.form.getlist('teams')
        if len(teams) != 10:
            flash("Error: Please enter exactly 10 team names.")
            return redirect(url_for('submit_teams'))
        generate_schedule()
        return redirect(url_for('schedule'))
    return render_template('subteam.html')

def generate_schedule():
    global matches
    matches = []
    for round_num in range(1, 37):
        round_matches = []
        teams_copy = teams[:]
        random.shuffle(teams_copy)
        for i in range(0, len(teams_copy), 2):
            round_matches.append((teams_copy[i], teams_copy[i+1]))
        matches.append(round_matches)

@app.route('/schedule')
def schedule():
    return render_template('schedule.html', matches=enumerate(matches, 1))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)
