from web import app, db
from web.forms import TaskForm #UserForm
from web.models import Task #User
from flask import render_template, redirect, url_for, request
#from flask_login import login_user, LoginManager, login_manager,logout_user, login_required
#from werkzeug.security import generate_password_hash, check_password_hash
import module
"""
login_manager = LoginManager()
login_manager.init_app(app)

#セッション状況を保存してくれる
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
"""
@app.route('/')
#@login_required
def index():

    #genreとdateをDBから呼び出す
    call = db.session.query(Task).all()
    events = module.event(call)
    tasks = Task.query.order_by(Task.date.asc()).paginate(page=1, per_page=app.config['ITEMS_PER_PAGE'], error_out=False)
    return render_template('index.html', tasks=tasks, events=events)


@app.route('/pages/<int:page_num>', methods=["GET", "POST"])
#@login_required
def index_pages(page_num):

    call = db.session.query(Task).all()
    events = module.event(call)
    tasks = Task.query.order_by(Task.date.asc()).paginate(page=page_num, per_page=app.config['ITEMS_PER_PAGE'], error_out=False)
    return render_template('index.html', tasks=tasks, events=events)


@app.route('/register', methods=["GET", "POST"])
#@login_required
def register_task():

    form = TaskForm()

    if form.validate_on_submit():
        task = Task(genre=form.genre.data, title=form.title.data, body=form.body.data, date=form.date.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register_task.html', form=form)


@app.route('/<int:id>/update', methods=["GET", "POST"])
#@login_required
def update_task(id):

    task = Task.query.get(id)
    form = TaskForm()
    
    if form.validate_on_submit():
        task.genre = form.genre.data
        task.title = form.title.data
        task.body = form.body.data
        task.date = form.date.data
        db.session.commit()

        return redirect(url_for('index'))
    
    elif request.method == "GET":
        form.genre.data = task.genre
        form.title.data = task.title
        form.body.data = task.body
        form.date.data = task.date
    
    return render_template('edit_task.html', form=form, id=id)


@app.route('/<int:id>/delete', methods=["GET", "POST"])
#@login_required
def delete_task(id):

    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/schedule')
#@login_required
def schedule_task():

    call = db.session.query(Task).filter(Task.genre == "Schedule")
    schedules = module.event(call)
    return render_template('schedule_task.html', schedules=schedules)

@app.route('/todo')
#@login_required
def todo_task():

    call = db.session.query(Task).filter(Task.genre == "Todo")
    todos = module.event(call)
    return render_template('todo_task.html', todos=todos)


"""
@app.route('/signup', methods=["GET", "POST"])
def signup():

    form = UserForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, password=generate_password_hash(form.password.data, method='sha256'))
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():

    form = UserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect('/')
        else:
            return "<html><body><h1>ログインに失敗しました</h1></body></html>"
    else:
        return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')
"""