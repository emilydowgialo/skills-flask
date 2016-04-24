from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Show a job application form"""

    return render_template("application-form.html")


@app.route("/application-response", methods=['POST'])
def application_response():
    """Show a response based on application form inputs"""

    if request.method == 'POST':
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        salary = request.form.get('salary')
        job_title = request.form.get('job-title')

        return render_template("application-response.html", 
                                firstname=first_name, 
                                lastname=last_name, 
                                salary=salary, 
                                jobtitle=job_title)


if __name__ == "__main__":
    app.run(debug=True)
