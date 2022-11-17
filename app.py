from flask import Flask, request, render_template
from main import get_scale


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scale', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return get_scale(processed_text)




if __name__ == '__main__':
    #app.debug = True
    app.run()
