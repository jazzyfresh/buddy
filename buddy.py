from flask import Flask, render_template, request, url_for, flash, redirect

git_users = []

# receive http requests: "i need a code review buddy"
app = Flask(__name__)
app.config['SECRET_KEY'] = '1b13d3f28eff40d7e17eb567596414eb1f0f036c9ff03583'

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', group_assignments=group_assignments)

@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        username = request.form['username']
        if not username:
            flash('username is required')
        else:
            assign_group(username)
            # git_users.append(username)
            return redirect(url_for('index'))
    return render_template('create.html')

# mock data
git_users.append("jazzyfresh")
git_users.append("rtoal")
git_users.append("dondi")
git_users.append("julian")
git_users.append("nat")
git_users.append("tori")

# compute groups: "randomly assign code review buddies"
#   3 people in a group
#   keep a counter of how many in current group
#   keep a counter of how many groups
#   keep track of who is assigned to which group
GROUP_MAX_SIZE = 3
group_size = 0
total_groups = 0
group_assignments = {}

def assign_group(username):
    git_users.append(username)

    while git_users:
        # pop a user off the queue
        user = git_users.pop(0)

        # assign to the latest group
        group_assignments[user] = total_groups

        # increment counts
        group_size += 1
        # if a group is full, start a new group
        if group_size == GROUP_MAX_SIZE:
            group_size = 0
            total_groups += 1


# for key in data:
#     print("user %s in group %d" % (key, data[key]))

# persist groups: "save to sqlite in case a crash"

# send http response: "you are assigned code review buddies~!"
