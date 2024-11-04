


test_dict = {'bollr38@hotmail.com':{
                    'name': 'Ryan',
                     'phone_number': '920-251-4841',
                     'email': 'bollr38@hotmail.com',
                     'notes': "Likes Ice Cream"
                     },
                    
            'ryanandkimboll@gmail.com':{
                    'name': 'Kim',
                    'phone_number': '920-379-4479',
                    'email': 'ryanandkimboll@gmail.com',
                    'notes': 'loves to cook'
            },
            'mateoboll@wstigers.com':{
                    'name':'Mateo',
                    'phone_number': '555-555-5555',
                    'email': 'mateoboll@wstigers.com',
                    'notes': 'this kid is super smart'
            }}




email = input("Please input email of the account you wish to access:\n")
new_email = input("What is the new email of this account?")

test_dict[new_email] = test_dict[email]
test_dict[new_email]['name'] = test_dict[email]['name']
test_dict[new_email]['phone_number'] = test_dict[email]['phone_number']
test_dict[new_email]['notes'] = test_dict[email]['notes']
test_dict[new_email]['email'] = new_email
test_dict.pop(email)

print(test_dict)

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line == '':
                    continue
                if not line.startswith(" "): #If the line does not start with a space it will assume it is the outer key.
                    current_key = line[:-1] #This will look for the entire line up until the ':' since the ':' should be the last part of the string 
                    contacts[current_key] = {} #This will initialize a key associated to an empty dictionary to start the inner key value pairs
                else:
                    if ':' in line: #Checks for the colon in the line to see if there is in fact a key value pair, if not it will skip
                        inner_key, value = line.split(": ", 1) #This will set a max split of 1 so there is only the key with one value.
                        contacts[current_key][inner_key] = (value)
                    else:
                        print("Skipping line.")