

# from logging import exception
# from firebase_admin import firestore
# from firebase_admin import credentials
# import firebase_admin

# cred = credentials.Certificate(r"cleaner-app-50143-firebase-adminsdk-cej46-ef12406467.json")
# firebase_admin.initialize_app(cred)
# def write_data(data):
    
#     db = firestore.client()
#     try:
#         db.collection('users').document('data').set({
#             'typed_data' : data,
#         }, merge= True)
#         print('data saved...')
#     except exception as e:
#         print(f'error occured. {e}')

# # write_data('hello shami.')

# def verify_registration():
#     db = firestore.client()
#     doc_ref = db.collection(u'activationKeys').stream()
#     for data in doc_ref:
#         doc_data = data.to_dict()
#         print(doc_data['key'])
#     # doc = doc_ref.get()
#     # if doc.exists:
#     #     doc = doc.to_dict()
#     #     print(doc)
#     # else:
#     #     print(u'No such document!')

# verify_registration()

# # import getpass
# # userID = getpass.getuser()
# # import socket
# # machineID = socket.gethostname()
# # print(userID)
# # print(machineID)

# # from tkinter import *
# # import random

# # root = Tk()
# # root.title('Register')
# # # root.iconbitmap('c:/gui/codemy.ico')
# # root.geometry("500x500")

# # # Generate Key
# # def generate():
# # 	# Clear key label
# # 	key_label.delete(0, END)
# # 	verify_label.config(text="")

# # 	# Set some defaults
# # 	key = ''
# # 	section = ''
# # 	check_digit_count = 0
# # 	alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'

# # 	# key = aaaa-bbbb-cccc-dddd-1111 or 24 characters

# # 	while len(key) < 25:
# # 		# Randomly pick digit from alphabet
# # 		char = random.choice(alphabet)
# # 		# Add random choice to key
# # 		key += char
# # 		# Also add the random choice to the section blob
# # 		section += char

# # 		# Add in the dashes/hyphens
# # 		if len(section) == 4:
# # 			# add in a hyphen
# # 			key += '-'
# # 			# Reset the section to nothing
# # 			section = ''
# # 	# set key to all but the last digit
# # 	key = key[:-1]

# # 	# output the key
# # 	key_label.insert(0, key)

# # # Create a button
# # generate_button = Button(root, text="Generate Key!", font=("Helvetica", 32), command=generate)
# # generate_button.pack(pady=50)

# # # Key Label
# # key_label = Entry(root, font=("Helvetica", 24), bd=0, bg="systembuttonface", width=25)
# # key_label.pack(pady=10, padx=50)

# # # Verify Label
# # verify_label = Label(root, text="Waiting...", font=("Helvetica", 32))
# # verify_label.pack(pady=10)

# # # Score Label
# # score_label = Label(root, text="Score: ", font=("Helvetica", 32))
# # score_label.pack(pady=10)

# # root.mainloop()

import tkinter as tk
from PIL import ImageTk
from PIL import Image

class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

        self.update = self.draw().__next__
        master.after(100, self.update)

    def draw(self):
        image = Image.open(self.filename)
        angle = 0
        while True:
            tkimage = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = self.canvas.create_image(
                250, 250, image=tkimage)
            self.master.after_idle(self.update)
            yield
            self.canvas.delete(canvas_obj)
            angle += 10
            angle %= 360

root = tk.Tk()
app = SimpleApp(root, 'assets/gradient_frame.png')
root.mainloop()
# import time
# import tkinter
# from tkinter import *
# import cv2
# import numpy as np
# from PIL import ImageTk, Image
# global rotater
# rotater=True
# def rotate_img(img_path, rt_degr):
#     img = Image.open(img_path)
#     return img.rotate(rt_degr, expand=1)

# def draw():
#     global rotater, image # use global "image"

#     if rotater:
#         img_rt_90 = rotate_img("assets/gradient_frame.png", 90)
#         img_rt_90.save("assets/gradient_frame.png")
#         image = ImageTk.PhotoImage(img_rt_90) # update image with rotated one
#         label.config(image=image)
#         rotater = False
#     else:
#         img_rt_90 = rotate_img("assets/gradient_frame.png", 90)
#         img_rt_90.save("assets/gradient_frame.png")
#         image = ImageTk.PhotoImage(img_rt_90) # update image with rotated one
#         label.config(image=image)
#         rotater = True
        
# def rotate():
#     while True:
#         time.sleep(0.2)
#         draw()
# root = Tk()
# image = cv2.imread("assets/gradient_frame.png")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# image = Image.fromarray(image)
# image = ImageTk.PhotoImage(image)
# label = Label(image=image)
# label.pack()
# but12=Button(root,text="deneme",command=rotate)
# but12.pack()
# root.mainloop()