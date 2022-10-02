from tkinter import *

root = Tk()

screen_height = 700
screen_width = 1000

# root.resizable(False, False)
root.geometry('1000x600')
# appbar
appbar = Frame(root, bg='#004AAD', height=70, relief='flat', borderwidth=2)
appbar.pack(fill=X, side='top', anchor='ne')

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
bottomnavbar.pack(fill=X, side=BOTTOM, anchor = 'sw')

rights_lbl = Label(bottomnavbar, text='Secure Optimizer @2022', font= ("DM Sans", 11, ), fg = 'white', bg = '#004AAD', relief='flat')
rights_lbl.pack(side= 'left', pady= 10, padx = 15)

pp_btn = Button(bottomnavbar, text='Privacy Policy', font= ("DM Sans", 11, ), fg = 'white', bg = '#004AAD', relief='flat')
pp_btn.pack(side= 'right', pady= 10, padx = 5)


t_and_c_btn = Button(bottomnavbar, text='Terms And Conditions', font= ("DM Sans", 11, ), fg = 'white', bg = '#004AAD', relief='flat')
t_and_c_btn.pack(side= 'right', pady= 10, padx = 5)

# sidebar
sidebar = Frame(root, bg='#E5E5E5', relief='flat', borderwidth=4, bd= 1)
sidebar.pack( fill=Y, side=LEFT, anchor='nw')

mem_cleaner_btn = Button(sidebar, text='Memory\nCleaner', fg = 'black', bg = '#E5E5E5', relief='flat')
mem_cleaner_btn.pack(side= 'top', pady= 20)

cache_cleaner_btn = Button(sidebar, text='Cache\nCleaner', fg = 'black', bg = '#E5E5E5', relief='flat')
cache_cleaner_btn.pack(side= 'top', pady= 20)

activation_key_btn = Button(sidebar, text='Activation\nKey', fg = 'black', bg = '#E5E5E5', relief='flat')
activation_key_btn.pack(side= 'top', pady= 20)

# main content area
dashboard = Frame(root, bg='#CCC',)
dashboard.pack( expand=True, fill= BOTH, anchor = 'ne')

caution_frame = Frame(dashboard, bg='#CCC',)
caution_frame.pack(fill=X, side='top', anchor=CENTER, expand=True, padx = screen_width * 0.2)

caution_icon_path = PhotoImage(file='caution.png')
caution_icon_path = caution_icon_path.zoom(15)
caution_icon_path = caution_icon_path.subsample(32)
caution_icon = Label(caution_frame, image= caution_icon_path, width= 50 , height= 50, bg='#CCC')
caution_icon.pack(side= 'left', pady= 5)

optimizing_lbl = Label(caution_frame, text='Optimising items frees up storage space on your device. ', font= ("DM Sans", 11, ), fg = 'black', bg = '#CCC', relief='flat')
optimizing_lbl.pack(side= 'left', pady= 5)

t_and_c_btn = Button(caution_frame, text='Scan Now!', activebackground='#CCC' ,font= ("DM Sans", 11, ), bg = '#CCC', fg = '#004AAD', relief='flat')
t_and_c_btn.pack(side= 'left', pady= 5)


scan_btn_path = PhotoImage(file='Group 24.png')
scan_btn_path = scan_btn_path.zoom(15)
scan_btn_path = scan_btn_path.subsample(32)
scan_btn = Button(dashboard, image= scan_btn_path, activebackground='#CCC' , width= screen_height *0.25 , height= screen_height *0.25 , bg='#CCC', relief='flat')
scan_btn.pack(side = TOP, padx = 20, pady = 10, anchor = CENTER)


stats_frame = Frame(dashboard, bg='#CCC',)
stats_frame.pack(fill=X, side='top', anchor=CENTER, expand=True)


gradient_circle_path = PhotoImage(file='Group 20.png')
gradient_circle_path = gradient_circle_path.zoom(20)
gradient_circle_path = gradient_circle_path.subsample(32)

empty_sizedbox = Label(stats_frame, text='', bg='#CCC')
empty_sizedbox.pack(side= 'left', anchor = CENTER, padx = 165)

memory_frame = Frame(stats_frame, bg='#CCC',)
memory_frame.pack(fill=X, side='left', anchor=CENTER, padx = 12)

mem_usage_circle = Label(memory_frame, image= gradient_circle_path, text='70%', compound= CENTER ,width= 50 , height= 50, bg='#CCC')
mem_usage_circle.pack(side= 'top', anchor = CENTER)

cpu_temp_circle = Label(memory_frame, text='Memory\nUsage', bg='#CCC')
cpu_temp_circle.pack(side= 'top', anchor = CENTER)

cpu_frame = Frame(stats_frame, bg='#CCC',)
cpu_frame.pack(fill=X, side='left', anchor=CENTER, padx = 12)

cpu_temp_circle = Label(cpu_frame, image= gradient_circle_path, text='50°', compound= CENTER ,width= 50 , height= 50, bg='#CCC')
cpu_temp_circle.pack(side= 'top', anchor = CENTER)

cpu_temp_circle = Label(cpu_frame, text='CPU\nTemprature', bg='#CCC')
cpu_temp_circle.pack(side= 'top', anchor = CENTER)


storage_frame = Frame(stats_frame, bg='#CCC',)
storage_frame.pack(fill=X, side='left', anchor=CENTER, padx = 12)

storage_usage_circle = Label(storage_frame, image= gradient_circle_path, text='82%', compound= CENTER ,width= 50 , height= 50, bg='#CCC')
storage_usage_circle.pack(side= 'top', anchor = CENTER)

storage_usage_circle = Label(storage_frame, text='Storage\nUsage', bg='#CCC')
storage_usage_circle.pack(side= 'top', anchor = CENTER)


space_clear = Label(dashboard, text='1.2 GB space can be cleared', font= ("DM Sans", 12, ), bg='#CCC')
space_clear.pack(side= 'top', anchor = CENTER, pady = 20)




# cachecleaner = Frame(root, bg='#CCC', width=500, height=500)
# cachecleaner.pack(expand=True, fill='both', side='right')
# activationkey = Frame(root, bg='#CCC', width=500, height=500)
# activationkey.pack(expand=True, fill='both', side='right')
# activationkey.pack_forget()
# cachecleaner.pack_forget()
dashboard.pack_forget()
memory_cleaner_frame = Frame(root, bg='#ECF0F5')
memory_cleaner_frame.pack(expand = True, fill = BOTH, anchor = 'ne')

# memory_cleaner_ui(memory_cleaner_frame)

# scanning_frame = Frame(memory_cleaner_frame, bg='#CCC')
# scanning_frame.pack(expand=True, fill=BOTH)

gradient_circle_frame_path = PhotoImage(file='gradient_frame.png')
gradient_circle_frame_path = gradient_circle_frame_path.zoom(15)
gradient_circle_frame_path = gradient_circle_frame_path.subsample(32)

empty_sizedbox = Label(memory_cleaner_frame, text='', bg='#ECF0F5')
empty_sizedbox.pack(side= 'top', anchor = CENTER, pady = 30)

cpu_temp_circle = Label(memory_cleaner_frame, image= gradient_circle_frame_path,font= ("DM Sans", 12,), text='Scanning... 40%', compound= CENTER ,width= 150 , height= 150, bg='#ECF0F5', fg='#7ED957')
cpu_temp_circle.pack(anchor = CENTER, side= TOP, pady= 30)

scanning_doc = Label(memory_cleaner_frame, text='Scanning Documents .....25MB', font= ("DM Sans", 12, ), bg='#ECF0F5')
scanning_doc.pack(side= 'top', anchor = CENTER)




root.mainloop()