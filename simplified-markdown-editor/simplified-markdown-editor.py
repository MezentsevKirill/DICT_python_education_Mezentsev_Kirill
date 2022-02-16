command_list = ["plain", "bold", "italic", "header", "link", "inline-code",
                "ordered-list", "unordered-list", "new-line", "!help", "!done"]


def choose_a_formatter():
    user_formatter = input("Choose a formatter: > ")
    if user_formatter not in command_list:
        print("Unknown formatting type or command")
    elif user_formatter == command_list[9]:
        print("Available formatters: plain, bold, italic, header, link, inline-code,"
              "ordered-list, unordered-list, new-line")
    elif user_formatter == command_list[10]:
        raise SystemExit


choose_a_formatter()
