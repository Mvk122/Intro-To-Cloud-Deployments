import flask
import string
import random

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    ai_generated_password = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(20)])
    return flask.render_template('index.html', password=ai_generated_password)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')