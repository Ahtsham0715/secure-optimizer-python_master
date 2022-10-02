from tkinter import *

# from memory_cleaner import memory_cleaner_ui

root = Tk()

screen_height = 600
screen_width = 1000

root.resizable(False, False)
root.geometry('1000x600')
# appbar
appbar = Frame(root, bg='#004AAD', height=70, relief='flat', borderwidth=2)
appbar.pack(expand=True, fill=X, side='top')

logo_path = PhotoImage(file='icon.png')
logo_path = logo_path.zoom(2)
logo_path = logo_path.subsample(32)
logo = Label(appbar, image= logo_path, width= 60 , height= 30, bg='#004AAD')
logo.pack(side= 'left', pady= 10)

app_name_lbl = Label(appbar, text='Secure Optimizer', font= ("DM Sans", 12, 'bold'), fg = 'white', bg = '#004AAD', relief='flat')
app_name_lbl.pack(side= 'left', pady= 10, padx = 15)



contact_lbl = Label(appbar, text='657-541-749', font= ("DM Sans", 12), fg = 'white', bg = '#004AAD', relief='flat')
contact_lbl.pack(side= 'right', pady= 10, padx = 5)

phone_icon_path = PhotoImage(file='phone.png')
phone_icon_path = phone_icon_path.zoom(15)
phone_icon_path = phone_icon_path.subsample(32)
phone_icon = Label(appbar, image= phone_icon_path, width= 40 , height= 40, bg='#004AAD')
phone_icon.pack(side= 'right', pady= 10)


# bottomnavbar
bottomnavbar = Frame(root, bg='#004AAD', height=50, relief='flat', borderwidth=2)
bottomnavbar.pack(expand=True, fill=X, side=BOTTOM)


rights_lbl = Label(bottomnavbar, text='Secure Optimizer @2022', font= ("DM Sans", 11, ), fg = 'white', bg = '#004AAD', relief='flat')
rights_lbl.pack(side= 'left', pady= 10, padx = 15)

pp_btn = Button(bottomnavbar, text='Privacy Policy', font= ("DM Sans", 11, ), fg = 'white', bg = '#004AAD', relief='flat')
pp_btn.pack(side= 'right', pady= 10, padx = 5)


t_and_c_btn = Button(bottomnavbar, text='Terms And Conditions', font= ("DM Sans", 11, ), fg = 'white', bg = '#004AAD', relief='flat')
t_and_c_btn.pack(side= 'right', pady= 10, padx = 5)


# sidebar
sidebar = Frame(root, width=100, bg='#E5E5E5', height=500, relief='flat', borderwidth=2)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

mem_cleaner_btn = Button(sidebar, text='Memory\nCleaner', fg = 'black', bg = '#E5E5E5', relief='flat')
mem_cleaner_btn.pack(side= 'top', pady= 20)

cache_cleaner_btn = Button(sidebar, text='Cache\nCleaner', fg = 'black', bg = '#E5E5E5', relief='flat')
cache_cleaner_btn.pack(side= 'top', pady= 20)

activation_key_btn = Button(sidebar, text='Activation\nKey', fg = 'black', bg = '#E5E5E5', relief='flat')
activation_key_btn.pack(side= 'top', pady= 20)

# main content area
dashboard = Frame(root, bg='#CCC',)
dashboard.pack( expand=True, fill= BOTH)

# memory_cleaner_frame = Frame(root, bg='#CCC')
# memory_cleaner_frame.pack(expand=True, fill=BOTH)


gradient_circle_frame_path = PhotoImage(file='gradient_frame.png')
gradient_circle_frame_path = gradient_circle_frame_path.zoom(15)
gradient_circle_frame_path = gradient_circle_frame_path.subsample(32)

cpu_temp_circle = Label(dashboard, image= gradient_circle_frame_path, text='Scanning 40%', compound= CENTER ,width= 50 , height= 50, bg='#CCC', fg='#7ED957')
cpu_temp_circle.pack(side= 'top', anchor = CENTER)





root.mainloop()