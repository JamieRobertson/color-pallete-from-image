from flask import Flask, render_template, Markup
from PIL import Image, ImageEnhance
from bg_colors import get_content

app = Flask(__name__)
content = get_content()


@app.route("/")
def index(content=content):
    return render_template('index.html', content=content)

if __name__ == "__main__":
    app.run()
