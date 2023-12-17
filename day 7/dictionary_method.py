person={
    'name': 'samarpan',
    'age':12
}
print(person.keys())
print(person.values())
print(person.items())

print(person.get('address'))# useful in cases where the keys are dynamically made

new_data={
    'name':'shyam'
}

person.update(new_data)
print(person)