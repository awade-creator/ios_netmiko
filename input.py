import yaml

# dict object
members = [{'name': 'Zoey', 'occupation': 'Doctor'},
           {'name': 'Zaara', 'occupation': 'Dentist'}]

# Convert Python dictionary into a YAML document
print(yaml.dump(members))