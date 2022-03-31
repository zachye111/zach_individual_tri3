from Week_1 import lists
from Week_0 import animation, matrix, mnms

main_menu = [
    ["Animation", animation.animation],
    ["Tree", "Week_0/tree.py"],
]

# Submenu list
sub_menu = [
    ["Swaps", "Week_0/swaps.py"],
    ["Matrix", matrix.driver],
]

sub_menu_math = [
    ["Factorial", "Week_2/factorial.py"],
    ["Fibonacci", "Week_1/fibonacci.py"],
    ["MNMS", mnms.myur],
]

patterns_sub_menu = [
    ["Health", "health.py"],
]

lists_sub_menu = [
    ["Lists", lists.tester],
    ["Factorial", lists.tester2],
    ["Fibonacci", lists.fibtester],
]

# Prompt for menu selection
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"



# references for main menu as well as sub menu's

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Swaps and Matrix", submenu])
    menu_list.append(["Create Task", patterns_submenu])
    menu_list.append(["Lists", lists_submenu])
    menu_list.append(["Math", submenu_math])
    buildMenu(title, menu_list)

# using sub menu list above, defining sub menu
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)
def lists_submenu():
    title = "Lists Submenu" + banner
    buildMenu(title, lists_sub_menu)
def submenu_math():
    title = "Math Submenu" + banner
    buildMenu(title, sub_menu_math)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()