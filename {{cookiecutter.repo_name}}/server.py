from flask import Flask


app = Flask(__name__)
app.debug = True
app.secret_key = 'Add secret key in a config file.'

@app.route('/')
def index():
    return 'Placeholder for template.'

if __name__ == '__main__':
    app.run()
