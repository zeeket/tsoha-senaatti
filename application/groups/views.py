from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.groups.models import Group
from application.groups.forms import GroupForm

@app.route("/groups", methods=["GET"])
@login_required
def groups_index():
    return render_template("groups/list.html",
           groups = Group.query.filter_by(created_by=current_user.id).all())

@app.route("/groups/new/")
@login_required
def groups_form():
    return render_template("groups/new.html", form = GroupForm())

@app.route("/groups/<group_id>/", methods=["POST"])
@login_required
def groups_remove(group_id):

    g = Group.query.get(group_id)
    if g.created_by==current_user.id:
        db.delete(g)
        db.session().commit()

    return redirect(url_for("polls_index"))

@app.route("/polls/", methods=["POST"])
@login_required
def groups_create():
    form = GroupForm(request.form)

    if not form.validate():
        return render_template("groups/new.html", form = form)

    g = Group(form.name.data)
    p.account_id = current_user.id
    #INSERT INTO group_accounts VALUES :group_id, :account_id

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("polls_index"))
