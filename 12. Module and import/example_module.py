data = {
  "name": "geniuis",
  "course": ["Data Science","Machine learning","Deep learning"],
  "Greetings": "Greetings from Genius"
}

def get_course():
    courses_offered = data["course"]
    return courses_offered
    

def greetings():
    return data["Greetings"]