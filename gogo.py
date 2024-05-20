def find_name(first_name, last_name, file_path):
  with open(file_path, 'r') as file:
      text = file.read().lower()
      full_name = f"{first_name.lower()} {last_name.lower()}"
      if full_name in text:
          print(f"Found: {first_name} {last_name}")
      else:
          print(f"Name '{first_name} {last_name}' not found in the text.")

i = open("IntervieweeNames.txt", "r").readlines()
interviewees = list(map(str.strip, i))

for x in interviewees:
  find_name(x.split()[0], x.split()[1], "PulseArticle.txt")
