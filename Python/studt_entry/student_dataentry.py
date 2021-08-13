# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:35:59 2021

@author: zahid
"""

import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact number","E-mail id"])
        
        writer.writerow(info_list)
        
if __name__=='__main__':
    condition=True
    
    while(condition):
        student_info=input("Enter student information in following format(Name   Age  Contact Number  Email id):")
        
        student_info_list=student_info.split(' ')
        
        print("\n the entered information is -\nName:{}\nAge:{}\nContact_Number:{}\nEmail_ID:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        
        choice_check=input("Is the entered information correct?(yes/no):")
        
        
        if choice_check=="yes":
            write_into_csv(student_info_list)
            
            condition_check=input("Enter (yes/no) if you want to enter information for another student:")
            
            if condition_check=="yes":
                condition=True
            elif condition_check=="no":
                condition=False
        elif choice_check=="no":
            print("\n Please re-enter the value")