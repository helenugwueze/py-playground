alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("Thealien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")


person = {'f_name': 'grace', 'l_name': 'john', 'age': 20, 'city': 'delta'}
print(person['f_name'])
print(person['l_name'])
print(person['age'])
print(person['city'])

favorite_number = {'mary': 60, 'jay': 34, 'john': 49, 'sam': 56, 'may': 89,}
print(favorite_number['mary'])
print(favorite_number['jay'])
print(favorite_number['john'])
print(favorite_number['sam'])
print(favorite_number['may'])
print(favorite_number)



favorite_friend = {"Amara": 7, "Tunde": 11, "Chioma": 3}

print(favorite_friend)

glossary = {
    'God': 'ominipotent',
    'dictionary': 'key pair value',
    'variable': 'it a container used to store value',
    'list': 'are covered by square bracket',
}
print("God",glossary['God'])
print("dictionary",glossary['dictionary'])
print("variable", glossary['variable'])
print("list",glossary['list'])
