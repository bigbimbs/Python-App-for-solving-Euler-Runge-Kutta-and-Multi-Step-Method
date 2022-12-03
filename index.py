import sys 
import euler_fn
import runge_kutta_fn
import multi_step_method_fn

def run_program():
    invalid_selection_solution = False
    allowed_selections = ["A", "B", "C"]
    while invalid_selection_solution == False:
        select_which_method = input("Please input A for Euler or input B for Runge Kutta or input C for Multi step method ").upper()
        if allowed_selections.__contains__(select_which_method) == False:
            print("Invalid Selection, please try again later")
        else:
            invalid_selection_solution = True
            if select_which_method == "A":
                check_if_inputs_are_valid = False
                print("Euler Method selected successfully, please enter the values requested which will be x0, y, x, and h")
                v_x0 = v_y = v_x = v_h = ""
                while(check_if_inputs_are_valid == False):
                    try:
                        v_x0 = float(input("Please enter the value of x0, "))
                        v_y = float(input("Please enter the value for y, "))
                        v_h = float(input("Please enter the value for h, "))
                        v_x = float(input("Please enter the value for x, "))
                    except:
                        print("One of the input is not an integer")
                
                    if(isinstance(v_x0, float) and isinstance(v_y, float) and isinstance(v_x, float) and isinstance(v_h, float)):
                        check_if_inputs_are_valid = True
                        euler_fn.euler(v_x0, v_y, v_h, v_x)
                        print("Success")
                        check_if_user_want_to_continue = input("Please enter Y if you want to run the program again or press any other key to quit the program, ").lower()
                        if(check_if_user_want_to_continue == "y"):
                            run_program()
                        else:
                            sys.exit()
                    else:
                        print("One of the input is not an integer please try again")
            elif select_which_method == "B":
                check_if_inputs_are_valid = False
                print("Runge Kutta selected successfully, please enter the values requested which will be x0, y0, x, and h")
                v_x0 = v_y0 = v_x = v_h = ""
                while(check_if_inputs_are_valid == False):
                    try: 
                        v_x0 = float(input("Please enter the value of x0, "))
                        v_y0 = float(input("Please enter the value for y0, "))
                        v_x = float(input("Please enter the value for x, "))
                        v_h = float(input("Please enter the value for h, "))
                    except:
                        print("One of the input is not an integer") 
                    if(isinstance(v_x0, float) and isinstance(v_y0, float) and isinstance(v_x, float) and isinstance(v_h, float)):
                        check_if_inputs_are_valid = True
                      
                        print ('The value of y at x is:', runge_kutta_fn.runge_Kutta(v_x0, v_y0, v_x, v_h))
                        print("Success")
                        check_if_user_want_to_continue = input("Please enter Y if you want to run the program again or press any other key to quit the program, ").lower()
                        if(check_if_user_want_to_continue == "y"):
                            run_program()
                        else:
                            sys.exit()
                    else:
                        print("please try again")
            elif select_which_method == "C":
                check_if_inputs_are_valid = False
                print("Multi step method selected successfully, please enter the values requested which will be x, xn, y, h")
                v_x = v_xn = v_y = v_h = ""
                while(check_if_inputs_are_valid == False):
                    try: 
                        v_x = float(input("Please enter the value of x0, "))
                        v_xn = float(input("Please enter the value for xn, "))
                        v_y = float(input("Please enter the value for y, "))
                        v_h = float(input("Please enter the value for h, "))
                    except:
                        print("One of the input is not an integer")
                    if(isinstance(v_x, float) and isinstance(v_xn, float) and isinstance(v_y, float) and isinstance(v_h, float)):
                        check_if_inputs_are_valid = True
                        multi_step_method_fn.printFinalValues(v_x, v_xn, v_y, v_h)
                        print("Success")
                        check_if_user_want_to_continue = input("Please enter Y if you want to run the program again or press any other key to quit the program, ").lower()
                        if(check_if_user_want_to_continue == "y"):
                            run_program()
                        else:
                            sys.exit()
                    else:
                        print("please try again")
            else:
                print("Invalid selection")
            
run_program()
