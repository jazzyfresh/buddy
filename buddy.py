
# receive http requests: "i need a code review buddy"

git_users = []
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


for key in group_assignments:
    print("user %s in group %d" % (key, group_assignments[key]))

# persist groups: "save to sqlite in case a crash"

# send http response: "you are assigned code review buddies~!"
