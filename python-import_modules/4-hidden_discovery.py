#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4  # import the compiled module

    names = dir(hidden_4)  # get all names defined in the module

    for name in sorted(names):  # sort alphabetically
        if not name.startswith("__"):  # ignore names starting with __
            print(name)  # print each name on its own line

