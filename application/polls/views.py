from application import app, db
from flask import redirect, render_template, request, url_for
from application.polls.models import Poll
from application.polls.forms import PollForm

@app.route("/polls", methods=["GET"])
def polls_index():
    return render_template("polls/list.html", polls = Poll.query.all())

@app.route("/polls/new/")
def polls_form():
    return render_template("polls/new.html", form = PollForm())

@app.route("/polls/<poll_id>/", methods=["POST"])
def polls_set_done(poll_id):

    p = Poll.query.get(poll_id)
    p.done = True
    db.session().commit()

    return redirect(url_for("polls_index"))

@app.route("/polls/", methods=["POST"])
def polls_create():

    p = Poll(request.form.get("name"), request.form.get("description"))

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("polls_index"))
