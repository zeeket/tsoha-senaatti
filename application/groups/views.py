from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.groups.models import Group
from application.groups.forms import GroupForm

def get_users_choices():
    #loads all possible userids and usernames from db
    users_choices_all = [(str(u.id), u.username) for u in User.query.all()]
    return users_choices_all

@app.route("/groups", methods=["GET"])
@login_required
def groups_index():
    return render_template("groups/list.html",
           groups = Group.query.filter_by(created_by=current_user.id).all())

@app.route("/groups/new/", methods=["GET"])
@login_required
def groups_form():
    myform = GroupForm()
    myform.group_users_select.choices = get_users_choices()
    return render_template("groups/new.html", form = myform)

@app.route("/groups/<group_id>/", methods=["POST"])
@login_required
def groups_remove(group_id):

    g = Group.query.get(group_id)
    if g.created_by==current_user.id:
        db.delete(g)
        db.session().commit()

    return redirect(url_for("polls_index"))

@app.route("/groups/new/", methods=["POST"])
@login_required
def groups_create():
    form = GroupForm(request.form)

    if not form.validate():
        return render_template("groups/new.html", form = form)
    
    allusers = get_users_choices()
    memberlist = []
    
    for v in form.group_users_select.data:
                try:
                    user_id = int(v)
                    memberlist.append(v)
                except ValueError:
                    pass
    
    g = Group(memberlist)
    g.name = form.name.data
    g.created_by = current_user.id
    #INSERT INTO group_accounts VALUES :group_id, :account_id

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("polls_index"))
