from sys import argv
script, username = argv
prompt=">"
print(f"Hi {username}, I'm the {script}.")
print(f"I'd like to ask you a few questions")
print(f"Do you like your {username}")
like =input(prompt)
print(f"where do you live {username}?",end=" ")
lives = input(prompt)
print("What kind of computer do you have?",end=" ")
computer = input(prompt)
print(f"""
said: {like}
lives: {lives}
computer: {computer}
""")
