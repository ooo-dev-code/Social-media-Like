# STILL WORKING ON IT, SOME BUGS ARE STILL PRESENT

from tkinter import *

width = 720
height = 720

frame_height = height/16

class App():
    def __init__(self):
        self.num_press = 0
        self.like = 0
        self.Name = ""
        self.Color = "black"
        
        self.w = Tk()
        self.w.geometry(f"{width}x{height}")
        self.w.title("Social")
        
        self.up_bar = Frame(self.w, background="darkblue", width=width, height=frame_height)
        self.up_bar.pack(anchor="n")
        self.body = Frame(self.w, background="blue", width=width, height=height-frame_height)
        self.body.pack(anchor="n")

        # Create a post-maker
        def Post():
            
            self.like = 0
            
            if part == False:
                create_window = Tk()
                create_window.geometry("100x125")
                create_window.title("Social")
                
                label1 = Label(create_window, text="Name")
                label1.grid()
                self.entry1 = Entry(create_window)
                self.entry1.grid()
                
                label2 = Label(create_window, text="Color")
                label2.grid()
                self.entry2 = Entry(create_window)
                self.entry2.grid()
                
                btn = Button(create_window, text="Submit", command=Create_post)
                btn.place(x=35, y=85)
                
                create_window.mainloop()

        # Render the post in the principal window
        def Create_post():
            self.Name = self.entry1.get()
            self.Color = self.entry2.get()
            
            try:
                canvas = Canvas(self.body, width=width/2, height=height/2, bg=self.Color)
                canvas.place(x=170, y=10)
            except Exception as e:
                canvas = Canvas(self.body, width=width/2, height=height/2, bg="black")
                canvas.place(x=170, y=10)
                
            title = Label(self.body, text=f"{str(self.Name)}", background="white", font=40)
            title.place(x=170, y=height/2+25)
            self.num_press +=1
            
            if self.num_press > 1:
                title.destroy()
                canvas.destroy()
                
                try:
                    canvas = Canvas(self.body, width=width/2, height=height/2, bg=self.Color)
                    canvas.place(x=170, y=10)
                except Exception as e:
                    canvas = Canvas(self.body, width=width/2, height=height/2, bg="black")
                    canvas.place(x=170, y=10)
                    
                title = Label(self.body, text=f"{str(self.Name)}", background="white", font=40)
                title.place(x=170, y=height/2+25)

        # Put like, Still bug sometimes
        def Like():
            self.like += 1
            num_like = Label(self.body, text=self.like)
            num_like.place(x=80)
        
        self.btn_post = Button(self.up_bar, text="Create post", command=Post)
        self.btn_post.place(x=10, y=10)
        
        like = Button(self.body, text="Like", command=Like)
        like.place(x=100)
        
        
        self.w.mainloop()

if __name__ == "__main__":
    App()
