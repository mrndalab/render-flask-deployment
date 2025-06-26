from flask import Flask, render_template_string
from nsedata import eq_opt_ltp

app = Flask(__name__)

my_variable=eq_opt_ltp("WIPR0", 230, '29-May-2025', 'PE')

html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Akshat's Flask App</title>
    </head>
    <body>
        <h1>Akshat's Flask App</h1>
        <!-- <p>{{ my_variable }}</p> -->
    </body>
    </html>
    """

@app.route("/", methods=['GET'])
def home():
    return render_template_string(html_content, my_variable=my_variable)

if __name__ == "__main__":
    app.run()
