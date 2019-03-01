from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.polls.models import Poll
from application.polls.forms import PollForm

@app.route("/polls", methods=["GET"])
def polls_index():
    return render_template("polls/list.html", polls = Poll.query.all())

@app.route("/polls/new/")
@login_required
def polls_form():
    return render_template("polls/new.html", form = PollForm())

@app.route("/polls/<poll_id>/setdone", methods=["POST"])
@login_required
def polls_set_done(poll_id):

    p = Poll.query.get(poll_id)
    p.done = True
    db.session().commit()

    return redirect(url_for("polls_index"))

@app.route("/polls/<poll_id>", methods=["GET"])
@login_required
def poll_show_single(poll_id):

    p = Poll.query.get(poll_id)

    return render_template("polls/singleview.html", poll = p)

@app.route("/polls/<poll_id>/voteup", methods=["POST"])
@login_required
def polls_vote_up(poll_id):

    p = Poll.query.get(poll_id)
    p.upvotes+=1
    db.session().commit()

    return request.referrer



@app.route("/polls/", methods=["POST"])
@login_required
def polls_create():
    form = PollForm(request.form)

    if not form.validate():
        return render_template("polls/new.html", form = form)

    p = Poll(form.name.data,form.description.data)
    p.account_id = current_user.id

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("polls_index"))
