import os
import shutil
import time
from tkinter import *
from PIL import ImageTk, Image

class CleanedAnimation:
    def __init__(self, root, path):
        self.root = root
        self.path = path
        self.main_frame = Frame(self.root, bg='black')
        self.main_frame.pack(expand=True, fill= BOTH, anchor = 'ne')

        self.image_label = Label(self.main_frame,image="", bg = 'black')
        self.image_label.pack(pady=100)
        if os.path.exists('gif_frames'):
            shutil.rmtree('gif_frames')
        os.mkdir('gif_frames')
        self.start = time.time()

        self.gif_frames = []
        self.images = []
        self.animation()

        root.mainloop()
    def animation(self):
        gif = Image.open('assets/scanned.gif')
        self.no_of_frames = gif.n_frames

        for i in range(self.no_of_frames):
            gif.seek(i)
            gif.save(os.path.join('gif_frames',f'splash{i}.png'))
            self.gif_frames.append(os.path.join('gif_frames',f'splash{i}.png'))

        for images in self.gif_frames:
            im = Image.open(images)
            im = im.resize((690,388),)
            im = ImageTk.PhotoImage(im)
            self.images.append(im)

        self.show_animation(0)

    def show_animation(self,count):
        image = self.images[count]
        self.image_label.configure(image=image)
        count += 1
        if count == len(self.images)-1:
            count = 0

        # to show the gif only for 10 seconds
        if int(time.time()-self.start) != 10:
            self.x = self.root.after(80,self.show_animation,count)
        else:
            second_folder = self.path
            for filename in os.listdir(second_folder):
                file_path = os.path.join(second_folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    print('removed')
                except Exception as e:
                    print(e)
            self.root.after_cancel(self.x)
            self.main_frame.pack_forget()
            # self.root.destroy()
            # self.main_app(self.main_frame)

            """
            to delete the gif_frames folder and images inside it so that when we run the program again
            then we don't get the error saying gif_frames folder already exists.
            """
            # shutil.rmtree('gif_frames')
            
# root = Tk()
# root.geometry("1000x600+220+100")
# root.configure(bg='black')
# CleanedAnimation(root)