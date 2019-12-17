from flask import Flask, render_template, request, redirect
from repository.branch_repository import BranchRepository
from repository.schedule_repository import ScheduleRepository
from repository.user_repository import UserRepository

from repository.branch_model import Branch
from repository.schedule_model import Schedule
from repository.user_repository import User
import config
import pymongo

try:
    mongo_client = pymongo.MongoClient("mongodb://root:root@127.0.0.1:27017/admin", serverSelectionTimeoutMS=2000)
except:
    raise Exception("failed connecting to database")

b = BranchRepository(mongo_client, config.DATABASE_NAME)
s = ScheduleRepository(mongo_client, config.DATABASE_NAME)
u = UserRepository(mongo_client, config.DATABASE_NAME) 


app = Flask(__name__)

@app.route("/branch")
def branch_index():
    data = b.find_all()
    print(data)
    return render_template('branches/index.html', data = data)

@app.route("/branch/add", methods=['GET', 'POST'])
def branch_add():
    if request.method == 'POST':
        name = request.form.get("name")
        address = request.form.get("address")
        instruments = request.form.getlist("instruments")
        req = Branch(name, address, instruments)
        print(name, address, instruments)
        b.create(req)
        return redirect("/")

    users = u.find_all()    
    return render_template('branches/add.html', users=users) 

@app.route("/schedule")
def schedule_index():
    return render_template('schedule/index.html')

@app.route("/schedule/add", methods=['GET', 'POST'])
def schedule_add():
    if request.method == 'POST':
        branch = request.form.get("branch")
        datetime = request.form.get("datetime")
        worship_leader = request.form.get("worship_leader")
        singers = request.form.getlist("singers")
        keyboard = request.form.get("keyboard")
        bass = request.form.get("bass")
        drum = request.form.get("drum")
        e_guitar = request.form.get("e_guitar")
        acc_guitar = request.form.get("acc_guitar")
        aux_keys = request.form.get("aux_keys")

        req = Schedule(branch, datetime, worship_leader, singers, keyboard, bass, drum, e_guitar, acc_guitar, aux_keys)
        print(req.__dict__)
        return redirect("/")

    branches = b.find_all()
    users = u.find_all()
    return render_template('schedule/add.html', branches=branches, users=users)

@app.route("/schedule/<id>/checkin")
def schedule_checkin(id):
    return render_template('schedule/check_in.html')
    
@app.route("/user")
def users_index():
    data = u.find_all()
    for i in data:
        i.branch = b.find_by_id(i.branch).name
    print(data)
    return render_template('users/index.html', data = data)

@app.route("/user/add", methods=['GET', 'POST'])
def user_add():
    if request.method == 'POST':
        name = request.form.get("name")
        branch = request.form.get("branch")
        telephone = request.form.get("telephone")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        req = User(name, username, branch, password, email, telephone)
        print(req.__dict__)
        u.create(req)
        return redirect("/")

    branches = b.find_all()
    return render_template('users/add.html', branches=branches) 

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)