# import tkinter as tk
from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
import os
import shutil
import time
from tkinter import messagebox
import matplotlib
import psutil
import firebase_admin
from firebase_admin import credentials, firestore
import scanned_animation
from threading import Thread
import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import datetime
import threading
import getpass
import socket

cred = credentials.Certificate(r"cleaner-app-50143-firebase-adminsdk-cej46-ef12406467.json")
firebase_admin.initialize_app(cred)


class Screen:
    def __init__(self):
        Thread(target = self.check_registration).start()
        # self.fetch_phone()
        self.activation_key = ''
        self.isActivated = False
        self.root = Tk()
        self.root.geometry("600x300+350+250")
        self.root.configure(bg='#ECF0F5')
        # self.root.eval('tk::PlaceWindow . top')

        # to remove the title bar
        self.root.wm_overrideredirect(True)

        self.main_frame = Frame(self.root, bg='white')
        self.main_frame.pack(fill="both",expand=True) 
        
        self.icon_path = ImageTk.PhotoImage(Image.open('assets/logo.png').resize((400,200), Image.ADAPTIVE))
              
        self.empty_label = Label(self.main_frame,text='', bg = 'white', fg='white')
        self.empty_label.pack(side = 'top', anchor = 'center', pady= 5)
        
        self.logo_label = Label(self.main_frame,image=self.icon_path, bg = 'white')
        self.logo_label.pack(side = 'top', anchor = 'center',)
        
        self.splash_progress_bar = customtkinter.CTkProgressBar(master=self.main_frame, fg_color='#e6e6e6', )
        self.splash_progress_bar.set(0.0)
    
        self.splash_progress_bar.pack(side = 'bottom', anchor = 'center', fill = X,) 
        
        self.initializing_label = Label(self.main_frame,text = ' Initializing... ', font= ("DM Sans", 15), bg = 'white', fg = 'black')
        self.initializing_label.pack(side = 'bottom', anchor = 'center',pady=5)

        self.bar()
                
        self.logo_path = ImageTk.PhotoImage(Image.open('assets/icon.png').resize((140,70), Image.ANTIALIAS))
        self.phone_icon_path = ImageTk.PhotoImage(Image.open('assets/phone.png').resize((30,30), Image.ANTIALIAS))
        self.caution_icon_path = PhotoImage(file='assets/caution.png')
        self.caution_icon_path = self.caution_icon_path.zoom(15)
        self.caution_icon_path = self.caution_icon_path.subsample(32)
        self.scan_btn_path = ImageTk.PhotoImage(Image.open('assets/Group 24.png').resize((150,150), Image.ANTIALIAS))
        self.gradient_circle_path = ImageTk.PhotoImage(Image.open('assets/Group 20.png').resize((55,55), Image.ANTIALIAS))
        self.gradient_circle_frame_path = PhotoImage(file='assets/gradient_frame.png')
        self.gradient_circle_frame_path = self.gradient_circle_frame_path.zoom(15)
        self.gradient_circle_frame_path = self.gradient_circle_frame_path.subsample(32)
        self.check_icon_path = ImageTk.PhotoImage(Image.open('assets/checked.png').resize((180,180), Image.ANTIALIAS))
        self.update_key_btn_path = ImageTk.PhotoImage(Image.open('assets/update_key.png').resize((140,45), Image.ANTIALIAS))
        self.folder_icon = ImageTk.PhotoImage(Image.open('assets/folder.png').resize((30,30), Image.ANTIALIAS))
        self.folder1_icon = ImageTk.PhotoImage(Image.open('assets/folder1.png').resize((30,30), Image.ANTIALIAS))
        self.pc_icon = ImageTk.PhotoImage(Image.open('assets/pc.png').resize((100,100), Image.ANTIALIAS))
        self.windows_pc_icon = ImageTk.PhotoImage(Image.open('assets/pc1.png').resize((30,30), Image.ANTIALIAS))
        self.antivirus_icon = ImageTk.PhotoImage(Image.open('assets/antivirus.png').resize((50,50), Image.ANTIALIAS))
        self.application_icon = ImageTk.PhotoImage(Image.open('assets/application.png').resize((30,30), Image.ANTIALIAS))
        self.broom_icon = ImageTk.PhotoImage(Image.open('assets/broom.png').resize((50,50), Image.ANTIALIAS))
        self.browser_icon = ImageTk.PhotoImage(Image.open('assets/browser.png').resize((30,30), Image.ANTIALIAS))
        self.clean_code_icon = ImageTk.PhotoImage(Image.open('assets/clean-code.png').resize((50,50), Image.ANTIALIAS))
        self.compact_disk_icon = ImageTk.PhotoImage(Image.open('assets/compact-disk.png').resize((50,50), Image.ANTIALIAS))
        self.code_icon = ImageTk.PhotoImage(Image.open('assets/code.png').resize((50,50), Image.ANTIALIAS))
        self.contract_icon = ImageTk.PhotoImage(Image.open('assets/contract.png').resize((50,50), Image.ANTIALIAS))
        self.folder_search_icon = ImageTk.PhotoImage(Image.open('assets/folder_search.png').resize((50,50), Image.ANTIALIAS))
        self.harddisk_icon = ImageTk.PhotoImage(Image.open('assets/harddisk.png').resize((50,50), Image.ANTIALIAS))
        self.key_icon = ImageTk.PhotoImage(Image.open('assets/key.png').resize((50,50), Image.ANTIALIAS))
        self.management_icon = ImageTk.PhotoImage(Image.open('assets/management.png').resize((30,30), Image.ANTIALIAS))
        self.message_icon = ImageTk.PhotoImage(Image.open('assets/message.png').resize((50,50), Image.ANTIALIAS))
        self.open_folder_icon = ImageTk.PhotoImage(Image.open('assets/open-folder.png').resize((50,50), Image.ANTIALIAS))
        self.photo_icon = ImageTk.PhotoImage(Image.open('assets/photo.png').resize((40,40), Image.ANTIALIAS))
        self.recycle_bin_icon = ImageTk.PhotoImage(Image.open('assets/recycle-bin.png').resize((50,50), Image.ANTIALIAS))
        self.recycle_bin1_icon = ImageTk.PhotoImage(Image.open('assets/recycle-bin1.png').resize((50,50), Image.ANTIALIAS))
        self.sound_waves_icon = ImageTk.PhotoImage(Image.open('assets/sound-waves.png').resize((50,50), Image.ANTIALIAS))
        self.usb_icon = ImageTk.PhotoImage(Image.open('assets/usb.png').resize((30,30), Image.ANTIALIAS))
        self.video_icon = ImageTk.PhotoImage(Image.open('assets/video.png').resize((30,30), Image.ANTIALIAS))
        self.video_camera_icon = ImageTk.PhotoImage(Image.open('assets/video-camera.png').resize((30,30), Image.ANTIALIAS))
        self.frame_icon = ImageTk.PhotoImage(Image.open('assets/frame.png').resize((30,30), Image.ANTIALIAS))
        self.floppy_disk_icon = ImageTk.PhotoImage(Image.open('assets/floppy-disk.png').resize((30,30), Image.ANTIALIAS))
        self.playlist_icon = ImageTk.PhotoImage(Image.open('assets/playlist.png').resize((30,30), Image.ANTIALIAS))
        
        
        self.activationkey_frame = Frame(self.root, bg='#ECF0F5',)
        self.finished_scan_frame = Frame(self.root, bg='#ECF0F5',)
        self.memory_cleaner_frame = Frame(self.root, bg='#ECF0F5')
        

        self.root.mainloop()
    

    def check_registration(self):
        os.remove('temp.txt')
        if not os.path.exists('temp.txt'):
            with open('temp.txt', 'w') as f:
                f.write('')
        try:
            db = firestore.client()
            query_ref = db.collection(u'allowed_users').where(u'machine_id', u'==', socket.gethostname()).stream()


            for doc in query_ref:
                data= doc.to_dict()
                print('in loop')
                print(getpass.getuser())
                print(socket.gethostname())
                if str(data['machine_id']) == socket.gethostname():
                    print(data['activation_key'])
                    self.activation_key = str(data['activation_key'])
                    with open('temp.txt', 'w') as f:
                        f.write('True')
                    self.isActivated = True
                    print(self.isActivated)
                else:
                    with open('temp.txt', 'w') as f:
                            f.write('False')
                    self.isActivated = False
                    self.isActivated = ''
                
                
        except Exception as e:
            with open('temp.txt', 'w') as f:
                f.write('False')
            # messagebox.showerror('Error', 'Wrong Activation Key\nTry Again!!!')
            print(e)     


    def bar(self):
        # isactive = ''
        # with open('temp.txt', 'r') as f:
        #     isactive = f.read()
        if float(self.splash_progress_bar.get()) >= 1.0:
            self.root.after_cancel(self.x)
            self.main_app(self.main_frame)
            self.root.wm_overrideredirect(False)
        else:
            self.x = self.root.after(300,self.bar)
            self.splash_progress_bar.set(float(self.splash_progress_bar.get())+0.1)
    
    
    
    def changeOnHover(self,button, bgcolorOnHover, fgcolorOnHover, bgcolorOnLeave, fgcolorOnLeave):

        button.bind("<Enter>", func=lambda e: button.config(
        background=bgcolorOnHover))
  
        button.bind("<Enter>", func=lambda e: button.config(
        foreground=fgcolorOnHover))
  
    # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
        background=bgcolorOnLeave))
    
        button.bind("<Leave>", func=lambda e: button.config(
        foreground=fgcolorOnLeave))
    
    def main_app(self, f):
        with open('temp.txt', 'r') as file:
            if file.read() == 'True':
                self.isActivated = True
            else:
                self.isActivated = False
                
        def fetch_phone():
            try:
                db = firestore.client()
                self.doc_ref = db.collection(u'users').document(u'data').get()
                self.doc_data = self.doc_ref.to_dict()
                self.contact_lbl['text'] = self.doc_data['phone']
                print(self.doc_data['phone'])
                        
            except Exception as e:
                print(e)
                self.contact_lbl['text'] = self.doc_data['phone']
        
        Thread(target = fetch_phone).start()

        
       
        
        screen_height = 700
        screen_width = 1000
        
        f.pack_forget()
        self.root.wm_iconbitmap('icon.ico')
        self.root.title('Secure Optimizer')
        self.root.wm_overrideredirect(False)
        self.root.geometry("1000x650+220+50")
        
        # appbar
        appbar = Frame(self.root, bg='#004AAD', height=70, relief='flat')
        appbar.pack(fill=X, side='top', anchor='ne')


        logo = Label(appbar, image= self.logo_path, width= 60 , height= 30, bg='#004AAD')
        logo.pack(side= 'left', pady= 10)

        app_name_lbl = Label(appbar, text='Secure Optimizer', font= ("DM Sans", 12, 'bold'), fg = 'white', bg = '#004AAD', relief='flat')
        app_name_lbl.pack(side= 'left', pady= 10, padx = 15)

        self.contact_lbl = Label(appbar, text='loading...', font= ("DM Sans", 12), fg = 'white', bg = '#004AAD', relief='flat')
        self.contact_lbl.pack(side= 'right', pady= 10, padx = 5)

        phone_icon = Label(appbar, image= self.phone_icon_path, width= 40 , height= 40, bg='#004AAD')
        phone_icon.pack(side= 'right', pady= 10)



        # bottomnavbar
        bottomnavbar = Frame(self.root, bg='#004AAD', height=50, relief='flat', borderwidth=2)
        bottomnavbar.pack(fill=X, side=BOTTOM, anchor = 'sw')

        rights_lbl = Label(bottomnavbar, text='Secure Optimizer @2022', font= ("DM Sans", 11, ), fg = 'white', bg = '#004AAD', relief='flat')
        rights_lbl.pack(side= 'left', pady= 10, padx = 15)

        pp_btn = Button(bottomnavbar, text='Privacy Policy', font= ("DM Sans", 11, ), fg = 'white', bg = '#004AAD', relief='flat')
        pp_btn.pack(side= 'right', pady= 10, padx = 5)


        t_and_c_btn = Button(bottomnavbar, text='Terms And Conditions', font= ("DM Sans", 11, ), fg = 'white', bg = '#004AAD', relief='flat')
        t_and_c_btn.pack(side= 'right', pady= 10, padx = 5)

        # sidebar
        sidebar = Frame(self.root, bg='#ECF0F5', relief='solid', borderwidth=1,border=0, bd= 1)
        sidebar.pack( fill=Y, side=LEFT, anchor='nw')

        def activation_key_func():
            app_name_lbl['text'] = 'Secure Optimizer'
            self.dashboard.pack_forget()
            self.dashboard_frame.pack_forget()
            self.memory_cleaner_frame.pack_forget()
            self.finished_scan_frame.pack_forget()
            self.cleaner_diagnosis.pack_forget()
            self.activationkey_frame.pack(expand = True, fill = BOTH, anchor = 'ne')

        def dashboard_btn_thread():
            self.activationkey_frame.pack_forget()
            self.cleaner_diagnosis.pack_forget()
            self.dashboard.pack_forget()
            self.finished_scan_frame.pack_forget()
            self.dashboard_frame.pack( expand=True, fill= BOTH, anchor = 'ne')

        def dashboard_btn_func():
            if self.isActivated:
                self.thread = Thread(target = dashboard_btn_thread)
                self.thread.start()
            else:
                activation_key_func()
            

        dashboard_btn = Button(sidebar, text='Dashboard', fg = 'black', command= dashboard_btn_func, font= ("DM Sans", 11, 'bold'), bg = '#ECF0F5', relief='flat')
        dashboard_btn.pack(side= 'top', pady= 2)

        def mem_cleaner_func():
            if self.isActivated:
                app_name_lbl['text'] = 'Secure Optimizer'
                self.activationkey_frame.pack_forget()
                self.dashboard_frame.pack_forget()
                self.cleaner_diagnosis.pack_forget()
                self.dashboard.pack( expand=True, fill= BOTH, anchor = 'ne')
                self.memory_cleaner_frame.pack_forget()
                self.finished_scan_frame.pack_forget()
            else:
                self.activationkey_frame.pack(expand = True, fill = BOTH, anchor = 'ne')
        
        def scan_btn_thread():
            app_name_lbl['text'] = 'Scan your PC'
            self.activationkey_frame.pack_forget()
            self.dashboard_frame.pack_forget()
            self.cleaner_diagnosis.pack_forget()
            self.dashboard.pack_forget()
            self.finished_scan_frame.pack_forget()
            # self.cleaner_diagnosis.pack_forget()
            self.memory_cleaner_frame.pack(expand = True, fill = BOTH, anchor = 'ne')
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
            self.memory_cleaner_frame.pack_forget()
            self.finished_scan_frame.pack(expand = True, fill = BOTH, anchor = 'ne')
            
            
        def scan_btn_func():
            if self.isActivated:
                self.thread = Thread(target = scan_btn_thread)
                self.thread.start()
            else:
                activation_key_func()
            
            # self.thread.join()
            

        mem_cleaner_btn = Button(sidebar, text='Memory Cleaner', fg = 'black', font= ("DM Sans", 11, 'bold'), bg = '#ECF0F5', relief='flat', command= mem_cleaner_func)
        mem_cleaner_btn.pack(side= 'top', pady= 20)


        cache_cleaner_btn = Button(sidebar, text='Cache Cleaner', fg = 'black', font= ("DM Sans", 11, 'bold'), bg = '#ECF0F5', relief='flat', command= scan_btn_func)
        cache_cleaner_btn.pack(side= 'top', pady= 20)



        quick_clean_btn = Button(sidebar, text='Quick Clean', fg = 'black', font= ("DM Sans", 11, 'bold'), bg = '#ECF0F5', relief='flat', command= scan_btn_func)
        quick_clean_btn.pack(side= 'top', pady= 20)


        deep_clean_btn = Button(sidebar, text='Deep Clean', fg = 'black', font= ("DM Sans", 11, 'bold'), bg = '#ECF0F5', relief='flat', command= scan_btn_func)
        deep_clean_btn.pack(side= 'top', pady= 20)

        activation_key_btn = Button(sidebar, text='Activation Key', fg = 'black', font= ("DM Sans", 11, 'bold'), bg = '#ECF0F5', relief='flat', command= activation_key_func)
        activation_key_btn.pack(side= 'top', pady= 20)

          # main content area
        self.dashboard_frame = Frame(self.root, bg='#ECF0F5')
        if self.isActivated:
            self.dashboard_frame.pack( expand=True, fill= BOTH, anchor = 'ne')
        else:
            self.activationkey_frame.pack(expand = True, fill = BOTH, anchor = 'ne')

        dashboard_bottom_bar = Frame(self.dashboard_frame, bg='#004AAD', height=30, relief='solid', borderwidth=1,border=0,bd=1)
        dashboard_bottom_bar.pack(fill=X, side=BOTTOM, anchor = 'sw', expand= True)


        total_memory = Label(dashboard_bottom_bar, text= 'Total Memory:', font= ("DM Sans", 11, 'bold'), fg = '#e1e0e0', bg = '#004AAD', relief='flat')
        total_memory.pack(side= 'left', pady= 5, anchor ='center')

        tot_mem = int(psutil.virtual_memory().total)/2**30
        

        total_memory_stat = Label(dashboard_bottom_bar, text= f'{str(round(tot_mem,1)).split(".")[0]} GB', font= ("DM Sans", 11, 'bold'), fg = 'white', bg = '#004AAD', relief='flat')
        total_memory_stat.pack(side= 'left', pady= 5, anchor ='center')        

        empty_sizedbox1 = Label(dashboard_bottom_bar, text='', bg='#004AAD')
        empty_sizedbox1.pack(side= 'left', anchor = CENTER, padx = 100)

        free_memory = Label(dashboard_bottom_bar, text= 'Memory Free:', font= ("DM Sans", 11, 'bold'), fg = '#e1e0e0', bg = '#004AAD', relief='flat')
        free_memory.pack(side= 'left', pady= 5, anchor ='center',)

        free_mem = int(psutil.virtual_memory().free)/2**30

        free_memory_stat = Label(dashboard_bottom_bar, text= f'{round(free_mem,1)} GB', font= ("DM Sans", 11, 'bold'), fg = 'white', bg = '#004AAD', relief='flat')
        free_memory_stat.pack(side= 'left', pady= 5, padx= 5 , anchor ='center')


        cpu_use_stat = Label(dashboard_bottom_bar, text= f'{int(psutil.cpu_percent())}%', font= ("DM Sans", 11, 'bold'), fg = 'white', bg = '#004AAD', relief='flat')
        cpu_use_stat.pack(side= 'right', pady= 5, padx= 5 , anchor ='center')

        cpu_use = Label(dashboard_bottom_bar, text= 'CPU Usage:', font= ("DM Sans", 11, 'bold'), fg = '#e1e0e0', bg = '#004AAD', relief='flat')
        cpu_use.pack(side= 'right', pady= 5, anchor ='center',)


        dashboard_top_bar1 = Frame(self.dashboard_frame, bg='#004AAD', height=50, relief='solid', borderwidth=1,border=0, bd= 1)
        dashboard_top_bar1.pack(fill=X, side='top', anchor='ne')        

        pc_icon = Label(dashboard_top_bar1, image= self.windows_pc_icon, width= 30 , height= 30, bg='#004AAD')
        pc_icon.pack(side= 'left', pady= 10)

        pc_status_lbl = Label(dashboard_top_bar1, text='PC Status Check', font= ("DM Sans", 12, 'bold'), fg = 'white', bg = '#004AAD', relief='flat')
        pc_status_lbl.pack(side= 'left', pady= 10, padx = 15)
       
        latest_issues_no = Label(dashboard_top_bar1, text='14021', font= ("DM Sans", 11, 'bold'), fg = 'white', bg = '#004AAD', relief='flat')
        latest_issues_no.pack(side= 'right', pady= 10, padx = 5)
       
        latest_issues = Label(dashboard_top_bar1, text='Latest Issues Found:', font= ("DM Sans", 11, 'bold'), fg = '#e1e0e0', bg = '#004AAD', relief='flat')
        latest_issues.pack(side= 'right', pady= 10,)
       
       
        dashboard_top_bar2 = Frame(self.dashboard_frame, bg='#004AAD', height=40,  relief='solid', borderwidth=1,border=0, bd= 1)
        dashboard_top_bar2.pack(fill=X, side='top', anchor='ne')        

        last_scan_lbl = Label(dashboard_top_bar2, text='Last Scan: ', font= ("DM Sans", 11, 'bold'), fg = '#e1e0e0', bg = '#004AAD', relief='flat')
        last_scan_lbl.pack(side= 'left', pady= 5, anchor='center', padx = 8)
        
        if not os.path.exists('last_scan.txt'):
            with open('last_scan.txt', 'w') as f:
                f.write('')
        
        last_scan_time_lbl = Label(dashboard_top_bar2, text='10.10.2022. 21:02:12', font= ("DM Sans", 11, 'bold'), fg = 'white', bg = '#004AAD', relief='flat')
        last_scan_time_lbl.pack(side= 'left', pady= 5, anchor='center')
        
        with open('last_scan.txt', 'r') as f:
            last_scan_time_lbl['text'] = f'{f.read()}'
        
        smart_menu_lbl = Label(self.dashboard_frame, text='Secure Optimizer Menu', font= ("DM Sans", 12, 'bold'), fg = 'black', bg = '#ECF0F5', relief='flat')
        smart_menu_lbl.pack(side= 'top', pady= 10, anchor='center')
        
        
        self.clean_frame = Frame(self.dashboard_frame, bg='#ECF0F5')
        self.clean_frame.pack(side = 'top', expand=True, anchor = 'center')

        def mem_btn_thread():
            if self.isActivated:
                self.activationkey_frame.pack_forget()
                self.dashboard.pack_forget()
                self.dashboard_frame.pack_forget()
                self.finished_scan_frame.pack_forget()
                self.cleaner_diagnosis.pack(side= 'top', expand=True, fill= BOTH, anchor = 'ne')
                # self.dashboard_frame.pack( expand=True, fill= BOTH, anchor = 'ne')
            else:
                activation_key_func()


        def mem_btn_func():
            self.thread = Thread(target = mem_btn_thread)
            self.thread.start()


        self.memory_cleaner_button = Button(master=self.clean_frame, image=self.antivirus_icon, font= ("DM Sans", 10, 'bold','underline') , text="\nMemory Cleaner",
                                                compound="top", relief='flat', bg='#ECF0F5', fg='black', command= mem_btn_func , cursor= 'hand2',)
        self.memory_cleaner_button.pack(side = 'left', anchor = 'center', padx = 30, pady= 2, ipady = 5)
         
       
        self.cache_cleaner_button = Button(master=self.clean_frame, image=self.clean_code_icon, font= ("DM Sans", 10, 'bold','underline') , text="\nCache Cleaner",
                                                compound="top", relief='flat', bg='#ECF0F5', fg='black', command= scan_btn_func, cursor= 'hand2',)
        self.cache_cleaner_button.pack(side = 'left', anchor = 'center', padx = 30, pady= 2, ipady = 5)
         
       
        self.deep_clean_button = Button(master=self.clean_frame, image=self.code_icon, font= ("DM Sans", 10, 'bold','underline') , text="\nDeep Clean",
                                                compound="top", relief='flat', bg='#ECF0F5', fg='black', command= scan_btn_func,  cursor= 'hand2',)
        self.deep_clean_button.pack(side = 'left', anchor = 'center', padx = 30, pady= 2, ipady = 5)

        self.active_key_frame = Frame(self.dashboard_frame, bg='#ECF0F5')
        self.active_key_frame.pack(side = 'top', expand=True, anchor = 'center', pady = 2)
       
        self.quick_clean_button = Button(master=self.active_key_frame, image=self.harddisk_icon, font= ("DM Sans", 10, 'bold','underline') , text="\nQuick Clean",
                                                compound="top", relief='flat', bg='#ECF0F5', fg='black', command= scan_btn_func , cursor= 'hand2',)
        self.quick_clean_button.pack(side = 'left', anchor = 'center', padx = 30, pady= 2, ipady = 5)
         
       
        self.activation_key_button = Button(master=self.active_key_frame, image=self.key_icon, font= ("DM Sans", 10, 'bold','underline') , text="\nActivation Key",
                                                compound="top", relief='flat', bg='#ECF0F5', fg='black', command=activation_key_func , cursor= 'hand2',)
        self.activation_key_button.pack(side = 'left', anchor = 'center', padx = 30, pady= 2, ipady = 5)
         


       
        self.health_status = Frame(self.dashboard_frame, bg='#ECF0F5', relief = 'flat')

        self.last_scan_var = ''

        with open('last_scan.txt', 'r') as lsfile:
            self.last_scan_var = str(lsfile.read())
        
        d1 = int(str(self.last_scan_var).split(' ')[0].split('-')[2])
        d2 = int(str(datetime.now()).split(' ')[0].split('-')[2])
        # print(d1)
        # print(d2)
        # print(d2-d1)
        
        if d2 - d1 >= 5:
            self.health_status.pack(side = 'top', expand=True, anchor = 'ne', pady = 5)
        
        self.health_status_frame = Frame(self.health_status, bg='#e3e3e3', relief= 'solid', borderwidth=1, border=0, bd=1)
        self.health_status_frame.pack(side = 'top', expand=True, anchor = 'nw')

        self.health_status_caution_icon = Label(self.health_status_frame, image= self.caution_icon_path, width= 40 , height= 40, bg='#e3e3e3')
        self.health_status_caution_icon.pack(side= 'left',padx = 15)

        self.health_status_lbl = Label(self.health_status_frame, text='System Health Status:', font= ("DM Sans", 14, 'bold'), fg = 'black', bg = '#e3e3e3', relief='flat')
        self.health_status_lbl.pack(side= 'left', anchor = CENTER)
        
        self.critical_lbl = Label(self.health_status_frame, text='Critical', font= ("DM Sans", 14, 'bold'), fg = 'red', bg = '#e3e3e3', relief='flat')
        self.critical_lbl.pack(side= 'left', anchor = CENTER, padx = 5)

        self.smart_pc_lbl = Label(self.health_status, text='Secure Optimizer Health', font= ("DM Sans", 12, 'bold'), fg = 'black', bg = '#ECF0F5', relief='flat')
        self.smart_pc_lbl.pack(side= 'right', pady= 0, anchor = 'nw', padx = 5)



        # cleaner diagnosis
        self.cleaner_diagnosis = Frame(self.root, bg='#ECF0F5',)
        # self.cleaner_diagnosis.pack(side= 'top', expand=True, fill= BOTH, anchor = 'ne')
       
        self.cleaner_top_frame = Frame(self.cleaner_diagnosis, bg='#004AAD', height=50, relief='solid', borderwidth=1,border=0, bd= 1)
        self.cleaner_top_frame.pack(fill=X, side='top', anchor='ne')        
       
       
        self.pc_lbl_cd = Label(self.cleaner_top_frame, image= self.windows_pc_icon, compound= 'left', font= ("DM Sans", 12, 'bold') ,text= '    Press Start Scan' , bg='#004AAD', fg='white')
        self.pc_lbl_cd.pack(side= 'left', anchor = 'nw', ipadx = 10)
      
        self.smart_pc_cleaner_lbl = Label(self.cleaner_diagnosis, text='Secure Optimizer Diagnosis', font= ("DM Sans", 12, 'bold'), fg = 'black', bg = '#ECF0F5', relief='flat')
        self.smart_pc_cleaner_lbl.pack(side= 'top', anchor='center', pady= 5) 
       
        self.cleaner_diagnosis_frame = Frame(self.cleaner_diagnosis, bg='#e3e3e3', relief='solid', borderwidth=1,border=0, bd= 1)
        self.cleaner_diagnosis_frame.pack(fill=X, side='top', anchor='center', padx = 20,ipady = 10, expand= True)  
       
        self.cleaner_diagnosis_left_frame = Frame(self.cleaner_diagnosis_frame, bg='#e3e3e3', relief='flat')
        self.cleaner_diagnosis_left_frame.pack(side='left', anchor='w' , padx = 20,)  
       
        self.file_icons = [self.folder1_icon, self.frame_icon, self.video_camera_icon, self.playlist_icon, self.floppy_disk_icon, self.recycle_bin1_icon]
       
        self.file_names = [' Files ', ' Pictures ', ' Videos ', ' Audios ', ' Drives ',' Junk ']
        self.files_count = 0
        
        for i in range(2):
            for j in range(3):
                self.cleaner_files = Label(self.cleaner_diagnosis_left_frame, image= self.file_icons[self.files_count], compound= 'left', font= ("DM Sans", 12, ) ,text= self.file_names[self.files_count] , height= 40, bg='#e3e3e3', fg='black')
                self.cleaner_files.grid(row= i+2, column = j+1, padx = 15, pady = 30)
                self.files_count += 1
       
       
        self.cleaner_diagnosis_right_frame = Frame(self.cleaner_diagnosis_frame, bg='#e3e3e3', relief='flat',)
        self.cleaner_diagnosis_right_frame.pack(side='right', anchor='ne', expand = True, fill= Y,)  
       
        self.smart_pccleaner_lbl = Label(self.cleaner_diagnosis_right_frame, font= ("DM Sans", 11, 'bold') ,text= 'Memory Usage Chart' , bg='#e3e3e3', fg='black')
        self.smart_pccleaner_lbl.pack(side='top', anchor = 'center', padx= 5)
       
        matplotlib.rcParams["font.family"] = "DM Sans"
        mermory_chart_label = ['Used' , 'Free']
        memory_chart_value = [int(psutil.disk_usage('/').used),int(psutil.disk_usage('/').free)]
        memory_chart_colors = ['red', 'green']
        fig = Figure(facecolor='#e3e3e3',) # create a figure object
        fig.set_size_inches(2,2)
        ax = fig.add_subplot(111, ) # add an Axes to the figure

        ax.pie(memory_chart_value, radius=1, labels=mermory_chart_label, colors=memory_chart_colors ,autopct='%0.2f%%', shadow=False,)

        chart1 = FigureCanvasTkAgg(fig,self.cleaner_diagnosis_right_frame, )
        chart1.get_tk_widget().pack(side= 'top', anchor='ne', padx= 5)
    
       
        self.percentage_lbl = Label(self.cleaner_diagnosis_right_frame, font= ("DM Sans", 13, 'bold') ,text= '0 %' , bg='#e3e3e3', fg='black')
        self.percentage_lbl.pack(side='bottom', anchor = 'e',padx=1,)
       
        self.scan_status_frame = Frame(self.cleaner_diagnosis, bg='#ECF0F5', relief='flat')
        self.scan_status_frame.pack(side='top', anchor='ne', fill=X, pady= 2 ,padx= 20)  
       
        self.scan_status_lbl = Label(self.scan_status_frame, font= ("DM Sans", 12, 'bold') ,text= 'Scan Status: Waiting...' , bg='#ECF0F5', fg='black')
        self.scan_status_lbl.pack(side='left', anchor = 'sw',)
       
        self.elapsed_time_lbl = Label(self.scan_status_frame, font= ("DM Sans", 12, 'bold') ,text= 'Elapsed Time' , bg='#ECF0F5', fg='black')
        self.elapsed_time_lbl.pack(side='right', anchor = 'sw',padx=5,)
       
       
        self.elapsed_time_lbl = Label(self.cleaner_diagnosis, font= ("DM Sans", 12, 'bold') ,text= '00:00:00' , bg='#ECF0F5', fg='black')
        self.elapsed_time_lbl.pack(side='top', anchor = 'ne',padx=25,pady= 2)
        
        self.progress_bar = customtkinter.CTkProgressBar(master=self.cleaner_diagnosis, fg_color='#e3e3e3')
        self.progress_bar.set(0.0)
    
        self.progress_bar.pack(side = 'top', anchor = 'center', fill = X, padx = 20, pady= 5)       

        def scanner():
            folder = 'C:\Windows\Prefetch'
            folder2 = 'C:\Windows\Temp'
            directory_list1 = os.listdir(folder)
            directory_list2 = os.listdir(folder2)
            directory_list = directory_list1 + directory_list2
            self.scan_status_lbl['font'] = ("DM Sans", 11, )
            t = threading.currentThread()
            while getattr(t, "do_run", True):
                for file in directory_list:
                    time.sleep(0.05)
                    self.scan_status_lbl['text'] = str(file)
                else:
                    break
            # if 
            scanner()

        def getThreadByName(name):
            threads = threading.enumerate() #Threads list
            for thread in threads:
                if thread.name == name:
                    return thread
    
        def mybar():
            self.start_scan_btn.configure(state= DISABLED)
            
            # self.scan_status_lbl['text'] = 'Scan Status: In Progress...'
            # self.start_scan_btn.configure(fg_color= 'grey')
            import time, random
            self.progress = 0.1
            rand_time = random.randint(15,40)
            rem_time = rand_time
            filethread = Thread(target = scanner, name='1123' ,daemon=True,)
            filethread.start()
            
            self.elapsed_time_lbl['text'] = f'00:00:{rem_time}'
            for i in range(0,rand_time,1):
                self.progress_bar.set(self.progress)
                if rem_time > 5:
                    rem_time = rem_time - random.randint(1,3)
                else:
                    rem_time = rem_time - 0
                if self.progress >= 1.0:                    
                    self.elapsed_time_lbl['text'] = f'00:00:00'
                    self.percentage_lbl['text'] = '100 %'
                    t = getThreadByName('1123')
                    t.do_run = False
                    t.join()
                    time.sleep(0.3)
                    messagebox.showinfo('Success', 'Scan Completed Successfully')
                    break
                else:
                    if self.progress >= 8.0:
                        if rem_time > 9:
                            rem_time = 7
                    self.elapsed_time_lbl['text'] = f'00:00:{rem_time}'
                    percentage = (float(self.progress_bar.get())/1.0) *100
                    self.percentage_lbl['text'] = f'{int(percentage)} %'
                self.root.update_idletasks()
                time.sleep(i)
                self.progress += random.uniform(0.05,0.1)
            scan_btn_thread()
            # scanned_animation.CleanedAnimation(self.root, path='C:\Windows\Prefetch')
            
    

            self.progress_bar.set(1.0)
            self.start_scan_btn.configure(state= NORMAL)
            self.scan_status_lbl['font'] = ("DM Sans", 12, 'bold')
            self.scan_status_lbl['text'] = 'Scan Status: Waiting...'
            
            self.percentage_lbl['text'] = '0 %'
            self.elapsed_time_lbl['text'] = f'00:00:00'
            with open('last_scan.txt', 'w') as f:
                f.write(f'{datetime.now()}')
            self.last_scanlbl['text'] = f'Last Scan: {datetime.now()}'
            # self.start_scan_btn['fg_color'] = '#004AAD'

    
        def bar_thread():
            self.thread = Thread(target = mybar)
            self.thread.start()
    
    
        self.last_scanlbl = Label(self.cleaner_diagnosis, compound= 'left' ,text= f'Last Scan: 01.01.2022', font= ("DM Sans", 11, 'bold'), fg = 'white', bg = '#004AAD', relief='solid', borderwidth=1, border=1, bd=1)
        self.last_scanlbl.pack(side= 'bottom', anchor ='sw', fill = X)
        
        with open('last_scan.txt', 'r') as f:
            self.last_scanlbl['text'] = f'Last Scan: {f.read()}'
    
        self.start_scan_btn = customtkinter.CTkButton(master= self.cleaner_diagnosis, command= bar_thread ,corner_radius=25, text='Start Scan', height= 40,  text_color='white', fg_color= '#004AAD', hover=False, text_font=("DM Sans", 11, ))
        self.start_scan_btn.pack(side = 'bottom', anchor = 'center', pady=5)
       

       
        # memory cleaner
        self.dashboard = Frame(self.root, bg='#ECF0F5',)
        # self.dashboard.pack( expand=True, fill= BOTH, anchor = 'ne')

        caution_frame = Frame(self.dashboard, bg='#ECF0F5',)
        caution_frame.pack(side='top', anchor='center' , expand=True)
        
        caution_icon = Label(caution_frame, image= self.caution_icon_path, width= 40 , height= 40, bg='#ECF0F5')
        caution_icon.pack(side= 'left', pady= 1)

        optimizing_lbl = Label(caution_frame, text='Optimising items frees up storage space on your device. ', font= ("DM Sans", 11, ), fg = 'black', bg = '#ECF0F5', relief='flat')
        optimizing_lbl.pack(side= 'left', pady= 1, anchor = CENTER)

        t_and_c_btn = Button(caution_frame, text='Scan Now!', cursor='hand2', command= scan_btn_func, activebackground='#ECF0F5' ,font= ("DM Sans", 11, ), bg = '#ECF0F5', fg = '#004AAD', relief='flat')
        t_and_c_btn.pack(side= LEFT, pady= 1, anchor = CENTER)

        scan_btn = Button(self.dashboard, image= self.scan_btn_path,cursor= 'hand2', activebackground='#ECF0F5',command= scan_btn_func , width= screen_height *0.25 , height= screen_height *0.25 , bg='#ECF0F5', relief='flat')
        scan_btn.pack(side = TOP, padx = 20, pady = 10, anchor = CENTER)

        # self.changeOnHover(t_and_c_btn, bgcolorOnHover='white', bgcolorOnLeave='#ECF0F5')

        stats_frame = Frame(self.dashboard, bg='#ECF0F5',)
        stats_frame.pack(side='top', anchor=CENTER, expand=True)


        empty_sizedbox = Label(stats_frame, text='', bg='#ECF0F5')
        empty_sizedbox.pack(side= 'left', anchor = CENTER, padx = 1)

        memory_frame = Frame(stats_frame, bg='#ECF0F5',)
        memory_frame.pack(fill=X, side='left', anchor=CENTER, padx = 12)


        memory_usage_var = int(psutil.virtual_memory().percent)

        mem_usage_circle = Label(memory_frame, image= self.gradient_circle_path, text=f'{memory_usage_var}%', compound= CENTER ,width= 50 , height= 50, bg='#ECF0F5')
        mem_usage_circle.pack(side= 'top', anchor = CENTER)

        cpu_temp_circle = Label(memory_frame, text='Memory\nUsage', bg='#ECF0F5')
        cpu_temp_circle.pack(side= 'top', anchor = CENTER)

        cpu_frame = Frame(stats_frame, bg='#ECF0F5',)
        cpu_frame.pack(fill=X, side='left', anchor=CENTER, padx = 12)

        cpu_temp_var = int(psutil.cpu_percent())


        cpu_temp_circle = Label(cpu_frame, image= self.gradient_circle_path, text=f'{cpu_temp_var}%', compound= CENTER ,width= 50 , height= 50, bg='#ECF0F5')
        cpu_temp_circle.pack(side= 'top', anchor = CENTER)

        cpu_temp_circle = Label(cpu_frame, text='CPU\nUsage', bg='#ECF0F5')
        cpu_temp_circle.pack(side= 'top', anchor = CENTER)


        storage_frame = Frame(stats_frame, bg='#ECF0F5',)
        storage_frame.pack(fill=X, side='left', anchor=CENTER, padx = 12)

        storage_usage_var = int(psutil.disk_usage('/').percent)

        storage_usage_circle = Label(storage_frame, image= self.gradient_circle_path, text=f'{storage_usage_var}%', compound= CENTER ,width= 50 , height= 50, bg='#ECF0F5')
        storage_usage_circle.pack(side= 'top', anchor = CENTER)

        storage_usage_circle = Label(storage_frame, text='Storage\nUsage', bg='#ECF0F5')
        storage_usage_circle.pack(side= 'top', anchor = CENTER)


        space_clear = Label(self.dashboard, text='1.2 GB space can be cleared', font= ("DM Sans", 12, ), bg='#ECF0F5')
        space_clear.pack(side= 'top', anchor = CENTER, pady = 20)

        thisfolder = 'C:\Windows\Prefetch' 
        sizegb=0
        for ele in os.scandir(thisfolder):
            sizegb+=os.stat(ele).st_size
        size_in_gb = round(sizegb/2**30,3)
        print(size_in_gb)

        space_clear['text'] = f'{size_in_gb} GB space can be cleared'

        empty_sizedbox = Label(self.memory_cleaner_frame, text='', bg='#ECF0F5')
        empty_sizedbox.pack(side= 'top', anchor = CENTER, pady = 30)

        cpu_temp_circle = Label(self.memory_cleaner_frame , font= ("DM Sans", 12,), text='Scanning... ', compound= CENTER ,width= 150 , height= 150, bg='#ECF0F5', fg='#7ED957')
        cpu_temp_circle.pack(anchor = CENTER, side= TOP, pady= 30)
        
        scanning_doc = Label(self.memory_cleaner_frame, text='Scanning Documents .....', font= ("DM Sans", 12, ), bg='#ECF0F5')
        scanning_doc.pack(side= 'top', anchor = CENTER)


        check_icon = Label(self.finished_scan_frame, image= self.check_icon_path ,width= 230 , height= 230, bg='#ECF0F5')
        check_icon.pack(anchor = 'nw', side= TOP, padx= 70, pady= 20)

        total_data_frame = Frame(self.finished_scan_frame, bg='#ECF0F5',)
        total_data_frame.place(x=screen_width * 0.5, y=screen_height * 0.05)

        scan_finished_label = Label(total_data_frame, text='Scan Finished', font= ("DM Sans", 14, 'bold'), bg='#ECF0F5')
        scan_finished_label.pack(side= 'top', anchor = 'ne', pady = 30, padx= 40)

        total_junks_label = Label(total_data_frame, text='Total Junks: 863 items', font= ("DM Sans", 12, ), bg='#ECF0F5')
        total_junks_label.pack(side= 'top', anchor = 'nw')

        total_junks_size_label = Label(total_data_frame, text='Total Junks Size: 9574 MB', font= ("DM Sans", 12, ), bg='#ECF0F5')
        total_junks_size_label.pack(side= 'top', anchor = 'nw', pady=10)

        def clean_now_thread():
            # self.finished_scan_frame.pack_forget()
            # self.activationkey_frame.pack_forget()
            # self.memory_cleaner_frame.pack_forget()
            self.root.withdraw()
            self.dashboard_frame.pack( expand=True, fill= BOTH, anchor = 'ne')
            self.dashboard.pack_forget()
            self.cleaner_diagnosis.pack_forget()
            self.activationkey_frame.pack_forget()
            self.finished_scan_frame.pack_forget()
            self.memory_cleaner_frame.pack_forget()
            scanned_animation.CleanedAnimation(self.root, path='C:\Windows\Prefetch')

        def clean_now_func():
            self.thread = Thread(target = clean_now_thread)
            self.thread.start()

        clean_now_btn = Button(total_data_frame, text='Clean Now', command= clean_now_func, relief='flat' , font= ("DM Sans", 13, ), bg='#004AAD', fg='white')
        clean_now_btn.pack(side= 'top', anchor = 'nw', pady=20, ipadx=120, ipady=5)


        rect_frame = Frame(self.finished_scan_frame, bg='#ECF0F5', width=100,background='#ECF0F5', relief='solid', border=1, borderwidth=1)
        rect_frame.pack(side= 'top', anchor = 'center', fill=X, padx = 50,pady = 15)

        empty_sizedbox = Label(rect_frame, text='', bg='#ECF0F5')
        empty_sizedbox.pack(side= 'left', anchor = 'nw', padx = 5)

        listbox_frame = Frame(rect_frame, bg='#ECF0F5', width=55,background='#ECF0F5', relief='solid', border=1, borderwidth=1)
        listbox_frame.pack(side= 'top', anchor = 'nw', pady= 20)

        # Creating a Listbox and
        listbox = Listbox(listbox_frame, background='#ECF0F5',width=50, relief='flat')

        listbox.pack(side = LEFT, fill = BOTH, anchor='nw', ipadx=40, ipady=40)

        scrollbar = Scrollbar(listbox_frame,background='#004AAD')

        scrollbar.pack(side = LEFT, fill = BOTH, anchor='nw')
    

        listbox.config(yscrollcommand = scrollbar.set)
        
        scrollbar.config(command = listbox.yview)

        activation_key_label = Label(self.activationkey_frame, text='Activation Key', font= ("DM Sans", 13, 'bold'), bg='#ECF0F5', fg='black')
        activation_key_label.pack(side='left', anchor= 'ne', padx=80, pady=100)

        activation_key_var = StringVar()

        activation_key_entry = Entry(self.activationkey_frame, textvariable=activation_key_var, bd=5, show="*",font= ("DM Sans", 15, ), bg='white', fg='black', relief='flat')
        activation_key_entry.pack(side='left', anchor= 'ne', ipadx = 10, ipady= 5,pady=90)

        def update_key_thread():
            update_key_btn['text'] = 'Processing'
            update_key_btn['state'] = DISABLED
            update_key_btn['image'] = ''
            
            
            try:
                db = firestore.client()
                # doc_ref = db.collection(u'activationKeys').stream()
                doc_ref = db.collection(u'allowed_users').document()
                doc_ref.set({
                    u'user_id': str(getpass.getuser()),
                    u'machine_id': str(socket.gethostname()),
                    u'activation_key': str(activation_key_var.get()),
                }, merge=True)
                
                messagebox.showinfo('success', 'You registered successfully.\nRestart Application to get access')
                update_key_btn['text'] = 'Update Key'
                update_key_btn['state'] = NORMAL
                update_key_btn['image'] = self.update_key_btn_path
                
            except Exception as e:
                messagebox.showerror('Error', 'Wrong Activation Key\nTry Again!!!')
                update_key_btn['text'] = 'Update Key'
                update_key_btn['state'] = NORMAL
                update_key_btn['image'] = self.update_key_btn_path
            
            
        def update_key_func():
            self.thread = Thread(target = update_key_thread)
            self.thread.start()

        update_key_btn = Button(self.activationkey_frame, image= self.update_key_btn_path , command= update_key_func, text='Update Key', compound=CENTER , relief='flat' , font= ("DM Sans", 12, 'bold'), bg='#ECF0F5',activebackground='#ECF0F5', fg='white', activeforeground='white')
        update_key_btn.place(x= 250, y = 180)

Screen()

# pyinstaller --noconfirm --onedir --windowed --add-data "C:/Users/Umer/AppData/Local/Programs/Python/Python37/Lib/site-packages/customtkinter;customtkinter/"  home_page.py
# pyinstaller --noconsole --icon=icon.ico --windowed --add-data "C:/Users/Umer/AppData/Local/Programs/Python/Python37/Lib/site-packages/customtkinter;customtkinter/"  Secure-Optimizer.py

