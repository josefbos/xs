from flask import Flask, render_template, request
import config
import blog


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        if 'form1' in request.form:
            prompt = request.form['question']
            blogT = blog.answer(prompt)
            answers = blogT

    return render_template('index.html', **locals())




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
