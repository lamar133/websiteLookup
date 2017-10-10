from flask import Flask, request, render_template, url_for
from string import Template
import main

PROFILE_CONTAINER = Template("""
<div id="divider"></div>
<div id="container">
    <div id="current_show"><b>{{current_show}}</b></div>
    <button class='nav_bttn' id='prev_bttn'>Previous</button>
    <button class='nav_bttn' id='next_bttn'>Next</button>
    <div id="pic_counter"><b>{{num_actors}} Actors in this List</b></div>
    <div id="actor_pic">
        {% for actor in actor_dict %}
        <img src={{ actor.Pics }}>
        {% endfor %}
    </div>
    <div id="actor_name">
        {% for actor in actor_dict %}
        <p>{{ actor.Actors }}</p>
        {% endfor %}
    </div>
    <button id="reveal_bttn">Show Name</button>
</div>
    """)

app = Flask(__name__)

@app.route('/')
@app.route('/search.html')
def search():
    return render_template('search.html')

@app.route('/result.html', methods=['POST'])
def result():
    website = request.form['website']
    requiredInfo = main.runSearch(website)
    return render_template('result.html', site=website, title=requiredInfo['Title'], description=requiredInfo['Description'], socials=requiredInfo['Socials'], address=requiredInfo['Address'], city=requiredInfo['City'], state=requiredInfo['State'], country=requiredInfo['Country'], phone=requiredInfo['Phone'], email=requiredInfo['Email'], alexa_score=requiredInfo['Alexa Score'], keywords=requiredInfo['Keywords'], timezone_id=requiredInfo['Timezone ID'], timezone_name=requiredInfo['Timezone Name'])
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)