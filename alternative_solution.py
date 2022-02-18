'''Engg 200 Group 13 L02
Ethan Bensler, Luiz Felipe, Mizy Bermas, Nimna Wijedasa
The purpose of this program is to create an interactive infographic that compares and contrasts covid data and responses by the 
government in order to come to a conclusion on whose response was the best

Instructions for setup:
- This program uses the module pygame, in order to install pygame, in the terminal type 'pip install pygame'
once a virtual environment has been created.
-  Once the program is running, a window should appear, at this point users can interact with the flag icons in order
to bring up region specific data.
'''
import pygame, sys, os

pygame.init()
size = 1280, 720
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont(None, 110)
pygame.display.set_caption('Alternative Solutions')



class Pics:
    def __init__ (self, size, cords, image, button_cords, button_size):
        self.x_cord = cords[0] #coordinates of the image
        self.y_cord = cords[1]
        self.x_scale = size[0]  #size of the image
        self.y_scale = size[1]
        self.x_button = button_cords[0]  #coordinates of button
        self.y_button = button_cords[1]
        self.image = pygame.transform.scale(image, (self.x_scale, self.y_scale))    #changing the size of image
        self.rect = pygame.Rect((self.x_button, self.y_button), (button_size[0], button_size[1])) # creating button with a rectangle with x_cords, y_cords, x_size, y_size
        

    def zoom(self):
        screen.blit(self.image, (self.x_cord,self.y_cord)) #drawing the new image onscreen over the top of the background
        pygame.display.flip()   #refreshing the screen so the image appears on screen
        while True:
            for ev in pygame.event.get():  #check to see if either the window is  closed or if the user clicks away, which closes the image
                if ev.type == pygame.QUIT:
                    sys.exit(), (45,45)
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    return(pygame.mouse.get_pos())


def main():
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))  #creating a source file directory to reference other files used in the program
    
    background = pygame.transform.scale(pygame.image.load(os.path.join(sourceFileDir,'BACKGROUND.png')).convert(), (1280,720))  #importing the background image and scaling it to the correct size

    alberta = Pics((648, 719),(632, 1),pygame.image.load(os.path.join(sourceFileDir,'ALBERTA.PNG')).convert(), (144, 238), (45,45))  #creating alberta instance. passing coordinate parameters along with the corresponding image

    brazil = Pics((648, 719),(632,1),pygame.image.load(os.path.join(sourceFileDir,'BRAZIL.PNG')).convert(), (306,467), (45,45))  

    canada = Pics((648, 719),(632,1),pygame.image.load(os.path.join(sourceFileDir,'CANADA.PNG')).convert(), (261, 208), (45,45))

    ontario = Pics((648, 719),(632,1),pygame.image.load(os.path.join(sourceFileDir,'ONTARIO.PNG')).convert(), (203, 247), (45,45))

    newzealand = Pics((648, 719),(632,1),pygame.image.load(os.path.join(sourceFileDir,'NEWZEALAND.PNG')).convert(), (433, 575), (45,45))

    united_states = Pics((648, 719),(632,1),pygame.image.load(os.path.join(sourceFileDir,'USA.PNG')).convert(), (165, 302), (45,45))

    zoomed_in = Pics((1280,720),(0,0),pygame.image.load(os.path.join(sourceFileDir,'zoomed_graph.png')).convert(),(700,42),(554,363))

    deaths_per100k = Pics((1280,720),(0,0), pygame.image.load(os.path.join(sourceFileDir,'deathper100k.png')).convert(),(700,450),(1254,700))

    pictures = [alberta, brazil, canada, ontario, newzealand, united_states, zoomed_in, deaths_per100k]  #creating a list of class instances to easily be able to iterate over each



    while True:  #main function while loop
        for ev in pygame.event.get():  #iterate over each different event, button press, mouse movement
            if ev.type == pygame.QUIT:  #quit if the user clicks the  button
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN: #check to see if the mouse button has been clicked
                for picture in pictures:  #iterate over each class instance
                    if picture.rect.collidepoint(pygame.mouse.get_pos()):  #check to see if the user has clicked on an invisible button
                        picture.zoom()  #calls the function which will display the image corresponding to the button the user pressed.
        for picture in pictures: #iterate over each class instance
            pygame.draw.rect(screen,(0,0,0) ,picture.rect)  #draw the buttons
            screen.blit(background, (0,0))  #display the background
            
            pygame.display.flip()#refresh the screen to update all images
            
if __name__ == '__main__':
    
    main()
