import os
import shutil
from time import sleep
from tkinter import *
from tkinter import messagebox
import psutil
import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate(r"cleaner-app-50143-firebase-adminsdk-cej46-ef12406467.json")
firebase_admin.initialize_app(cred)



def main_app():

    root = Tk()

    screen_height = 700
    screen_width = 1000

    # root.resizable(False, False)
    root.geometry('1000x600')
    # appbar
    appbar = Frame(root, bg='#004AAD', height=70, relief='flat')
    appbar.pack(fill=X, side='top', anchor='ne')

    logo_path = PhotoImage(file='assets/icon.png')
    logo_path = logo_path.zoom(2)
    logo_path = logo_path.subsample(32)
    logo = Label(appbar, image= logo_path, width= 60 , height= 30, bg='#004AAD')
    logo.pack(side= 'left', pady= 10)

    app_name_lbl = Label(appbar, text='Secure Optimizer', font= ("DM Sans", 12, 'bold'), fg = 'white', bg = '#004AAD', relief='flat')
    app_name_lbl.pack(side= 'left', pady= 10, padx = 15)



    contact_lbl = Label(appbar, text='657-541-749', font= ("DM Sans", 12), fg = 'white', bg = '#004AAD', relief='flat')
    contact_lbl.pack(side= 'right', pady= 10, padx = 5)

    phone_icon_path = PhotoImage(file='assets/phone.png')
    phone_icon_path = phone_icon_path.zoom(15)
    phone_icon_path = phone_icon_path.subsample(32)
    phone_icon = Label(appbar, image= phone_icon_path, width= 40 , height= 40, bg='#004AAD')
    phone_icon.pack(side= 'right', pady= 10)



    # bottomnavbar
    bottomnavbar = Frame(root, bg='#004AAD', height=50, relief='flat', borderwidth=2)
    bottomnavbar.pack(fill=X, side=BOTTOM, anchor = 'sw')

    rights_lbl = Label(bottomnavbar, text='Secure Optimizer @2022', font= ("DM Sans", 11, ), fg = 'white', bg = '#004AAD', relief='flat')
    rights_lbl.pack(side= 'left', pady= 10, padx = 15)

    pp_btn = Button(bottomnavbar, text='Privacy Policy', font= ("DM Sans", 11, ), fg = 'white', bg = '#004AAD', relief='flat')
    pp_btn.pack(side= 'right', pady= 10, padx = 5)


    t_and_c_btn = Button(bottomnavbar, text='Terms And Conditions', font= ("DM Sans", 11, ), fg = 'white', bg = '#004AAD', relief='flat')
    t_and_c_btn.pack(side= 'right', pady= 10, padx = 5)

    # sidebar
    sidebar = Frame(root, bg='#ECF0F5', relief='solid', borderwidth=1,border=0, bd= 1)
    sidebar.pack( fill=Y, side=LEFT, anchor='nw')

    def mem_cleaner_func():
        app_name_lbl['text'] = 'Secure Optimizer'
        # contact_lbl.pack(side= 'right', pady= 10, padx = 5)
        # phone_icon.pack(side= 'right', pady= 10)
        activationkey_frame.pack_forget()
        dashboard.pack( expand=True, fill= BOTH, anchor = 'ne')
        memory_cleaner_frame.pack_forget()
        finished_scan_frame.pack_forget()
        

    mem_cleaner_btn = Button(sidebar, text='Memory Cleaner', fg = 'black', font= ("DM Sans", 11, 'bold'), bg = '#ECF0F5', relief='flat', command= mem_cleaner_func)
    mem_cleaner_btn.pack(side= 'top', pady= 20)


    def cache_cleaner_func():
        # contact_lbl.pack_forget()
        # phone_icon.pack_forget()
        app_name_lbl['text'] = 'Scan your PC'
        activationkey_frame.pack_forget()
        dashboard.pack_forget()
        finished_scan_frame.pack_forget()
        memory_cleaner_frame.pack(expand = True, fill = BOTH, anchor = 'ne')
        folder = 'C:\Windows\Temp'
        # sleep(1)
        # directory_list = os.listdir(folder)
        # number_files = len(directory_list)
        # print(directory_list)
        # print(number_files)  
        # size=0
        # for ele in os.scandir(folder):
        #     size+=os.stat(ele).st_size
        # size_in_mb = round(size/2**20,2)
        # print(size_in_mb)
        try:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(e)
            root.after(200)
            if messagebox.showinfo('success', 'Cache cleaned successfully'):
                app_name_lbl['text'] = 'Secure Optimizer'
                # contact_lbl.pack(side= 'right', pady= 10, padx = 5)
                # phone_icon.pack(side= 'right', pady= 10)
                activationkey_frame.pack_forget()
                dashboard.pack( expand=True, fill= BOTH, anchor = 'ne')
                memory_cleaner_frame.pack_forget()
                finished_scan_frame.pack_forget()
        except Exception as e:
            messagebox.showerror('Failure', 'An error occured... Try again!')
            print('e')
        

    cache_cleaner_btn = Button(sidebar, text='Cache Cleaner', fg = 'black', font= ("DM Sans", 11, 'bold'), bg = '#ECF0F5', relief='flat', command= cache_cleaner_func)
    cache_cleaner_btn.pack(side= 'top', pady= 20)

    def activation_key_func():
        # contact_lbl.pack_forget()
        # phone_icon.pack_forget()
        app_name_lbl['text'] = 'Secure Optimizer'
        dashboard.pack_forget()
        memory_cleaner_frame.pack_forget()
        finished_scan_frame.pack_forget()
        activationkey_frame.pack(expand = True, fill = BOTH, anchor = 'ne')

    activation_key_btn = Button(sidebar, text='Activation Key', fg = 'black', font= ("DM Sans", 11, 'bold'), bg = '#ECF0F5', relief='flat', command= activation_key_func)
    activation_key_btn.pack(side= 'top', pady= 20)

    # main content area
    dashboard = Frame(root, bg='#ECF0F5',)
    dashboard.pack( expand=True, fill= BOTH, anchor = 'ne')

    caution_frame = Frame(dashboard, bg='#ECF0F5',)
    caution_frame.pack(fill=X, side='top', anchor='ne', expand=True, padx = screen_width * 0.15, ipadx=50)

    caution_icon_path = PhotoImage(file='assets/caution.png')
    caution_icon_path = caution_icon_path.zoom(15)
    caution_icon_path = caution_icon_path.subsample(32)
    caution_icon = Label(caution_frame, image= caution_icon_path, width= 40 , height= 40, bg='#ECF0F5')
    caution_icon.pack(side= 'left', pady= 5)

    optimizing_lbl = Label(caution_frame, text='Optimising items frees up storage space on your device. ', font= ("DM Sans", 11, ), fg = 'black', bg = '#ECF0F5', relief='flat')
    optimizing_lbl.pack(side= 'left', pady= 5)

    def scan_btn_func():
        app_name_lbl['text'] = 'Scan your PC'
        # contact_lbl.pack_forget()
        # phone_icon.pack_forget()
        activationkey_frame.pack_forget()
        dashboard.pack_forget()
        finished_scan_frame.pack_forget()
        memory_cleaner_frame.pack(expand = True, fill = BOTH, anchor = 'ne')
        folder = 'C:\Windows\Prefetch'
        # sleep(1)
        directory_list = os.listdir(folder)
        number_files = len(directory_list)
        print(directory_list)
        print(number_files)  
        size=0
        for ele in os.scandir(folder):
            size+=os.stat(ele).st_size
        size_in_mb = round(size/2**20,2)
        print(size_in_mb)
        total_junks_label['text'] = f'Total Junks: {number_files} items'
        total_junks_size_label['text'] = f'Total Junks Size: {size_in_mb} MB'
        for value in directory_list:
            listbox.insert(END, value)
        memory_cleaner_frame.pack_forget()
        finished_scan_frame.pack(expand = True, fill = BOTH, anchor = 'ne')

    t_and_c_btn = Button(caution_frame, text='Scan Now!', command= scan_btn_func, activebackground='#ECF0F5' ,font= ("DM Sans", 11, ), bg = '#ECF0F5', fg = '#004AAD', relief='flat')
    t_and_c_btn.pack(side= 'left', pady= 5)

    scan_btn_path = PhotoImage(file='assets/Group 24.png')
    scan_btn_path = scan_btn_path.zoom(15)
    scan_btn_path = scan_btn_path.subsample(32)
    scan_btn = Button(dashboard, image= scan_btn_path, activebackground='#ECF0F5',command= scan_btn_func , width= screen_height *0.25 , height= screen_height *0.25 , bg='#ECF0F5', relief='flat')
    scan_btn.pack(side = TOP, padx = 20, pady = 10, anchor = CENTER)


    stats_frame = Frame(dashboard, bg='#ECF0F5',)
    stats_frame.pack(fill=X, side='top', anchor=CENTER, expand=True)


    gradient_circle_path = PhotoImage(file='assets/Group 20.png')
    gradient_circle_path = gradient_circle_path.zoom(20)
    gradient_circle_path = gradient_circle_path.subsample(32)

    empty_sizedbox = Label(stats_frame, text='', bg='#ECF0F5')
    empty_sizedbox.pack(side= 'left', anchor = CENTER, padx = 150)

    memory_frame = Frame(stats_frame, bg='#ECF0F5',)
    memory_frame.pack(fill=X, side='left', anchor=CENTER, padx = 12)


    memory_usage_var = int(psutil.virtual_memory().percent)

    mem_usage_circle = Label(memory_frame, image= gradient_circle_path, text=f'{memory_usage_var}%', compound= CENTER ,width= 50 , height= 50, bg='#ECF0F5')
    mem_usage_circle.pack(side= 'top', anchor = CENTER)

    cpu_temp_circle = Label(memory_frame, text='Memory\nUsage', bg='#ECF0F5')
    cpu_temp_circle.pack(side= 'top', anchor = CENTER)

    cpu_frame = Frame(stats_frame, bg='#ECF0F5',)
    cpu_frame.pack(fill=X, side='left', anchor=CENTER, padx = 12)

    cpu_temp_var = '50°'


    cpu_temp_circle = Label(cpu_frame, image= gradient_circle_path, text=f'{cpu_temp_var}', compound= CENTER ,width= 50 , height= 50, bg='#ECF0F5')
    cpu_temp_circle.pack(side= 'top', anchor = CENTER)

    cpu_temp_circle = Label(cpu_frame, text='CPU\nTemprature', bg='#ECF0F5')
    cpu_temp_circle.pack(side= 'top', anchor = CENTER)


    storage_frame = Frame(stats_frame, bg='#ECF0F5',)
    storage_frame.pack(fill=X, side='left', anchor=CENTER, padx = 12)

    storage_usage_var = int(psutil.disk_usage('/').percent)

    storage_usage_circle = Label(storage_frame, image= gradient_circle_path, text=f'{storage_usage_var}%', compound= CENTER ,width= 50 , height= 50, bg='#ECF0F5')
    storage_usage_circle.pack(side= 'top', anchor = CENTER)

    storage_usage_circle = Label(storage_frame, text='Storage\nUsage', bg='#ECF0F5')
    storage_usage_circle.pack(side= 'top', anchor = CENTER)


    space_clear = Label(dashboard, text='1.2 GB space can be cleared', font= ("DM Sans", 12, ), bg='#ECF0F5')
    space_clear.pack(side= 'top', anchor = CENTER, pady = 20)

    thisfolder = 'C:\Windows\Prefetch' 
    sizegb=0
    for ele in os.scandir(thisfolder):
        sizegb+=os.stat(ele).st_size
    size_in_gb = round(sizegb/2**30,3)
    print(size_in_gb)

    space_clear['text'] = f'{size_in_gb} GB space can be cleared'

    # activationkey.pack_forget()
    # cachecleaner.pack_forget()
    # dashboard.pack_forget()
    memory_cleaner_frame = Frame(root, bg='#ECF0F5')
    # memory_cleaner_frame.pack(expand = True, fill = BOTH, anchor = 'ne')

    # memory_cleaner_ui(memory_cleaner_frame)

    # scanning_frame = Frame(memory_cleaner_frame, bg='#ECF0F5')
    # scanning_frame.pack(expand=True, fill=BOTH)

    gradient_circle_frame_path = PhotoImage(file='assets/gradient_frame.png')
    gradient_circle_frame_path = gradient_circle_frame_path.zoom(15)
    gradient_circle_frame_path = gradient_circle_frame_path.subsample(32)

    empty_sizedbox = Label(memory_cleaner_frame, text='', bg='#ECF0F5')
    empty_sizedbox.pack(side= 'top', anchor = CENTER, pady = 30)

    cpu_temp_circle = Label(memory_cleaner_frame, image= gradient_circle_frame_path,font= ("DM Sans", 12,), text='Scanning... ', compound= CENTER ,width= 150 , height= 150, bg='#ECF0F5', fg='#7ED957')
    cpu_temp_circle.pack(anchor = CENTER, side= TOP, pady= 30)

    scanning_doc = Label(memory_cleaner_frame, text='Scanning Documents .....', font= ("DM Sans", 12, ), bg='#ECF0F5')
    scanning_doc.pack(side= 'top', anchor = CENTER)

    # memory_cleaner_frame.pack_forget()
    finished_scan_frame = Frame(root, bg='#ECF0F5',)
    # finished_scan_frame.pack(expand = True, fill = BOTH, anchor = 'ne')

    check_icon_path = PhotoImage(file='assets/checked.png')
    check_icon_path = check_icon_path.zoom(7)
    check_icon_path = check_icon_path.subsample(10)

    check_icon = Label(finished_scan_frame, image= check_icon_path ,width= 230 , height= 230, bg='#ECF0F5')
    check_icon.pack(anchor = 'nw', side= TOP, padx= 70, pady= 20)

    total_data_frame = Frame(finished_scan_frame, bg='#ECF0F5',)
    total_data_frame.place(x=screen_width * 0.5, y=screen_height * 0.05)

    scan_finished_label = Label(total_data_frame, text='Scan Finished', font= ("DM Sans", 14, 'bold'), bg='#ECF0F5')
    scan_finished_label.pack(side= 'top', anchor = 'ne', pady = 30, padx= 40)

    total_junks_label = Label(total_data_frame, text='Total Junks: 863 items', font= ("DM Sans", 12, ), bg='#ECF0F5')
    total_junks_label.pack(side= 'top', anchor = 'nw')

    total_junks_size_label = Label(total_data_frame, text='Total Junks Size: 9574 MB', font= ("DM Sans", 12, ), bg='#ECF0F5')
    total_junks_size_label.pack(side= 'top', anchor = 'nw', pady=10)

    def clean_now_func():
        second_folder = 'C:\Windows\Prefetch'
        try:
            for filename in os.listdir(second_folder):
                file_path = os.path.join(second_folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(e)
            if messagebox.showinfo('success', 'files cleaned successfully'):
                app_name_lbl['text'] = 'Secure Optimizer'
                # contact_lbl.pack(side= 'right', pady= 10, padx = 5)
                # phone_icon.pack(side= 'right', pady= 10)
                activationkey_frame.pack_forget()
                dashboard.pack( expand=True, fill= BOTH, anchor = 'ne')
                memory_cleaner_frame.pack_forget()
                finished_scan_frame.pack_forget()
        except Exception as e:
            messagebox.showerror('Failure', 'An error occured... Try again!')
            print('e')

    clean_now_btn = Button(total_data_frame, text='Clean Now', command= clean_now_func, relief='flat' , font= ("DM Sans", 13, ), bg='#004AAD', fg='white')
    clean_now_btn.pack(side= 'top', anchor = 'nw', pady=20, ipadx=120, ipady=5)


    rect_frame = Frame(finished_scan_frame, bg='#ECF0F5', width=100,background='#ECF0F5', relief='solid', border=1, borderwidth=1)
    rect_frame.pack(side= 'top', anchor = 'center', fill=X, padx = 50,pady = 15)

    # junks_frame_label = Label(root, text='Junk-9574 MB', font= ("DM Sans", 12, ), bg='#ECF0F5', fg='black')
    # junks_frame_label.place(x=180, y = 345)

    empty_sizedbox = Label(rect_frame, text='', bg='#ECF0F5')
    empty_sizedbox.pack(side= 'left', anchor = 'nw', padx = 5)

    listbox_frame = Frame(rect_frame, bg='#ECF0F5', width=55,background='#ECF0F5', relief='solid', border=1, borderwidth=1)
    listbox_frame.pack(side= 'top', anchor = 'nw', pady= 20)

    # Creating a Listbox and
    listbox = Listbox(listbox_frame, background='#ECF0F5',width=50, relief='flat')

    listbox.pack(side = LEFT, fill = BOTH, anchor='nw', ipadx=40, ipady=40)

    scrollbar = Scrollbar(listbox_frame,background='#004AAD')

    scrollbar.pack(side = LEFT, fill = BOTH, anchor='nw')
    

    # for values in range(100):
        # listbox.insert(END, values)

    listbox.config(yscrollcommand = scrollbar.set)
    
    scrollbar.config(command = listbox.yview)


    # finished_scan_frame.pack_forget()

    activationkey_frame = Frame(root, bg='#ECF0F5',)
    # activationkey_frame.pack(expand = True, fill = BOTH, anchor = 'ne')
    # activationkey_frame.pack_forget()

    activation_key_label = Label(activationkey_frame, text='Activation Key', font= ("DM Sans", 13, 'bold'), bg='#ECF0F5', fg='black')
    activation_key_label.pack(side='left', anchor= 'ne', padx=80, pady=100)

    activation_key_var = StringVar()

    activation_key_entry = Entry(activationkey_frame, textvariable=activation_key_var, bd=5, show="*",font= ("DM Sans", 15, ), bg='white', fg='black', relief='flat')
    activation_key_entry.pack(side='left', anchor= 'ne', ipadx = 10, ipady= 5,pady=90)

    update_key_btn_path = PhotoImage(file='assets/update_key.png')
    update_key_btn_path = update_key_btn_path.zoom(5)
    update_key_btn_path = update_key_btn_path.subsample(10)

    def update_key_func():
        pass

    update_key_btn = Button(activationkey_frame, image= update_key_btn_path , command= update_key_func, text='Update Key', compound=CENTER , relief='flat' , font= ("DM Sans", 12, 'bold'), bg='#ECF0F5',activebackground='#ECF0F5', fg='white', activeforeground='white')
    update_key_btn.place(x= 250, y = 180)

    root.mainloop()