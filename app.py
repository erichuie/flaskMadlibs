from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

# from stories import silly_story
from stories import stories_list

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

chosen_story = None

@app.get('/')
def madlib_dropdown():
    return render_template("dropdown.html", story_list=stories_list)


@app.get('/story')
def madlib_form():

    """Renders form for madlib story prompts"""

    global chosen_story
    form_story_type = request.args.get("story_select")
    for story in stories_list:
        if story.type == form_story_type:
            chosen_story = story
            print(chosen_story)
            print("test")#no spaces is convention for passing vars to templates
            return render_template("questions.html", prompts=chosen_story.prompts)

@app.get('/results/<chosen_story>')
def display_results():
    """Renders resulting story from user prompts"""
    #need form answers
    #answers_dict = {}
 #FIXME: basically this was all extra because we can just pass the args
 # to get_result_text
    # for prompt in silly_story.prompts:
    #     answer = request.args.get(prompt)
    #     answers_dict[prompt] = answer
    print(chosen_story)
    results_text = chosen_story.get_result_text(request.args)

    return render_template('results.html', results_text=results_text)
