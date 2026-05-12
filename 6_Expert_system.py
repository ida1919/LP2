disease_db = {
    "Common Cold": {
        "must": ["runny nose", "sneezing"],
        "extra": ["mild fever", "sore throat", "cough", "tiredness"]
    },
    "Flu": {
        "must": ["high fever", "body pain","eye pain "],
        "extra": ["fatigue", "cough", "sore throat", "headache", "chills"]
    },
    "COVID-19": {
        "must": ["fever"],
        "extra": ["dry cough", "fatigue", "loss of taste", "loss of smell",
                  "breathing problem", "headache"]
    },
    "Malaria": {
        "must": ["vomitting", "chills"],
        "extra": ["sweating", "headache", "vomiting", "body pain"]
    }

}

def find_disease(symptoms):

    for disease, data in disease_db.items():

        # combine all symptoms
        all_symptoms = data["must"] + data["extra"]

        for s in symptoms:

            s = s.strip().lower()

            if s in all_symptoms:
                return disease

    return "No disease found"


print("Symptoms: cough, sneezing, fever, body pain, high fever, chills")

user = input("Enter symptoms separated by comma: ")

user_symptoms = user.split(",")

result = find_disease(user_symptoms)

print("Possible disease:", result)
