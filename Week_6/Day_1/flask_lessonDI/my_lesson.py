from markdown import markdown
from flask import Flask, render_template_string, render_template

my_lesson = Flask(__name__)

@my_lesson.route('/')
def index():
    return '''
    
    <h1> Welcome to my learning site!</h1>
    <div>
        <ul>
            <li> <a href="http://127.0.0.1:5000/lesson" target="_blank">Lesson 1</a> </li>
            <li> <a href="http://127.0.0.1:5000/exercise" target="_blank">Exercise 1</a> </li>
    </div>
    '''

@my_lesson.route('/lesson')
def runlesson():
    readme_file = open("./static/in-this-chapter.md", "r")
    md_template_string = markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template_string

@my_lesson.route('/exercise')
def runexo():
    readme_file = open("./static/exercises.md", "r")
    md_template_string = markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template_string