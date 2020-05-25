from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import tkinter.messagebox as msg
import re

class StudentDB:
    headers=['ID','First Name','Last Name','Email','Street','City','State',
             'Zip','Phone','DOB','Sex','Lunch']
    student_info=[]
    conn=None
    cursor=None
    query=None
    error_widget_list=None

    def __init__(self):
        self.tree=None
        self.username=StringVar(root,value='')
        self.pass_word=StringVar(root,value='')
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
        pass_entry=Entry(self.frame,textvariable=self.pass_word,show='*')
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
           len(self.pass_word.get())==0 or
           self.pass_word.get()!='khalsapanth1*'):
           self.error_var.set('Enter correct credentials!')
        #verify

        #now login#
        else:
            self.delete_login_widgets()
            root.geometry("1500x600")
            root.title("Manage Student Records")
            ##connect to db##
            try:
                self.conn=mysql.connector.connect(host='localhost',database='students',
                                                  username=self.username.get(),
                                                  password=self.pass_word.get())
            except Error as e:
                print(e)
            ##connect to db##
            self.create_widgets()

    def delete_login_widgets(self):
        for w in self.frame.grid_slaves():
            w.destroy()
        self.frame.destroy()

    def create_widgets(self):
        #----ROW1-----#

        #student_id#
        sid_label=Label(root,text='ID:')
        sid_label.grid(row=0,column=0,pady=10,sticky=W)
        self.sid_var=StringVar(root,value='')
        self.sid_entry=Entry(root,textvariable=self.sid_var)
        self.sid_entry.grid(row=0,column=1,pady=10,sticky=W)
        self.sid_err_var=StringVar(root,value='')
        self.sid_error_label=ttk.Label(root,textvariable=self.sid_err_var,foreground='red')
        self.sid_error_label.grid(row=0,column=2,sticky=W)
        #student_id#

        #firstname#
        f_name_label=Label(root,text='First Name:')
        f_name_label.grid(row=0,column=3,pady=10,sticky=W)
        self.f_name_var=StringVar(root,value='')
        self.f_name_entry=Entry(root,textvariable=self.f_name_var)
        self.f_name_entry.grid(row=0,column=4,pady=10,sticky=W)
        self.fname_err_var=StringVar(root,value='')
        self.fname_error_label=ttk.Label(root,textvariable=self.fname_err_var,foreground='red')
        self.fname_error_label.grid(row=0,column=5,sticky=W)
        #firstname#

        #lastname#
        l_name_label=Label(root,text='Last Name:')
        l_name_label.grid(row=0,column=6,pady=10,sticky=W)
        self.l_name_var=StringVar(root,value='')
        self.l_name_entry=Entry(root,textvariable=self.l_name_var)
        self.l_name_entry.grid(row=0,column=7,pady=10,sticky=W)
        self.lname_err_var=StringVar(root,value='')
        self.lname_error_label=ttk.Label(root,textvariable=self.lname_err_var,foreground='red')
        self.lname_error_label.grid(row=0,column=8,sticky=W)
        #lastname#

        #email#
        email_label=Label(root,text='Email:')
        email_label.grid(row=0,column=9,pady=10,sticky=W)
        self.email_var=StringVar(root,value='')
        self.email_entry=Entry(root,textvariable=self.email_var)
        self.email_entry.grid(row=0,column=10,pady=10,sticky=W)
        self.email_err_var=StringVar(root,value='')
        self.email_error_label=ttk.Label(root,textvariable=self.email_err_var,foreground='red')
        self.email_error_label.grid(row=0,column=11,sticky=W)
        #email#

        #street#
        street_label=Label(root,text='Street:')
        street_label.grid(row=0,column=12,pady=10,sticky=W)
        self.street_var=StringVar(root,value='')
        self.street_entry=Entry(root,textvariable=self.street_var)
        self.street_entry.grid(row=0,column=13,pady=10,sticky=W)
        self.street_err_var=StringVar(root,value='')
        self.street_error_label=ttk.Label(root,textvariable=self.street_err_var,foreground='red')
        self.street_error_label.grid(row=0,column=14,sticky=W)
        #street#

        #------ROW2-----#
        #city#
        city_label=Label(root,text='City:')
        city_label.grid(row=1,column=0,pady=10,sticky=W)
        self.city_var=StringVar(root,value='')
        self.city_entry=Entry(root,textvariable=self.city_var)
        self.city_entry.grid(row=1,column=1,pady=10,sticky=W)
        self.city_err_var=StringVar(root,value='')
        self.city_error_label=ttk.Label(root,textvariable=self.city_err_var,foreground='red')
        self.city_error_label.grid(row=1,column=2,sticky=W)
        #city#

        #state#
        state_label=Label(root,text='State:')
        state_label.grid(row=1,column=3,pady=10,sticky=W)
        self.state_var=StringVar(root,value='')
        self.state_entry=Entry(root,textvariable=self.state_var)
        self.state_entry.grid(row=1,column=4,pady=10,sticky=W)
        self.state_err_var=StringVar(root,value='')
        self.state_error_label=ttk.Label(root,textvariable=self.state_err_var,foreground='red')
        self.state_error_label.grid(row=1,column=5,sticky=W)
        #state#

        #zip#
        zip_label=Label(root,text='Zip:')
        zip_label.grid(row=1,column=6,pady=10,sticky=W)
        self.zip_var=StringVar(root,value='')
        self.zip_entry=Entry(root,textvariable=self.zip_var)
        self.zip_entry.grid(row=1,column=7,pady=10,sticky=W)
        self.zip_err_var=StringVar(root,value='')
        self.zip_error_label=ttk.Label(root,textvariable=self.zip_err_var,foreground='red')
        self.zip_error_label.grid(row=1,column=8,sticky=W)
        #zip#

        #phone#
        phone_label=Label(root,text='Phone:')
        phone_label.grid(row=1,column=9,pady=10,sticky=W)
        self.phone_var=StringVar(root,value='')
        self.phone_entry=Entry(root,textvariable=self.phone_var)
        self.phone_entry.grid(row=1,column=10,pady=10,sticky=W)
        self.phone_err_var=StringVar(root,value='')
        self.phone_error_label=ttk.Label(root,textvariable=self.phone_err_var,foreground='red')
        self.phone_error_label.grid(row=1,column=11,sticky=W)
        #phone#

        #DOB#
        dob_label=Label(root,text='DOB:')
        dob_label.grid(row=1,column=12,pady=10,sticky=W)
        self.dob_var=StringVar(root,value='')
        self.dob_entry=Entry(root,textvariable=self.dob_var)
        self.dob_entry.grid(row=1,column=13,pady=10,sticky=W)
        self.dob_err_var=StringVar(root,value='')
        self.dob_error_label=ttk.Label(root,textvariable=self.dob_err_var,foreground='red')
        self.dob_error_label.grid(row=1,column=14,sticky=W)
        #DOB#
        
        #------ROW3-----#
        #Sex#
        sex_label=Label(root,text='Sex:')
        sex_label.grid(row=2,column=0,pady=10,sticky=W)
        self.sex_var=StringVar(root,value='')
        self.sex_entry=ttk.Combobox(root,textvariable=self.sex_var)
        self.sex_entry['values']=('M','F')
        self.sex_entry.grid(row=2,column=1,pady=10,sticky=W)
        self.sex_err_var=StringVar(root,value='')
        self.sex_error_label=ttk.Label(root,textvariable=self.sex_err_var,foreground='red')
        self.sex_error_label.grid(row=2,column=2,sticky=W)
        #Sex#

        #Lunch#
        lunch_label=Label(root,text='Lunch:')
        lunch_label.grid(row=2,column=3,pady=10,sticky=W)
        self.lunch_var=StringVar(root,value='')
        self.lunch_entry=Entry(root,textvariable=self.lunch_var)
        self.lunch_entry.grid(row=2,column=4,pady=10,sticky=W)
        self.lunch_err_var=StringVar(root,value='')
        self.lunch_error_label=ttk.Label(root,textvariable=self.lunch_err_var,foreground='red')
        self.lunch_error_label.grid(row=2,column=5,sticky=W)
        #DOB#
        
        #buttons#
        add_button=Button(root,text='Add Student',command=self.add_student)
        add_button.grid(row=2,column=6,padx=5,pady=10,sticky='WE',columnspan=2)

        update_button=Button(root,text='Update Student',command=self.update_student)
        update_button.grid(row=2,column=9,padx=5,pady=10,sticky='WE',columnspan=2)

        delete_button=Button(root,text='Delete Student',command=self.delete_student)
        delete_button.grid(row=2,column=12,padx=5,pady=10,sticky='WE',columnspan=2)

        refresh_button=Button(root,text='Clear Entries',command=self.refresh_entries)
        refresh_button.grid(row=2,column=14,padx=5,pady=10,sticky='WE')
        #buttons#

        reset_tree_btn=Button(root,text='Reset Tree',command=self.update_tree)
        reset_tree_btn.grid(row=4,column=0,padx=5,pady=10,columnspan=14)

        #treeview#
        self.tree=ttk.Treeview(root,selectmode='browse',height=14,show='headings')
        self.tree['columns']=self.headers
        self.tree['show']='headings'
        self.tree.bind('<<TreeviewSelect>>',self.track_item)
        i=1
        for col in self.headers:
            col_id=f'#{i}'
            self.tree.column(col_id,width=113,anchor=CENTER)
            self.tree.heading(col_id,text=col,anchor=CENTER)
            i+=1
        self.tree.heading('First Name',command=self.sort_by_name)
        self.update_tree()
        self.tree.grid(row=3,column=0,columnspan=20)
        #treeview#

    
    def execute_query(self,query,result_expected):
        try:
            self.cursor=self.conn.cursor()
            self.cursor.execute(query)
            if result_expected:
                self.student_info=self.cursor.fetchall()
            self.conn.commit()
            self.cursor.close()

        except Error as e:
            msg.showwarning(title='dbError',message=e)
            
    
    def track_item(self,event=None):
        sel_item=self.tree.selection()[0]
        sel_item_info=self.tree.item(sel_item)
        sel_item_data=sel_item_info['values']
        self.sid_var.set(sel_item_data[0])
        self.f_name_var.set(sel_item_data[1])
        self.l_name_var.set(sel_item_data[2])
        self.email_var.set(sel_item_data[3])
        self.street_var.set(sel_item_data[4])
        self.city_var.set(sel_item_data[5])
        self.state_var.set(sel_item_data[6])
        self.zip_var.set(sel_item_data[7])
        self.phone_var.set(sel_item_data[8])
        self.dob_var.set(sel_item_data[9])
        self.sex_var.set(sel_item_data[10])
        self.lunch_var.set(sel_item_data[11])

    def refresh_entries(self):
        self.sid_var.set('')
        self.f_name_var.set('')
        self.l_name_var.set('')
        self.email_var.set('')
        self.street_var.set('')
        self.city_var.set('')
        self.state_var.set('')
        self.zip_var.set('')
        self.phone_var.set('')
        self.dob_var.set('')
        self.sex_var.set('')
        self.lunch_var.set('')

    def sort_by_name(self):
        self.query='''SELECT student_id,first_name,last_name,email,street,city,state,zip,phone,
                      birth_date,sex,lunch_cost
                      FROM students ORDER BY first_name'''
        if (self.conn.is_connected()):
            all_students=self.tree.get_children()
            if(len(all_students)!=0):
                self.tree.delete(*all_students)
            self.execute_query(self.query,True)

        for data in self.student_info:
            self.tree.insert('','end',values=data)


    def update_tree(self):
        self.query='''SELECT student_id,first_name,last_name,email,street,city,state,zip,phone,
                      birth_date,sex,lunch_cost
                      FROM students'''
        if (self.conn.is_connected()):
            all_students=self.tree.get_children()
            if(len(all_students)!=0):
                self.tree.delete(*all_students)
            self.execute_query(self.query,True)
        
        for data in self.student_info:
            self.tree.insert('','end',values=data)

    def apply_checks_on_entries(self,id_check,f_name,l_name,email,street,city,state,zip,phone,dob,sex,lunch):
        check_list=[]
        widget_with_error_lst=[]
        #patterns#
        name_pat='^[A-Z][a-z]+$'
        city_pat='^[A-Z][A-Za-z\s]+$'
        state_pat='^[A-Z]{2}$'
        street_pat='^[A-Z0-9]{1,5}[\w\s]+$'
        zip_pat='^[0-9]{5,12}$'
        phone_pat='^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        dob_pat='^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
        email_pat='^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
        lunch_pat='^[0-9]{1,3}\.[0-9]{1,3}$'
        sex_pat='^[MF]$'
        id_pat='^[1-9]+$'
        #patterns#

        #id
        if id_check:
            id_srch=re.search(id_pat,self.sid_var.get())
            if(id_srch is None):
                check_list.append(0)
                widget_with_error_lst.append(self.sid_err_var)
            else:
                check_list.append(1)
        #id

        #f_name
        f_srch=re.search(name_pat,f_name)
        if(f_srch is None):
            check_list.append(0)
            widget_with_error_lst.append(self.fname_err_var)

        else:
            check_list.append(1)
        #f_name

        #l_name
        l_srch=re.search(name_pat,l_name)
        if(l_srch is None):
            check_list.append(0)
            widget_with_error_lst.append(self.lname_err_var)
        else:
            check_list.append(1)
        #l_name

        #city#
        city_srch=re.search(city_pat,city)
        if(city_srch is None):
            check_list.append(0)
            widget_with_error_lst.append(self.city_err_var)
        else:
            check_list.append(1)
        #city

        #state#
        if(len(self.state_var.get())==2):
            state_srch=re.search(state_pat,state)
            if state_srch is None:
                check_list.append(0)
                widget_with_error_lst.append(self.state_err_var)
            else:
                check_list.append(1)
        else:
            check_list.append(0)
        #state#
        
        #street#
        street_search=re.search(street_pat,street)
        if(street_search is None):
             check_list.append(0)
             widget_with_error_lst.append(self.street_err_var)
        else:
            check_list.append(1)
        #street#

        #zip#
        zip_search=re.search(zip_pat,zip)
        if(zip_search is None):
            check_list.append(0)
            widget_with_error_lst.append(self.zip_err_var)
        else:
            check_list.append(1)
        #zip#

        #phone#
        ph_search=re.search(phone_pat,phone)
        if(ph_search is None or ph_search.span()[0]!=0):
            check_list.append(0)
            widget_with_error_lst.append(self.phone_err_var)
        else:
            check_list.append(1)
        #phone#

        #dob#
        dob_search=re.search(dob_pat,dob)
        if(dob_search is None):
            check_list.append(0)
            widget_with_error_lst.append(self.dob_err_var)
        else:
            birth_yr=int(dob[0:4])
            birth_mt=int(dob[5:7])
            birth_dy=int(dob[8:10])
            if((1970<=birth_yr<=2020) and (1<=birth_mt<=12) and (1<=birth_dy<=31)):
                check_list.append(1)
            else:
                check_list.append(0)
                widget_with_error_lst.append(self.dob_err_var)
        #dob#

        #sex#
        sex_search=re.search(sex_pat,sex)
        if(sex_search is None):
            check_list.append(0)
            widget_with_error_lst.append(self.sex_err_var)
        else:
            check_list.append(1)
        #sex#

        #email#
        email_search=re.search(email_pat,email)
        if(email_search is None):
            check_list.append(0)
            widget_with_error_lst.append(self.email_err_var)
        else:
            check_list.append(1)
        #email#
        
        #lunch#
        lunch_search=re.search(lunch_pat,lunch)
        if(lunch_search is None):
            check_list.append(0)
            widget_with_error_lst.append(self.lunch_err_var)
        else:
            check_list.append(1)
        #lunch#
        
        return all(check_list),widget_with_error_lst

    def remove_marks(self):
        if self.error_widget_list:
            for w in self.error_widget_list:
                w.set('')


    def all_entries_filled(self,id_need):
        if (len(self.f_name_var.get())==0 or
        len(self.l_name_var.get())==0 or
        len(self.email_var.get())==0 or
        len(self.street_var.get())==0 or
        len(self.city_var.get())==0 or
        len(self.state_var.get())==0 or
        len(self.zip_var.get())==0 or
        len(self.phone_var.get())==0 or
        len(self.dob_var.get())==0 or
        len(self.sex_var.get())==0 or
        len(self.lunch_var.get())==0):
            return False
        elif id_need:
            if(len(self.sid_var.get())==0):
                return False
            else:
                return True
        return True
           

    def add_student(self):
        entry_date=datetime.now()
        entry_date_format=entry_date.strftime('%Y-%m-%d')

        if self.all_entries_filled(False):
            f_name=self.f_name_var.get()
            l_name=self.l_name_var.get()
            email=self.email_var.get() 
            street=self.street_var.get()
            city=self.city_var.get()
            state=self.state_var.get()
            zip=self.zip_var.get()
            phone=self.phone_var.get()
            dob=self.dob_var.get()   
            sex=self.sex_var.get() 
            lunch=self.lunch_var.get()

            check_result_tup=self.apply_checks_on_entries(False,f_name,l_name,email,street,city,state,zip,phone,dob,sex,lunch)

            if check_result_tup[0]:

                self.query=f'''INSERT INTO students(first_name,last_name,email,street,city,state,zip,phone,birth_date,sex,date_entered,lunch_cost) 
                        VALUES('{f_name}','{l_name}','{email}','{street}','{city}','{state}',{zip},'{phone}',
                        '{dob}','{sex}','{entry_date_format}',{lunch})
                        '''
                if(self.conn.is_connected()):
                    self.execute_query(self.query,False)
                    self.update_tree()
                    self.remove_marks()
            else:

                self.error_widget_list=check_result_tup[1]
                for w in self.error_widget_list:
                    w.set('!')

                msg.showwarning(title='Enter Valid Data', message='Please enter valid information! Observe the already entered data in the tree for correct entries! ')
        
        else:
            self.pop_message("Ensure all fields have entries!")

    def update_student(self):
        if self.all_entries_filled(True):
            f_name=self.f_name_var.get()
            l_name=self.l_name_var.get()
            email=self.email_var.get() 
            street=self.street_var.get()
            city=self.city_var.get()
            state=self.state_var.get()
            zip=self.zip_var.get()
            phone=self.phone_var.get()
            dob=self.dob_var.get()   
            sex=self.sex_var.get()
            lunch=self.lunch_var.get()
            stu_id=self.sid_var.get()

            check_result_tup=self.apply_checks_on_entries(False,f_name,l_name,email,street,city,state,zip,phone,dob,sex,lunch)           
            if check_result_tup[0]:
                self.query=f'''UPDATE students SET first_name='{f_name}',last_name='{l_name}',email='{email}',
                            street='{street}',city='{city}',state='{state}',zip={zip},phone='{phone}',
                            birth_date='{dob}',sex='{sex}',lunch_cost={lunch} WHERE student_id={stu_id}'''

                if(self.conn.is_connected()):
                    self.execute_query(self.query,False)
                    self.update_tree()
                    self.remove_marks()
            else:
                self.error_widget_list=check_result_tup[1]
                for w in self.error_widget_list:
                    w.set('!')

                msg.showwarning(title='Enter Valid Data', message='Please enter valid information! Observe the already entered data in the tree for correct entries! ')
        
        else:
            self.pop_message("Ensure all fields have entries!")
            

    def delete_student(self):
        if len(self.sid_var.get())==0:
            self.pop_message("Please enter a ID")
        else:
            stu_id=self.sid_var.get()
            id_pat='^[1-9]+$'
            id_srch=re.search(id_pat,stu_id)
            if(id_srch is None):
                self.sid_err_var.set('!')
                self.pop_message("Please enter a valid ID")
            else:
                self.query=f'''DELETE FROM students WHERE student_id={stu_id}'''
                if(self.conn.is_connected()):
                    self.execute_query(self.query,False)
                    self.update_tree()
                    self.sid_err_var.set('')
    
    def pop_message(self,msg):
        popup_win=Toplevel()
        popup_win.title("Enter valid values")
        popup_win.resizable(height=False,width=False)
        popup_win.geometry("200x50")
        error_label=Label(popup_win,text=msg)
        error_label.pack()
        close_button=Button(popup_win,text='OK',command=popup_win.destroy)
        close_button.pack()

root=Tk()
stu_db=StudentDB()
root.mainloop()
