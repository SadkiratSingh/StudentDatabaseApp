from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

class StudentDB:
    headers=['ID','First Name','Last Name','Email','Street','City','State',
             'Zip','Phone','DOB','Sex','Lunch']
    student_info=[(1,'Harry', 'Truman', 'htruman@aol.com', '202 South St', 'Vancouver', 'WA', 98660,          '792-223-9810', '1946-1-24','M',3.50),(2,'Shelly', 'Johnson', 'sjohnson@aol.com', '9 Pond Rd', 'Sparks', 'NV', 89431, '792-223-6734', '1970-12-12','F', 3.50),(3,'Bobby', 'Briggs', 'bbriggs@aol.com', '14 12th St', 'San Diego', 'CA',92101, '792-223-6178', '1967-5-24','M', 3.50),(4,'Donna', 'Hayward', 'dhayward@aol.com', '120 16th St', 'Davenport', 'IA', 52801, '792-223-2001', '1970-3-24','F',3.50),(5,'Audrey', 'Horne', 'ahorne@aol.com', '342 19th St', 'Detroit', 'MI', 48222, '792-223-2001', '1965-2-1','F', 3.50),(6,'James', 'Hurley', 'jhurley@aol.com', '2578 Cliff St', 'Queens', 'NY', 11427, '792-223-1890', '1967-1-2','M',3.50)]

    conn=None
    cursor=None
    query=None

    def __init__(self):
        self.tree=None
        self.username=StringVar(root,value='')
        self.password=StringVar(root,value='')
        self.create_login_db()

    def create_login_db(self):
        root.title("Login")
        root.geometry('250x150')
        self.frame=Frame(root,width=250,height=150)
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1,weight=1)
        self.frame.pack()

        #username#
        user_label=Label(self.frame,text='Username:')
        user_label.grid(row=0,column=0,sticky='E',padx=5,pady=10)
        user_entry=Entry(self.frame,textvariable=self.username)
        user_entry.grid(row=0,column=1,sticky='W',padx=5,pady=10)
        #username#
    
        #password#
        pass_label=Label(self.frame,text='Password:')
        pass_label.grid(row=1,column=0,sticky='E',padx=5,pady=10)
        pass_entry=Entry(self.frame,textvariable=self.password,show='*')
        pass_entry.grid(row=1,column=1,sticky='W',padx=5,pady=10)
        #password#

        #button#
        login_button=Button(self.frame,text='login',command=self.login_and_connect)
        login_button.grid(row=2,column=0,padx=5,pady=10,columnspan=2)
        #button#

        #error_label#
        self.error_var=StringVar(root,value='')
        error_label=Label(self.frame,textvariable=self.error_var)
        error_label.grid(row=3,column=0,columnspan=2)
        #error_label#

    def login_and_connect(self):
        #verify#
        if(len(self.username.get())==0 or
           self.username.get()!='studentadmin' or
           len(self.password.get())==0 or
           self.password.get()!='khalsapanth1*'):
           self.error_var.set('Enter correct credentials!')
        #verify

        #now login#
        else:
            self.delete_login_widgets()
            root.geometry("1500x600")
            root.title("Manage Student Records")
            self.create_widgets()

    def delete_login_widgets(self):
        for w in self.frame.grid_slaves():
            w.destroy()
        self.frame.destroy()

    def create_widgets(self):
        #----ROW1-----#

        #student_id#
        sid_label=Label(root,text='ID:')
        sid_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)
        self.sid_var=StringVar(root,value='')
        sid_entry=Entry(root,textvariable=self.sid_var)
        sid_entry.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        #student_id#

        #firstname#
        f_name_label=Label(root,text='First Name:')
        f_name_label.grid(row=0,column=2,padx=5,pady=10,sticky=W)
        self.f_name_var=StringVar(root,value='')
        f_name_entry=Entry(root,textvariable=self.f_name_var)
        f_name_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        #firstname#

        #lastname#
        l_name_label=Label(root,text='Last Name:')
        l_name_label.grid(row=0,column=4,padx=5,pady=10,sticky=W)
        self.l_name_var=StringVar(root,value='')
        l_name_entry=Entry(root,textvariable=self.l_name_var)
        l_name_entry.grid(row=0,column=5,padx=5,pady=10,sticky=W)
        #lastname#

        #email#
        email_label=Label(root,text='Email:')
        email_label.grid(row=0,column=6,padx=5,pady=10,sticky=W)
        self.email_var=StringVar(root,value='')
        email_entry=Entry(root,textvariable=self.email_var)
        email_entry.grid(row=0,column=7,padx=5,pady=10,sticky=W)
        #email#

        #street#
        street_label=Label(root,text='Street:')
        street_label.grid(row=0,column=8,padx=5,pady=10,sticky=W)
        self.street_var=StringVar(root,value='')
        street_entry=Entry(root,textvariable=self.street_var)
        street_entry.grid(row=0,column=9,padx=5,pady=10,sticky=W)
        #street#

        #------ROW2-----#
        #city#
        city_label=Label(root,text='City:')
        city_label.grid(row=1,column=0,padx=5,pady=10,sticky=W)
        self.city_var=StringVar(root,value='')
        city_entry=Entry(root,textvariable=self.city_var)
        city_entry.grid(row=1,column=1,padx=5,pady=10,sticky=W)
        #city#

        #state#
        state_label=Label(root,text='State:')
        state_label.grid(row=1,column=2,padx=5,pady=10,sticky=W)
        self.state_var=StringVar(root,value='')
        state_entry=Entry(root,textvariable=self.state_var)
        state_entry.grid(row=1,column=3,padx=5,pady=10,sticky=W)
        #state#

        #zip#
        zip_label=Label(root,text='Zip:')
        zip_label.grid(row=1,column=4,padx=5,pady=10,sticky=W)
        self.zip_var=StringVar(root,value='')
        zip_entry=Entry(root,textvariable=self.zip_var)
        zip_entry.grid(row=1,column=5,padx=5,pady=10,sticky=W)
        #zip#

        #phone#
        phone_label=Label(root,text='Phone:')
        phone_label.grid(row=1,column=6,padx=5,pady=10,sticky=W)
        self.phone_var=StringVar(root,value='')
        phone_entry=Entry(root,textvariable=self.phone_var)
        phone_entry.grid(row=1,column=7,padx=5,pady=10,sticky=W)
        #phone#

        #DOB#
        dob_label=Label(root,text='DOB:')
        dob_label.grid(row=1,column=8,padx=5,pady=10,sticky=W)
        self.dob_var=StringVar(root,value='')
        dob_entry=Entry(root,textvariable=self.dob_var)
        dob_entry.grid(row=1,column=9,padx=5,pady=10,sticky=W)
        #DOB#
        
        #------ROW3-----#
        #Sex#
        sex_label=Label(root,text='Sex:')
        sex_label.grid(row=2,column=0,padx=5,pady=10,sticky=W)
        self.sex_var=StringVar(root,value='')
        sex_entry=Entry(root,textvariable=self.sex_var)
        sex_entry.grid(row=2,column=1,padx=5,pady=10,sticky=W)
        #Sex#

        #Lunch#
        lunch_label=Label(root,text='Lunch:')
        lunch_label.grid(row=2,column=2,padx=5,pady=10,sticky=W)
        self.lunch_var=StringVar(root,value='')
        lunch_entry=Entry(root,textvariable=self.lunch_var)
        lunch_entry.grid(row=2,column=3,padx=5,pady=10,sticky=W)
        #DOB#
        
        #buttons#
        add_button=Button(root,text='Add Student',command=self.add_student)
        add_button.grid(row=2,column=4,padx=5,pady=10,sticky='WE')

        update_button=Button(root,text='Update Student',command=self.update_student)
        update_button.grid(row=2,column=5,padx=5,pady=10,sticky='WE')

        delete_button=Button(root,text='Delete Student',command=self.delete_student)
        delete_button.grid(row=2,column=6,padx=5,pady=10,sticky='WE')
        #buttons#

        #treeview#
        self.tree=ttk.Treeview(root,selectmode='browse',height=14,show='headings')
        self.tree['columns']=self.headers
        self.tree['show']='headings'
        i=1
        for col in self.headers:
            col_id=f'#{i}'
            self.tree.column(col_id,width=113,anchor=CENTER)
            self.tree.heading(col_id,text=col,anchor=CENTER)
            i+=1
        for data in self.student_info:
            self.tree.insert('','end',values=data)

        self.tree.grid(row=3,column=0,columnspan=20)
        #treeview#

    def add_student(self):
        pass

    def update_student(self):
        pass

    def delete_student(self):
        pass

        
        


root=Tk()
#root.geometry('1500x600')
#root.title("StudentRecords")
stu_db=StudentDB()
root.mainloop()
