from flask import Flask, render_template
from csv import reader
from occupation_handling import csv_to_weighted_list, weighted_choice, read_file  # Custom import

app = Flask(__name__)

# Helper
def csv_to_list():
    with open('occupations.csv') as f:
      return list(reader(f))

@app.route('/occupations')
def occupations():
  rows = csv_to_list()[1:-1] # Strip out first and last lines
  occupations = read_file('occupations.csv')
  weighted_list = csv_to_weighted_list(occupations)
  job = weighted_choice(weighted_list)
  return render_template('occupation_template.html', rows=rows, job=job)

if __name__ == '__main__':
  app.debug = True
  app.run()

