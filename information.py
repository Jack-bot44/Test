name = input("What is your name ? Please answer here:")
age = input("And also how old are you ? Answer here again -_-:")
if int(age) < 5:
    print("How do you even know how to write ?! You shouldn't be here ! Go back to your drawings, foolish being ! ")
elif int(age) < 17:
    print("Hmm ... A teenager ... I see ... I'm not used to seeing youngsters, but I guess it's a good thing ...")
    Designation = input("What should I call you, Miss or Mister ? ")
    while Designation.lower() != "mister" and Designation.lower() != "miss":
        print("Stop fooling around, just write Miss or Mister. I'm not stupid you know.")
        Designation = input("What should I call you, Miss or Mister ? ")
    print(f"well, welcome, {Designation} {name} ! Pleased to meet you ! ")
else:
    print("Ok, you're actually not that young ... hehe")