from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def madlib_form():
    """Renders form for madlib story prompts"""
    print("test")
    return render_template("questions.html", prompts = silly_story.prompts)

@app.get('/results')
def display_results():
    """Renders resulting story from user prompts"""
    #need form answers
    answers_dict = {}

    for prompt in silly_story.prompts:
        answer = request.args.get(prompt)
        answers_dict[prompt] = answer

    results_text = silly_story.get_result_text(answers_dict)

    return render_template('results.html', results_text=results_text)
