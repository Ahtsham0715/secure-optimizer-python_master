import os
import shutil
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
class CleanedAnimation:
    def __init__(self, root, path):
        self.root = root
        self.path = path
        
        self.dialog = customtkinter.CTkToplevel(self.root, fg_color='#ECF0F5')
        # self.dialog.title('Secure Optimizer')
        # self.dialog.wm_iconbitmap('icon.ico')
        
        self.dialog.geometry("400x200+500+250")
        self.dialog.wm_overrideredirect(True)        
        # self.empty_label = Label(self.dialog,text='', bg = 'white', fg='white')
        # self.empty_label.pack(side = 'top', anchor = 'center', pady= 5)
        
        self.icon_path = ImageTk.PhotoImage(Image.open('assets/management.png').resize((70,70), Image.ADAPTIVE))
        
        self.logo_label = Label(self.dialog,image=self.icon_path, bg = '#ECF0F5')
        self.logo_label.pack(side = 'top', anchor = 'center', pady = 15)

        self.splash_progress_bar = customtkinter.CTkProgressBar(master=self.dialog, fg_color='#ECF0F5', progress_color='green')
        self.splash_progress_bar.set(0.0)
    
        self.splash_progress_bar.pack(side = 'bottom', anchor = 'center', fill = X,) 
    
        self.clearing_label = Label(self.dialog,text = ' Cleaning Files... ', font= ("DM Sans", 15), bg = '#ECF0F5', fg = 'black')
        self.clearing_label.pack(side = 'bottom', anchor = 'center',pady=10)
        
        self.bar()
        
    def bar(self):
        self.file_cleaner()
        if float(self.splash_progress_bar.get()) >= 1.0:
            self.root.after_cancel(self.x)
            self.dialog.destroy()
            self.root.deiconify()
            # self.root.wm_overrideredirect(False)
        else:
            self.x = self.root.after(400,self.bar)
            self.splash_progress_bar.set(float(self.splash_progress_bar.get())+0.1)
        
    #     if os.path.exists('gif_frames'):
    #         shutil.rmtree('gif_frames')
    #     os.mkdir('gif_frames')
    #     self.start = time.time()

    #     self.gif_frames = []
    #     self.images = []
    #     self.animation()

    #     root.mainloop()
    # def animation(self):
    #     gif = Image.open('assets/scanned21.gif')
    #     self.no_of_frames = gif.n_frames

    #     for i in range(self.no_of_frames):
    #         gif.seek(i)
    #         gif.save(os.path.join('gif_frames',f'splash{i}.png'))
    #         self.gif_frames.append(os.path.join('gif_frames',f'splash{i}.png'))

    #     for images in self.gif_frames:
    #         im = Image.open(images)
    #         im = im.resize((690,388),)
    #         im = ImageTk.PhotoImage(im)
    #         self.images.append(im)

    #     self.show_animation(0)

    def file_cleaner(self):
        # image = self.images[count]
        # self.image_label.configure(image=image)
        # count += 1
        # if count == len(self.images)-1:
        #     count = 0

        # to show the gif only for 10 seconds
        # if int(time.time()-self.start) != 8:
        #     self.x = self.root.after(100,self.show_animation,count)
        # else:
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
        # self.root.after_cancel(self.x)
        # self.main_frame.pack_forget()
            # self.root.destroy()
            # self.main_app(self.main_frame)

            # shutil.rmtree('gif_frames')
            
# root = Tk()
# root.geometry("1000x600+220+100")
# root.configure(bg='black')
# CleanedAnimation(root)