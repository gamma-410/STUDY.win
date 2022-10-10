from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# データベースの作成 / 設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///postData.db'
app.config['SECRET_KEY'] = '5730292743938474948439320285857603'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# SQLite の設定
class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  userName = db.Column(db.Text, nullable=False)
  taskTitle = db.Column(db.String(20), nullable=False)
  taskDetail = db.Column(db.Text, nullable=False)


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  userName = db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String(25), nullable=False)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))



@app.route('/')
def index():
  return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == "GET":
    return render_template('login.html')

  else:
    try:
      userName = request.form.get('userName')
      password = request.form.get('password')

      # UserテーブルからuserNameに一致するユーザを取得
      user = User.query.filter_by(userName=userName).first()
      if check_password_hash(user.password, password):
        login_user(user)
        flash("ログインしました！")
        return redirect(f'/event')

      else:
        flash("ログインに失敗しました...")
        return redirect('/login')

    except:
      flash("ログインに失敗しました...")
      return redirect('/login')

@app.route('/setup', methods=['GET', 'POST'])
def setup():
  if request.method == "GET":
    return render_template('setup.html')

  else:
    try:
      userName = request.form.get('userName')
      password = request.form.get('password')

      if userName:
        print("ok")
      else:
        flash("入力漏れがあります...")
        return redirect("/setup")

      if password:
        print("ok")
      else:
        flash("入力漏れがあります...")
        return redirect("/setup")

      new_user = User(userName=userName, password=generate_password_hash(password, method='sha256'))  # パスワードをハッシュ値に変換
      db.session.add(new_user)  
      db.session.commit() 

      flash("アカウントの作成が完了しました。ログインしましょう！")
      return redirect('/login')

    except:
      flash("アカウントの作成に失敗しました...")
      return redirect('/setup')


@app.route('/logout')
@login_required 
def logout():
  logout_user()
  return redirect('/')
  

@app.route('/event', methods=['GET', 'POST'])
@login_required
def event():
  if request.method == 'GET':
    task = Task.query.filter_by(userName=current_user.userName).order_by(Task.id.desc()).all()
    return render_template('event.html', task=task)
  
  else:
    userName = current_user.userName
    taskTitle = request.form.get('taskTitle') 
    taskDetail = request.form.get('taskDetail')
    new_task = Task(userName=userName, taskTitle=taskTitle, taskDetail=taskDetail)
    db.session.add(new_task)
    db.session.commit()

    flash("イベントを追加しました！")
    return redirect('/event')


@app.route('/done/<int:id>')
def doneEvent(id):
  task = Task.query.get(id)
  db.session.delete(task)
  db.session.commit()
  flash("イベント完了ですね！お疲れ様でした✨")
  return redirect('/event')

@app.route('/delete/<int:id>')
def deleteEvent(id):
  task = Task.query.get(id)
  db.session.delete(task)
  db.session.commit()
  flash("イベントを削除しました！")
  return redirect('/event')

@app.route('/timer')
def timer():
  return render_template('timer.html')

if __name__ == "__main__":
  app.run(debug=True)
