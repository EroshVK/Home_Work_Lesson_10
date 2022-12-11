from flask import Flask
from functions import *

app = Flask(__name__)


@app.route("/")
def index():
    candidates = get_all()
    result = '<br>'
    for candidate in candidates:
        result += candidate['name']+'<br>'
        result += candidate['position']+'<br>'
        result += candidate['skills']+'<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    candidate = get_by_pk(pk)
    result = '<br>'
    result += candidate['name']+'<br>'
    result += candidate['position']+'<br>'
    result += candidate['skills']+'<br>'
    result += '<br>'
    url = candidate['picture']

    return f"""<img src='{url}'>
        <pre> {result} </pre>
        """


@app.route("/skills/<skill_name>")
def get_candidates_by_skills(skill_name):
    candidates = get_by_skill(skill_name)
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


if __name__ == '__main__':
    app.run(debug=True)
