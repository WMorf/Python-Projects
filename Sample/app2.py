

import app1


def print_app2():
    name = (__name__)
    return name


if __name__ == "__main__":
    # The Following is calling code within this script
    print("I am running code from {}".format(print_app2()))

    # The Following is calling code from imported app1.py
    print("I am running code from {}".format(app1.print_app()))
