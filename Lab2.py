def display_main_menu():
    print("Enter some numbers separated by commas(e.g., 5,6,7,32)")


def get_user_input():
   input_num = input()
   numbers=input_num.split(",")
   num_list=[float(string)for string in numbers]
   return num_list


def calc_average_temperature(num_list):
   avg_temp = sum(num_list)/len(num_list)
   return avg_temp

def calc_min_max_temperature(num_list):
    min_max_list=[min(num_list),max(num_list)]
    return min_max_list

def main():
    print ("ET0735 (DevOpa for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list=get_user_input()
    print(num_list)
    avg_temp=calc_average_temperature(num_list)
    print("The average temperature is",avg_temp)
    min_max_list=calc_min_max_temperature(num_list)
    print("The minimum and maximum temperatures are ",min_max_list)
if __name__=="__main__":
    main()