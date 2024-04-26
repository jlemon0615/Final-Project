
"""
Created on Tue Apr 16 21:33:04 2024

@author: Jillian Lemon, Angie, Isabella Sacharczyk

Description: Code takes input from user through the graphical interface and put it into 
a profile-like format for the user to see.

"""

from graphics import *

class Avatar:
    
    def __init__(self):
        self.name = None
        self.hometown = None
        self.age= None
        self.major= None
        self.housing= None
        self.generation= None
    


    def bio(self):
       win= GraphWin ("Avatar Program", 600, 500)
#Make the white rectangle
       r = Rectangle ( Point (550, 450), Point (50,50))
       r.setFill("white")
       r.draw(win)
#Draw text for directions
       txt1= Text(Point (300,100), "Directions: Input the option you choose!")
       txt1.setFill("black")
       txt1.draw(win)
#Draw text for question one
       txt2= Text(Point (120,130), "1. What is your name?") 
       txt2.setFill("black")
       txt2.draw(win)
#User input for question one
       user1= Entry(Point (140,150),20)
       user1.setFill("grey")
       user1.draw(win)
#Draw text for question two
       txt3= Text(Point (133,175), "2. What is your hometown?")
       txt3.setFill("black")
       txt3.draw(win)
#User input for question two
       user2= Entry(Point (140,200),20)
       user2.setFill("grey")
       user2.draw(win)
#Draw text for question three
       txt4= Text(Point (115,225), "3. How old are you?")
       txt4.setFill("black")
       txt4.draw(win)
#User input for question three
       user3=Entry(Point (140,245),20)
       user3.setFill("grey")
       user3.draw(win)
#Draw text for question four
       txt5= Text(Point (120,265), "4. What is your major?")
       txt5.setFill("black")
       txt5.draw(win)
#User input for question four
       user4=Entry(Point (140,285),20)
       user4.setFill("grey")
       user4.draw(win)
#Draw text for question five
       txt6= Text(Point(190, 315), "5. Are you a commuter or do you live on campus? \n Please enter commuter or campus.")
       txt6.setFill("black")
       txt6.draw(win)
#User input for question five
       user5=Entry(Point(140,340),20)
       user5.setFill("grey")
       user5.draw(win)
#Draw text for qustion six
       txt7= Text(Point(155, 370), "6. Are you a first generation student? \n Please enter am or am not.")
       txt7.setFill("black")
       txt7.draw(win)
#User input for question six
       user6= Entry(Point(140,400),20)
       user6.setFill("grey")
       user6.draw(win)
#Button to move to the next page
       btn = Rectangle(Point(425,325), Point(525,425))
       btn.setFill("green")
       btn.draw(win)
       btntxt= Text(Point (475,375), "Press to move on")
       btntxt.setFill("black")
       btntxt.setStyle("bold")
       btntxt.draw(win)
       while win.checkKey() != "q":
           mousePt = win.checkMouse()
           if mousePt is not None:
               if btn.getP1().getX() < mousePt.getX() < btn.getP2().getX():
                   if btn.getP1().getY() < mousePt.getY() < btn.getP2().getY():
                       #Takes variables and assigns them values from input given to the user
                       self.name=user1.getText()
                       self.hometown=user2.getText()
                       self.age=user3.getText()
                       self.major=user4.getText()
                       housing=user5.getText()
                       if housing == ("commuter"):
                           self.housing = ("commuter")
                       else:
                           self.housing=("live on campus")
                       generation=user6.getText()
                       if generation == ("am"):
                           self.generation = ("am")
                       else:
                           self.generation= ("am not")
                       #Make white rectangle to move onto next screen for the bio
                       win= GraphWin ("Avatar Program", 600, 500) 
                       r = Rectangle ( Point (550, 450), Point (50,50))
                       r.setFill("white")
                       r.draw(win)
                       # Draw text that puts users name at the top of the page
                       bolded_name= Text( Point(300,140), self.name)
                       bolded_name.setFill("Black")
                       bolded_name.setStyle("bold")
                       bolded_name.setSize(36)
                       bolded_name.draw(win)
                       #Draw text that uses previous variables to fill in user information
                       text=Text(Point(300,250),"My name is " + self.name + " and my hometown \n is " + self.hometown + ". I " + self.housing + " and " + self.generation + " a \n first generation student. I am " + self.age + " years old and \n my major is "+ self.major + "!")   
                       text.setFill("black")
                       text.draw(win)
                    

def main():
    newA= Avatar()
    newA.bio()
   
    
