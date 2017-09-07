students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_full_name(class_room):
    for thing in class_room:
        print "{} {}".format(thing['first_name'], thing['last_name'])

print_full_name(students)
# now Part II
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def print_everything(members):
    for member_type, member in members.items():
        print member_type
        id_num = 1
        for person in member:
            name = person["first_name"]
            last_name = person["last_name"]
            char_length = len(name) + len(last_name)
            print "{} - {} {} - {}".format(id_num, name, last_name, char_length)
            id_num += 1

print_everything(users)
