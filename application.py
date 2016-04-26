from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""


    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
    return render_template("index.html")

@app.route("/application-form")
def application_form():
    """Collect user information"""
    
    return render_template("application-form.html")

@app.route("/application-response")
def application_respone():
    """Returns user application information"""
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    salary = request.args.get("salary")
    job_title = request.args.get("job_title")

    return render_template("application-response.html", first_name=first_name, last_name=last_name, salary=salary,job_title=job_title)



if __name__ == "__main__":
    app.run(debug=True)
