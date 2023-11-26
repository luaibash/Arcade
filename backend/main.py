from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    try:
        subprocess.run(['python -m navigation.csv -f 1 -l 1'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    return render_template('App.js')
               
@app.route('/templerun')
def templerun():
    try:
        subprocess.run(['python -m templerun.csv -f 1 -l 1'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    return render_template('templerun.js')

@app.route('/mario')
def mario():
    try:
        subprocess.run(['python -m mario.csv -f 1 -l 1'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    return render_template('mario.js')

@app.route('/flappybird')
def flappybird():
    try:
        subprocess.run(['python -m flappybird.csv -f 1 -l 1'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    return render_template('mario.js')

@app.route('/2048')
def game2048():
    try:
        subprocess.run(['python -m 2048.csv -f 1 -l 1'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    return render_template('mario.js')

@app.route('/pacman')
def pacman():
    try:
        subprocess.run(['python -m pacman.csv -f 1 -l 1'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    return render_template('mario.js')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, threaded=True, use_reloader=False)