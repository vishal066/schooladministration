import csv

def write_into_csv(info):
    with open("student_info.csv","a",newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell() == "0":
            writer.writerow(["name","age","number","e-mail"])
        writer.writerow(info)
if __name__=="__main__":
    condition=True
    student_num=1
    while (condition):
        student_info=input("enter the student #{} info in name,age,number and e-mail:".format(student_num))
        student_info_list=student_info.split(" ")
        print("\nthe entered value-\n name: {}\nAge: {}\nnumber: {}\ne-mail: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("please enter (yes/no) if the values are correct:")
        if choice_check == "yes":
            student_num=student_num+1
            write_into_csv(student_info_list)
            condition_check=input("enter (yes/no) if you want to enter another student info:")
            if condition_check == "yes" :
                condition=True
            elif condition_check == "no" :
                condition=False
        elif choice_check == "no":
            print("please re-enter the values!")
