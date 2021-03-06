import logging
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

@app.route("/polls/<poll_id>/", methods=["POST", "GET"])
def polls_show_single(poll_id):
    p = Poll.query.get(poll_id)
    return render_template("polls/singleview.html", get_creator_name = p.get_creator_name,userswhovoted=p.find_users_who_voted(),poll=p)

@app.route("/polls/<poll_id>/up", methods=["POST"])
@login_required
def polls_set_upvote(poll_id):

    p = Poll.query.get(poll_id)
    if not p.account_id == current_user.id and not p.has_voted(current_user.id):
        p.upvotes+=1
        p.votes.append(current_user)
        db.session().commit()

    return redirect(url_for("polls_show_single", poll_id=p.id))

@app.route("/polls/<poll_id>/neutral", methods=["POST"])
@login_required
def polls_set_neutralvote(poll_id):

    p = Poll.query.get(poll_id)
    app.logger.info('account id %(current_user.id)s voted neutral on poll id %(p.id)s')
    hasvotedalready = p.has_voted(current_user.id)
    app.logger.info('p.hasvoted(%(current_user.id)s) returned %(hasvotedalready)s')
    app.logger.info('p.account_id = %(p.account_id)s and it should not be %(current_user.id)s')
    if not p.account_id == current_user.id and not hasvotedalready:
        p.neutralvotes+=1
        p.votes.append(current_user)
        db.session().commit()

    return redirect(url_for("polls_show_single", poll_id=p.id))

@app.route("/polls/<poll_id>/down", methods=["POST"])
@login_required
def polls_set_downvote(poll_id):

    p = Poll.query.get(poll_id)
    if not p.account_id == current_user.id and not p.has_voted(current_user.id):
        p.downvotes+=1
        p.votes.append(current_user.id)
        db.session().commit()

    return redirect(url_for("polls_show_single",poll_id=p.id))

@app.route("/polls/<poll_id>/delete", methods=["POST"])
@login_required
def polls_delete(poll_id):

    p = Poll.query.get(poll_id)
    if p.account_id != current_user.id:
        return login_manager.unauthorized

    db.session.delete(p)
    db.session.commit()

    return redirect(url_for("polls_index"))
