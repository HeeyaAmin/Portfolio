from flask import Flask, render_template

app = Flask(__name__)

# Assuming your HTML, CSS, and JavaScript files are in a subdirectory named 'static'
app.config['STATIC_FOLDER'] = 'static'


@app.route('/')
def portfolio():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
