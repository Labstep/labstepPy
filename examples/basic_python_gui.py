import labstep
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class NewExperimentForm:
  def __init__(self,root, user):
    self.user = user
    self.frame = Frame(root, width=100, height=50, pady=50,padx=50)
    self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    Logo(self.frame)
    self.name = LabelledInput(self.frame, 'Name')
    self.submit_button = Button(self.frame, text="Create Experiment", command=self.action)
    self.submit_button.pack()

  def action(self):
    name = self.name.get()
    self.user.newExperiment(name)

class Logo:
  def __init__(self,root):
    load = Image.open("labstep_logo.png")
    render = ImageTk.PhotoImage(load)
    logo = Label(root, image=render)
    logo.image = render
    logo.pack()

class LabelledInput:
  def __init__(self,root,name):
    self.label = Label(root, text=name)
    self.label.pack()
    self.input = Entry(root,width=20)
    self.input.pack()

  def get(self):
    return self.input.get()


class LoginForm:
  def __init__(self,root,onSuccess):
    self.onSuccess = onSuccess
    # Define and place the frame for the login form
    self.frame = Frame(root, width=100, height=50, pady=10,padx=10)
    self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    # Place the labstep logo
    Logo(self.frame)
    # Username label and input
    self.username = LabelledInput(self.frame,"Username")
    # Api key label and input
    self.apikey = LabelledInput(self.frame,"API key")
    # Submit button
    submit_button = Button(self.frame, text="Authenticate", command=self.onSubmit)
    submit_button.pack()

  # Function that runs when user hits enter
  def onSubmit(self):
    self.frame.place_forget() # hide login frame
    username = self.username.get() # get user input
    apikey = self.apikey.get() # get user input
    user = labstep.authenticate(username,apikey) # Login via labstep API
    messagebox.showinfo('Login Success', f'You have successfully authenticated as {user.first_name} {user.last_name}')
    self.onSuccess(user)


class App:
  def __init__(self):
    self.window = Tk()
    self.window.title("Labstep Python App")
    self.window.geometry('600x400')
    self.login()

  def main(self,user):
    NewExperimentForm(self.window,user)

  def login(self):
    LoginForm(self.window,self.main)

  def start(self):
    self.window.mainloop()


App().start()