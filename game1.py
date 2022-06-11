#
#   Python: 3
#
#   Author: Wesley Morford
#
#   Purpose: Program demonstrating passing variables between functions



def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name,l_name,age,gender)



def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am a {} yearold {}.".format(f_name,l_name,age,gender))
    





if __name__ == "__main__":
   start()
