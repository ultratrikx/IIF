from flask import Flask, request, render_template, redirect, url_for
from classifier.classify import classify_description
import csv
import os

app = Flask(__name__, static_url_path='/static')
CSV_FILE_PATH = 'data.csv'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        idea_description = request.form['description']
        classification = classify_description(idea_description)

        # Save the idea and its classification to the CSV file
        with open(CSV_FILE_PATH, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([f'{idea_description}', classification])

        return render_template('index.html', description=idea_description, classification=classification, show_update=True)
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    idea_description = request.form['description']
    new_classification = request.form['new_classification']

    # Read the current data
    data = []
    if os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

    # Update the classification for the specific idea
    for row in data:
        if row[0] == idea_description:
            row[1] = new_classification
            break

    # Write the updated data back to the CSV file
    with open(CSV_FILE_PATH, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

    return redirect(url_for('index'))

if __name__ == '__main__':
    # app.run(debug=True, port=42069, host="0.0.0.0") use this line if you want to run the app on a server
    app.run(debug=True, port=42069)
