import array
import pygame # pygame library for game development
import sys
import random # to generate random numbers
from word_list import WORDS # access to word_list file that contains list of different 5 letter words

pygame.init() # initialize pygame

# Restart Button
window = (600, 700) # size of window
screen = pygame.display.set_mode(window) #screen to be used with button functionality

color = (255, 255, 255) #Font color of button
color_static = (170, 170, 170) #color of button when not hovering over (light grey)
color_dynamic = (150, 150, 150) #color of button when hovered (dark grey)

font = pygame.font.Font(None, 24) #font of button

button_width = 150 #Dimensions and relative position of the button
button_height = 50
button_x = (window[0] - button_width) / 2
button_y = window[1] - button_height - 20

button_surface = pygame.Surface((button_width, button_height)) #Creates button surface
button_surface.fill(color_static) #Makes the interior of the button light grey

text = font.render('Restart', True, color) #Creates text for the button
text_rect = text.get_rect(center=(button_width / 2, button_height / 2))
text_rect.center = (button_x + button_width / 2, button_y + button_height / 2) #Places text in the center of the button

boundaries = pygame.Rect(button_x, button_y, button_width, button_height) #Creates the clickable boundaries of the button

#DEFINING CONSTANTS

WIDTH, HEIGHT = 600, 700 # dimensions of the display

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # define screen with desired dimensions
BACKGROUND = pygame.image.load("design/Starting Tiles.png") # define background, load image with background tiles found online
BACKGROUND_RECTANGLE = BACKGROUND.get_rect(center=(317, 300)) # define background rectangle and center it
ICON = pygame.image.load("design/Icon.png") # define icon with character square image found online

pygame.display.set_caption("Wordle") # set header of pygame to wordle
pygame.display.set_icon(ICON) # set icon of pygame to icon image

# set colors with custom color tags

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

# set correct word

CORRECT_WORD = random.choice(WORDS)

print("Correct word:", CORRECT_WORD)

LETTER_FONT = pygame.font.Font("design/BrontidevpDemoStyle2-ZV8E3.otf", 50) # define a letter font variable with font file

# setup display screen and display the background in the boundaries of "background rectangle"

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECTANGLE)
pygame.display.update()

# define variables for spacing and size

LETTER_HORIZONTAL_SPACING = 85
LETTER_VERTICAL_SPACING = 12
LETTER_SIZE = 75

# define variables for guess count, 2D list to contain all guesses, a list for current guess, string for this guess, current letter spacing, letters in word
a1 = 0
b1 = 0
c1 = 0
d1 = 0
e1 = 0
f1 = 0
g1 = 0
h1 = 0
i1 = 0
j1 = 0
k1 = 0
l1 = 0
m1 = 0
n1 = 0
o1 = 0
p1 = 0
q1 = 0
r1 = 0
s1 = 0
t1 = 0
u1 = 0
v1 = 0
w1 = 0
x1 = 0
y1 = 0
z1 = 0
list = ([a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1,o1,p1,q1,r1,s1,t1,u1,v1,w1,x1,y1,z1])
list2 = (['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
guesses_count = 0
guesses = [[]] * 6
current_guess = []
current_guess_string = ""
current_letter_background_horizontal = 110
game_result = "" # string to represent the result of the game 

# define a letter class for each individual "letter" block

class Letter:
    
    # function to initialize the letter with color, position, spacing
    
    def __init__(self, text, background_position):
        self.background_color = "white"
        self.text_color = "black"
        self.background_position = background_position
        self.background_position_horizontal = background_position[0]
        self.background_position_vertical = background_position[1]
        self.background_rectangle = (background_position[0], self.background_position_vertical, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.background_position_horizontal+36, self.background_position[1]+34)
        self.text_render = LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rectangle = self.text_render.get_rect(center=self.text_position)
        
    # function to draw(show) the letter on screen

    def draw(self):
        pygame.draw.rect(SCREEN, self.background_color, self.background_rectangle)
        if self.background_color == "white":
            pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.background_rectangle, 3)
        self.text_render = LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_render, self.text_rectangle)
        pygame.display.update()
        
    # function to delete(remove) the letter on screen

    def delete(self):
        pygame.draw.rect(SCREEN, "white", self.background_rectangle)
        pygame.draw.rect(SCREEN, OUTLINE, self.background_rectangle, 3)
        pygame.display.update()

# function to check the current guess

def check_guess(guess_to_check):
    global current_guess, current_guess_string, guesses_count, current_letter_background_horizontal, game_re
    check_letter = False

    for spot in range(5):
        lowercase_letter = current_guess[spot].text.lower() # first letter in current guess
        if lowercase_letter == CORRECT_WORD[spot]:
            for letters in range(26):
                if(lowercase_letter == list2[letters]):
                    if(list[letters] > 0):
                        list[letters] -= 1

    game_over = False
    for spot in range(5):
        lowercase_letter = guess_to_check[spot].text.lower() # first letter in current guess
        if lowercase_letter in CORRECT_WORD: # if letter is in correct word
            if lowercase_letter == CORRECT_WORD[spot]: # if letter is equal to letter at this position in the correct word
                guess_to_check[spot].background_color = GREEN # letter is correct, make green
                if not game_over:
                    game_result = "W"
            else:
                for letters in range(26):
                    if(lowercase_letter == list2[letters]):
                        if(list[letters] > 0):
                            list[letters] -= 1
                            check_letter = True
                            guess_to_check[spot].background_color = YELLOW # if letter is in but not at correct position, make yellow

                if check_letter == False:
                    guess_to_check[spot].background_color = GREY # otherwise, the letter is grey
                
                game_result = ""
                game_over = True
                check_letter = False

        else:
            guess_to_check[spot].background_color = GREY # otherwise, the letter is grey
            game_result = ""
            game_over = True
        guess_to_check[spot].draw()
        pygame.display.update()
    
    guesses_count += 1 # increase guess count 
    current_guess = [] # clear current guess
    current_guess_string = "" # clear current guess string
    current_letter_background_horizontal = 110 # set letter spacing

    if guesses_count == 6 and game_result == "": # if guesses = 6 and game is not won, result is a loss
        game_result = "L"

# define a function to count number of occurences of letters in said word
        
def find_all_letters():
    for letters in range(5):
        for count in range(26):
            if(CORRECT_WORD[letters] == list2[count]):
                list[count] += 1

# define a function to reset the count
def reset_letters():
    for letters in range(26):
        list[letters] = 0

# define a function to create a new letter for display

def create_new_letter():
    global current_guess_string, current_letter_background_horizontal
    current_guess_string += key_pressed # add key to current string
    new_letter = Letter(key_pressed, (current_letter_background_horizontal, guesses_count*100+LETTER_VERTICAL_SPACING)) # set spacing for letter
    current_letter_background_horizontal += LETTER_HORIZONTAL_SPACING
    guesses[guesses_count].append(new_letter) # add new letter to the end guesses list
    current_guess.append(new_letter) # add new letter to the end of current_guess list
    for guess in guesses:
        for letter in guess:
            letter.draw() # iterate through and display all letters

# define a function to delete a letter from the display

def delete_letter():
    global current_guess_string, current_letter_background_horizontal
    guesses[guesses_count][-1].delete() # delete last element from guesses list
    guesses[guesses_count].pop() 
    current_guess_string = current_guess_string[:-1] # remove letter from current_guess_string
    current_guess.pop()
    current_letter_background_horizontal -= LETTER_HORIZONTAL_SPACING # reset spacing

# define restart function to reset the game

def restart():
    global guesses_count, CORRECT_WORD

    CORRECT_WORD = random.choice(WORDS) #Chooses a new word from word bank to guess
    print("***New correct word:", CORRECT_WORD)

    reset_letters() #resets letter guess count
    for count in range(26): # resets the count of each letter occurance
        list[count] = 0

    find_all_letters() #finds all letter occurances in new word

    for guess in reversed(guesses): # needs fixed########################################################################################
        for letter in guess:
            letter.background_color = "white"
            letter.draw()
        for _ in range(5):
            guesses[guesses_count][-_].delete()

    guesses_count = 0 # guess count is returned to 0

# main driver code of the program

while True:

    for event in pygame.event.get(): # for event in pygame
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # if return is pressed
                if game_result != "":
                    pygame.quit()
                    sys.exit()
                else:
                    if len(current_guess_string) == 5 and current_guess_string.lower() in WORDS: # if guess length is 5 and a valid word (from list)
                        find_all_letters()
                        check_guess(current_guess) # check the guess
                        reset_letters()
            elif event.key == pygame.K_BACKSPACE: # if key is backspace delete the last letter
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "": # if key pressed is a letter, create new letter
                    if len(current_guess_string) < 5:
                        create_new_letter()

        ###################################################################
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if boundaries.collidepoint(event.pos): #if mouse is clicked over the button
                print("Restart button clicked")
                restart()

        if boundaries.collidepoint(pygame.mouse.get_pos()): #if mouse is over button, change color
            button_surface.fill(color_dynamic)
        else:
            button_surface.fill(color_static) #else do nothing to button color
 
        screen.blit(button_surface, (button_x, button_y)) #Initializes the button on the screen
        screen.blit(text, text_rect.topleft) #Initializes text on the button
        pygame.display.flip()