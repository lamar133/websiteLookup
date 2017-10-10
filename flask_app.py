from flask import Flask, request, render_template
from string import Template
import main

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