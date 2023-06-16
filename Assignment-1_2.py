import json

indian_states = {
    "Tamil Nadu": "Chennai",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai"
}
with open(r'C:\Users\NASREEN\OneDrive\Desktop\Json assignment\indian_states.json', 'w') as file:
    json.dump(indian_states, file)

