#BAD ACE TECHNOLOGIES, PROTOTYPE ONE.

#-------IMPORTS--------
#NOTE: need to figure out a way to merge Rick's virtual environment with mine so we can run his functions.
from tkinter import *
import findScore
import expansion
import os
import string
from tkinter import ttk
#----------------------

#-----------------------------------------------DOCUMENTATION-----------------------------------------------

#This program will allow a user to either login using existing credentials, or alternatively allows them
#to register for a new account, entering in a new username and a new password. Once they have compeleted their
#registration they will be taken back to the login screen, where they can enter in their new credentials
#if they enter in the incorrect information, they will be notified of this mistake and given infinite many chances
#to keep trying to log in. Once they have successfully logged in, they will be taken to the main menu screen, which is
#blank at the moment but will soon include a button to play blackjack using a webcam and a seperate card detection
#software made by rick, this software is in the file 'findScore.py'.

#NOTE: I apologize for the rough workarounds and the confusing abbreviations for some of the functions, I tried
#my best to give descriptive comments to help guide you through my jargon, feel free to change the names though if
#you disagree with them, so long as we turn in a solid product im happy.

# This is just the background color ----> '#010E17', this is the text color ----> '#FFFACC'

#In order for this program to run without throwing an error, you must also have the background image included inside
#the same file where the program is stored, that way we can simply use "background.png" when using it in the code
#if you dont have the background image it will look ugly, and it will also not run, so make sure you have it, it should
#be included with the files I will send you. just remember to put the image in the same file as the actual program

#If you have any questions about anything in the code, or concerns,
#just @Bengiladash in discord and I will be happy to explain the code or listen to ideas.

#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#-------------------------------------------------FUNCTIONS-------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

#This screen will be created when they 'register' button is pressed by the user
#This screen allows the user to create a new account using a new set of credentials, and then it will
#allow the user to return to the login screen to input those new credentials they just created.
def registerScreen():

    #Deleteing the widgets from the login screen so we can replace it with the register screen widgets
    mainCanvas.delete(usernameEntry_window)
    mainCanvas.delete(passwordEntry_window)
    mainCanvas.delete(loginButton_window)
    mainCanvas.delete(registerButton_window)
    mainCanvas.delete(loginText)
    mainCanvas.delete(usernameText)
    mainCanvas.delete(passwordText)

    #setting these widgets to global so we can delete them off the canvas in other functions
    global newUsernameEntry
    global newPasswordEntry
    global registerScreenText
    global newUsernameText
    global newPasswordText
    global frButton
    global frButton_window
    global newUsernameEntry_window
    global newPasswordEntry_window

    #Creating and then placing the text boxes for the register screen onto the canvas
    #NOTE: 'frButton' stands for 'Finish registration Button'
    registerScreenText = mainCanvas.create_text(598.5, 40, text="Register", font=("Helvetica", 50), fill='#FFFACC')
    newUsernameText = mainCanvas.create_text(540, 260, text="New Username", font=("Helvetica", 15), fill='#FFFACC')
    newPasswordText = mainCanvas.create_text(540, 335, text="New Password", font=("Helvetica", 15), fill='#FFFACC')

    #Creating new entry and button widgets for the register screen
    frButton = Button(root, text="Finish Registration", font=("Helvetica", 13), width=15, fg="black", command=registerNewUser)
    newUsernameEntry = Entry(root, font=("Helvetica", 20), width=17, fg='black', bd=0)
    newPasswordEntry = Entry(root, font=("Helvetica", 20), width=17, fg='black', bd=0)

    #Placing the new entry and button widgets for the register screen onto the canvas
    frButton_window = mainCanvas.create_window(530, 400, anchor='nw', window=frButton)
    newUsernameEntry_window = mainCanvas.create_window(475, 275, anchor='nw', window=newUsernameEntry)
    newPasswordEntry_window = mainCanvas.create_window(475, 350, anchor='nw', window=newPasswordEntry)
#----------------------------------------------------------------------------------------------------------

#This function will be executed after the 'finish registration' button is pressed
#It will take a string literal from the newUsername and newPassword entries and write them as a new file
def registerNewUser():

    #setting this widget to global so we can delete them off the canvas in other functions
    global registrationSuccess
    global userCredentials
    global rtlButton
    global rtlButton_window

    #Grabbing the string literals from newUsernameEntry and newPasswordEntry
    newUsernameInfoTemp = newUsernameEntry.get()
    newPasswordInfoTemp = newPasswordEntry.get()

    #This will encode the newly entered username and password before it
    #gets saved locally, the key for this encryption can be found in --MAIN--
    newUsernameInfo = ""
    for letter in newUsernameInfoTemp:
        index = chars.index(letter)
        newUsernameInfo += key[index]

    newPasswordInfo = ""
    for letter in newPasswordInfoTemp:
        index = chars.index(letter)
        newPasswordInfo += key[index]

    #This will open (create) a new file titled after the newUsernameInfo, it will then
    #put the new username on the first line, then the new password on the second line.
    #NOTE: This method is kinda sloppy as it does not contain all credentials in a singular file
    #but rather creates a separate file for each user, but it works, possible upgrade for prototype #2?
    file = open(newUsernameInfo, "w")
    file.write(newUsernameInfo + "\n")
    file.write(newPasswordInfo)
    file.close()

    #Clears the entries newUsernameEntry and newPassowrdEntry
    newUsernameEntry.delete(0, END)
    newPasswordEntry.delete(0, END)

    #This will delete the old register screen widgets so we can then place the 'rtlButton' button, and the
    #'registrationSuccess' text onto the canvas next
    mainCanvas.delete(registerScreenText)
    mainCanvas.delete(frButton_window)
    mainCanvas.delete(newUsernameEntry_window)
    mainCanvas.delete(newPasswordEntry_window)
    mainCanvas.delete(newUsernameText)
    mainCanvas.delete(newPasswordText)

    # Creates the 'rtlButton', or, 'return to login button' which will takes user back to login screen when pressed
    rtlButton = Button(root, text="Return to Login", font=("Helvetica", 13), width=15, fg="black", command=rtlfr)

    # Places the 'rtlButton' onto the canvas, and also places the 'registrationSuccess' text onto the canvas
    rtlButton_window = mainCanvas.create_window(530, 325, anchor='nw', window=rtlButton)
    registrationSuccess = mainCanvas.create_text(598.5, 40, text="Registration Successful!", font=("Helvetica", 50), fill='#FFFACC')
#----------------------------------------------------------------------------------------------------------

# 'rtlfr' stands for 'return to login (screen) from registration (screen).
# We run this function after the user completes registration
# it acts as a method to delete old widgets off the canvas
# which clears up visual space so the next screen's widgets can be placed.
def rtlfr():

    #Deleting old widgets from registration screen
    mainCanvas.delete(rtlButton_window)
    mainCanvas.delete(registrationSuccess)

    #Sends the user to the login screen
    loginScreen()
#----------------------------------------------------------------------------------------------------------

#The first set of widgets (screen) that the user will see
def loginScreen():

    #These global tags will allow the other functions to see these variables, as
    #we will need them to destroy them when we need to open a new window
    #NOTE: I say "open a new window" but in reality, we are simply just deleting
    #old widgets off our canvas and immediately adding new widgets, giving
    #the illusion that we are 'changing windows', this is my current solution
    #to the changing windows problem.
    #most of the functions in this code actually represent a new 'window', or
    #a new set of widgets to be placed.
    global usernameEntry_window
    global passwordEntry_window
    global usernameEntry
    global passwordEntry
    global loginButton_window
    global registerButton_window
    global loginText
    global usernameText
    global passwordText


    #Places 3 text labels onto the canvas, 1 is the big "Login" text at the top
    #The smaller other two, 'Username' and 'Password, will sit on top of the Username and the Password entries
    loginText = mainCanvas.create_text(598.5, 40, text="Login", font=("Helvetica", 50), fill='#FFFACC')
    usernameText = mainCanvas.create_text(520, 260, text="Username", font=("Helvetica", 15), fill='#FFFACC')
    passwordText = mainCanvas.create_text(520, 335, text="Password", font=("Helvetica", 15), fill='#FFFACC')

    #Creates the login button, and also creates the entry boxes for username and password
    #Also creates the register button
    registerButton = Button(root, text="Register", font=("Helvetica", 13), width=12, fg="black", command=registerScreen)
    loginButton = Button(root, text="Login", font=("Helvetica", 13), width=12, fg="black", command=loginVerification)
    usernameEntry = Entry(root, font=("Helvetica", 20), width=17, fg='black', bd=0)
    passwordEntry = Entry(root, font=("Helvetica", 20), width=17, fg='black', bd=0)

    #Places the login button, the username entry box, and the password entry box onto the canvas
    #Also places the Register button
    registerButton_window = mainCanvas.create_window(550, 440, anchor='nw', window=registerButton)
    loginButton_window = mainCanvas.create_window(550, 400, anchor='nw', window=loginButton)
    usernameEntry_window = mainCanvas.create_window(475, 275, anchor='nw', window=usernameEntry)
    passwordEntry_window = mainCanvas.create_window(475, 350, anchor='nw', window=passwordEntry)
#----------------------------------------------------------------------------------------------------------

#This function will help verify that the credentials entered in the login screen are registered credentials
#If they are registered credentials it send the user to the main menu
#If not, it sends them to 'lvtl', which stands for, "login verification to login (screen)" which
#will create an error text that is displayed to the user, and then that function calls the login screen function
#so in essence it just displays an error message and allows the user to try logging in again
def loginVerification():

    #Setting global variables so they can be used in other functions
    global displayName

    #Grabs the entered username and password from the login entries
    usernameTemp = usernameEntry.get()
    passwordTemp = passwordEntry.get()

    #This is stored so we can display their username in the main menu screen
    displayName = usernameTemp

    #This will encode the login information that was just entered, so it
    #can properly be compared against the encrypted data stored locally

    username = ""
    for letter in usernameTemp:
        index = chars.index(letter)
        username += key[index]

    password = ""
    for letter in passwordTemp:
        index = chars.index(letter)
        password += key[index]

    #Clears those entries to allow for subsequent attempts if the user enteres incorrect credentials
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)

    #The 'os.listdir()' simply prints a list of the name of each file in the directory that this program is stored.
    #the idea is that, the way we create credentials is that it creates a new file per user credentials, and this
    #new file for those credentials is stored in the same file as the program
    #The name for any given user credentials file is simply the username of that users' credentials
    #the idea is that we print the list of names of files, we then check if the entered 'username' for logging in
    #is included in this list, if it is, that means there is a file named after their username, and thus they have
    #created an account and their credentials are stored in that file. We then open that file named after the
    #users' username, and check the password line using 'file1.read().splitlines()', if the password is correct aswell
    #then it sends the user to the 'menuScreen()' which means they successfully logged in.
    #If they fail login hoever they are sent to 'lvtl' which stands for 'login verification to login (screen)'.
    list_of_files = os.listdir()

    if username in list_of_files:

        file1 = open(username, "r")
        verify = file1.read().splitlines()

        if password in verify:

            menuScreen()

        else:
            
            lvtl()

    else:

        lvtl()
#----------------------------------------------------------------------------------------------------------

# 'lvtls' or 'login verification (screen) to login (screen) takes us back to the login screen
# if the user enters in incorrect credentials, this functions serves to also add a text that displays
# in red, the fact that they entered in the incorrect credentials.
def lvtl():

    global loginFailed

    mainCanvas.delete(usernameEntry_window)
    mainCanvas.delete(passwordEntry_window)
    mainCanvas.delete(loginButton_window)
    mainCanvas.delete(registerButton_window)
    mainCanvas.delete(loginText)
    mainCanvas.delete(usernameText)
    mainCanvas.delete(passwordText)


    loginFailed = mainCanvas.create_text(598.5, 225, text="Username/Password not found, please try again", font=("Helvetica", 15), fill='red')
    loginScreenFF()
# ----------------------------------------------------------------------------------------------------------

#This function will help us delete the red login failed text, then it will run the login screen
#'dflt' stands for 'delete failed login text'
#Described in more detail in 'loginScreenFF' comments
def dfltLogin():

    mainCanvas.delete(loginFailed)
    loginVerification()
# ----------------------------------------------------------------------------------------------------------

#This function will help us delete the red login failed text, then it will run the registration screen
#'dflt' stands for 'delete failed login text'
#Described in more detail in 'loginScreenFF' comments
def dfltRegister():

    mainCanvas.delete(loginFailed)
    registerScreen()
# ----------------------------------------------------------------------------------------------------------

#This function is simply a copy and paste of the 'loginScreen' function, except we run this version
#when we just failed a login verification, so it stands for 'login screen from failed (verification)'. The
#only difference here is that the two buttons will send us to 'dfltLogin' for the login button, and the register
#button will send us to 'dfltRegister'. The purpose of this is to delete the red text that says we failed the login
#verification, once dfltLogin, or dfltRegister has deleted that 'loginFailed' text, it will then run their function
#NOTE: This is a very bulky work around I know, there most likely is a simpler way to do this, but for now this is
#what we got for prototype one atleast.
def loginScreenFF():

    #This will allow the other functions to see these variables, as we will need them to destroy them when
    #we need to open a new window
    global usernameEntry_window
    global passwordEntry_window
    global usernameEntry
    global passwordEntry
    global loginButton_window
    global registerButton_window
    global loginText
    global usernameText
    global passwordText


    #Places 3 text labels onto the canvas, 1 is the big "Login" text at the top
    #The smaller other two, 'Username' and 'Password, will sit on top of the Username and the Password entries

    loginText = mainCanvas.create_text(598.5, 40, text="Login", font=("Helvetica", 50), fill='#FFFACC')
    usernameText = mainCanvas.create_text(520, 260, text="Username", font=("Helvetica", 15), fill='#FFFACC')
    passwordText = mainCanvas.create_text(520, 335, text="Password", font=("Helvetica", 15), fill='#FFFACC')

    #Creates the login button, and also creates the entry boxes for username and password
    #Also creates the register button
    registerButton = Button(root, text="Register", font=("Helvetica", 13), width=12, fg="black", command=dfltRegister)
    loginButton = Button(root, text="Login", font=("Helvetica", 13), width=12, fg="black", command=dfltLogin)
    usernameEntry = Entry(root, font=("Helvetica", 20), width=17, fg='black', bd=0)
    passwordEntry = Entry(root, font=("Helvetica", 20), width=17, fg='black', bd=0)

    #Places the login button, the username entry box, and the password entry box onto the canvas
    #Also places the Register button
    registerButton_window = mainCanvas.create_window(550, 440, anchor='nw', window=registerButton)
    loginButton_window = mainCanvas.create_window(550, 400, anchor='nw', window=loginButton)
    usernameEntry_window = mainCanvas.create_window(475, 275, anchor='nw', window=usernameEntry)
    passwordEntry_window = mainCanvas.create_window(475, 350, anchor='nw', window=passwordEntry)
# ----------------------------------------------------------------------------------------------------------


#This is the main menu that the user will see once they have succesfully logged in
#This will in the near future include the button that will allow the user to play blackjack using Rick's function
def menuScreen():

    #Setting widgets as global variables so we can delete them in a later screen
    global demoButton
    global demoButton_window
    global antiCheatButton
    global antiCheatButton_window
    global menuText
    global webcamButton
    global webcamButton_window
    global selectFileButton
    global selectFileButton_window

    #Deletes the widgets from login screen
    mainCanvas.delete(usernameEntry_window)
    mainCanvas.delete(passwordEntry_window)
    mainCanvas.delete(loginButton_window)
    mainCanvas.delete(registerButton_window)
    mainCanvas.delete(loginText)
    mainCanvas.delete(usernameText)
    mainCanvas.delete(passwordText)


    #Creates new widgets for the menu screen, 'playBjButton' stands for 'play Black jack Button'
    #Once the user presses this button, it will start running Rick's code to play blackjack using a file.
    #NOTE: at the moment the 'playBlackJackFile' function does not exist so I have removed the command for now
    #just so the program will actually run without throwing an error
    demoButton = Button(root, text="Play Demo", font=("Helvetica", 30), width=16, fg="purple", bg="#FFFACC",
                          command=expansion.people_tracker)
    webcamButton = Button(root, text="Use Webcam", font=("Helvetica", 30), width=16, fg="purple", bg="#FFFACC", command=findscore.app_webcam)
    selectFileButton = Button(root, text="Select Mp4 File", font=("Helvetica", 30), width=16, fg="purple", bg="#FFFACC", command=findscore.select_file)


    #Creates a variable that allows us to display the user specific name on the menu screen
    nameDisplay = "Welcome back " + displayName + "!"

    #Placing the new widgets, including a menuText text onto the canvas for the menu screen window

    webcamButton_window = mainCanvas.create_window(415, 440, anchor='nw', window=webcamButton)
    selectFileButton_window = mainCanvas.create_window(415, 320, anchor='nw', window=selectFileButton)
    demoButton_window = mainCanvas.create_window(415, 200, anchor='nw', window=demoButton)
    menuText = mainCanvas.create_text(598.5, 40, text=nameDisplay, font=("Helvetica", 50), fill='#FFFACC')

#----------------------------------------------------------------------------------------------------------

#This function runs after the user presses the 'playBjButton' on the menuScreen, this function
#will start running the file based version of Rick's Blackjack code.
#NOTE: need to finish working on this
#def playBlackjackFile():



#----------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------
#-------------------------------------------------MAIN-------------------------------------------------
#------------------------------------------------------------------------------------------------------



#Creating the Root window and specifying the visuals
root = Tk()
root.title("Bad Ace Technologies")
root.geometry('1197x716')
root.config(background='#010E17')

global chars
global key


# The following lines of code is in regards to the key that is used to encode the user data before it gets
# saved locally onto their computers, this helps boost security.
chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = ['y', '+', 'Q', '>', '%', 'A', 's', 'B',
       '[', 'h', ',', 'K', '\\', '!', 'f', 'Z',
       'U', 'l', '1', '(', 'I', '`', '5', 'k',
       'J', '^', 'C', 'x', 'p', 'i', '$', 'M',
       '#', 'r', 'H', '*', '@', '0', 'z', ';',
       '3', 'F', '?', 'b', '"', 'P', '&', 'L',
       '|', '4', '8', 'v', 'X', 'V', 'j', 'W',
       '}', 'N', 'c', '2', '6', "'", ')', '~',
       'E', 'T', 'w', 'Y', 't', 'O', 'o', 'd',
       'u', ']', '{', '.', 'e', '<', '9', 'n',
       '-', ' ', '/', 'D', ':', '=', 'G', 'q',
       '7', 'a', '_', 'R', 'S', 'm', 'g']

#Creating a canvas that will serve as a container for all of our widgets, including the background image
#This canvas is what we are going to be adding and deleting widgets on and off of, to help create
#the illusion that we are loading new 'screens' as we go from login screen to registration screen, etc.
global mainCanvas
mainCanvas = Canvas(root, width=1197, height=716, highlightthickness=0, background='#010E17')
mainCanvas.pack(expand=True)

#Defines the background image, this image is included in the folder where this code is stored
global bgImg
bgImg = PhotoImage(file='Background.PNG')

#Places the background image onto the canvas
mainCanvas.create_image(0, 0, image=bgImg, anchor='nw')

#Creates Widgets for the first screen, the login screen
loginScreen()


#This line of code starts the window up, that window being root.
root.mainloop()
