import re
# Function to write TV shows to a file
def write_show(shows):
    with open('shows_list.txt', 'w') as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")

# Function to add a show to our shows list in dictionary format and write it to our file with the write_show function
def add_show(shows):
    title = input("What is the title of the show?")
    platform = input("where can we watch it?")
    genre = input("What genre is it?")
    shows.append({'Title': title, 'Platform': platform, 'Genre': genre})
    write_show(shows) # write to shows file

# Functin to Read TV shows from a file
def read_shows():
    shows_list = []
    try:
        with open('shows_list.txt', 'r') as file:
            for line in file:
                data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
                shows_list.append({'Title': data.group(1), 'Platform': data.group(2), 'Genre': data.group(3).strip()})
    except FileNotFoundError:
        pass  
    return shows_list


# Function to print the listof shows forthe user in a formatted way
def view(shows):
    print("\nShows List")
    print('----------------')
    for idx, show in enumerate(shows):
        vowels = ['a', 'e', 'i', 'o', 'u']
        a_or_an = 'an' if show['Genre'][0].lower() in vowels else 'a'
        print(f"{idx + 1}.) {show['Title']} is {a_or_an} {show['Genre']} show on {show['Platform']}") 

# Function to show our current list of shows and allow the user to chose which to remove
def remove_show(shows):
    view(shows)
    option = int(input("\n\nChose a number for the show you'd like to remove:"))
    show = shows.pop(option - 1) # index - 1
    print(f"\n{show['Title']} was successfully removed")
    write_show(shows)
    
def edit_show(shows):
    if not shows:
        print("\nNo shows to edit")
        return
    view(shows)
    try:
        option = int(input("\nChoose a number of the show to edit: "))
        if option < 1 or option > len(shows):
            print("Invalid number.")
            return
    except ValueError:
        print("Please enter a a valid number.")
        return
    selected_show = shows[option - 1]
    print(f"\nCurrent details")
    print(f"Title: {selected_show['Title']}")
    print(f"Platform: {selected_show['Platform']}")
    print(f"Genre:{selected_show['Genre']}")

    field = input("\nWhich field would you like to edit (Platform/Genre?) ").strip().lower()
    while field not in ['platform', 'genre']: 
        print("Invalid field. Please enter 'Platform' or 'Genre'.")
        field = input(("Which field would you like to edit (Platform/Genre?) ")).strip().lower()

    new_value = input(f"Enter new {field}: ")
    selected_show[field.capitalize()] = new_value
    write_show(shows)
    print("\nShow updated successfully!")


#** Building the Interactive Program
# Main Function to run the TV show manager
def main():
    while True:
        shows_list = read_shows()
        action = input('''
Options
--------------
1 - Add a TV Show
2 - Remove a TV Show
3 - View List of TV Shows
4 - Edit a TV Show
5 - Quit

Enter your choice (1-5): ''')
        
        if action == '1':
            add_show(shows_list)
        elif action == '2':
            remove_show(shows_list)
        elif action == '3':
            view(shows_list)
        elif action == '4':
            edit_show(shows_list)
        elif action == '5':
            print("\nThanks for using this app!")
            break
        else:
            print("\nInvalid choice. Please select 1-5.")

main()