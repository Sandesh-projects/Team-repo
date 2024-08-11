
try:
    with open("file.txt") as file:
        """
        it open by default in reading mode
        it doesn't create a file if it not present
        """
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found")




with open('new_file.txt', 'w') as file:
    """
    it does create a file if it not present
    """
    file.write("My name is anthony gonsalves")


with open('new_file.txt', 'a') as file:
    """
    it add an content to the file
    """
    file.write("\nPlayed by amitabh bachan")