#Python Exercise: Create a class "Ball" with attributes and methods

class Ball:
    color= 'yellow'
    circumference= '65'
    material= ''
    
    def changeColor(self, color):
        self.color= color      
    
    def showColor(self):    
        print ('The color of the ball is: ', self.color)

b= Ball()
b.changeColor('pink')
b.showColor()
