#!/usr/bin/env python
# coding: utf-8

# # Calculate HRA & DA

# In[7]:


en=int(input("Enter Employee No:"),10)
ena=input("Enter Employee Name:")
gen=input("Enter Employee Gender:")
sal=int(input("Enter Employee Salary:"),10)
if(gen=='M'):
     da=0.20*sal
     hra=0.25*sal
     tot=sal+da+hra
     print("Total Salary=:",tot)
elif(gen=='F'):
     da=0.15*sal
     hra=0.20*sal
     tot=sal+da+hra
     print("Total Salary=:",tot)
else:
    print("PLease enter Correct Gender")

