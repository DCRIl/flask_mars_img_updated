import os

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def gallery():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join("static/img", file.filename))
    images = os.listdir("static/img")[::-1]
    print(images)
    return render_template('gallery.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)
