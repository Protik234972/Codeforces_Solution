string="amaama"
half = int(len(string)/2)

if len(string)%2==0:
    first_str = string[:half]
    second_str = string[half:]
else:
    first_str =string[:half]
    second_str =string[half+1:]

if first_str == second_str:
    print("symmetrical")
else:
    print("not symmetrical")