import webbrowser
def view():
    
    url = link
    for i in range(int(number)):
        webbrowser.open_new_tab(url)


password = "omar"

user_input = input("Enter password: ")

if user_input == password:
    number = input("how many views do you want?")
    link = input("put the blog url: ")
    view()
else:
    print("Sorry, incorrect password")

