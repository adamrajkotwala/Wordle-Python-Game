##
# @file PLAYER.py
#
# @brief Defines the main driver program for Wrodle
#
#
import random # to generate random numbers
import sys
from word_list import * # access to word_list file that contains list of different 5 letter words
import pygame # pygame library for game development
import unittest #used to test the program

pygame.init() # initialize pygame

#DEFINING CONSTANTS

WIDTH, HEIGHT = 750, 1000 # dimensions of the display

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # define screen with desired dimensions
BACKGROUND = pygame.image.load("design/Starting Tiles.png") # define background, load image with background tiles found online
BACKGROUND_RECTANGLE = BACKGROUND.get_rect(center=(375, 300)) # define background rectangle and center it
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

CORRECT_WORD = random.choice(ANSWERS)

ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

LETTER_FONT = pygame.font.Font("design/BrontidevpDemoStyle2-ZV8E3.otf", 50) # define a letter font variable with font file

# Restart Button
window = (750, 1000) # size of window
screen = pygame.display.set_mode(window) #screen to be used with button functionality

color = (255, 255, 255) #Font color of button
color_static = (170, 170, 170) #color of button when not hovering over (light grey)
color_dynamic = (140, 140, 140) #color of button when hovered (dark grey)

font = pygame.font.Font(None, 30) #font of button

button_width = 150 #Dimensions and relative position of the button
button_height = 50
button_x = (window[0] - button_width) / 2
button_y = window[1] - button_height - 40

button_surface = pygame.Surface((button_width, button_height)) #Creates button surface
button_surface.fill(color_static) #Makes the interior of the button light grey

text = font.render('Restart', True, color) #Creates text for the button
text_rect = text.get_rect(center=(button_width / 2, button_height / 2))
text_rect.center = (button_x + button_width / 2, button_y + button_height / 2) #Places text in the center of the button

boundaries = pygame.Rect(button_x, button_y, button_width, button_height) #Creates the clickable boundaries of the button

# setup display screen and display the background in the boundaries of "background rectangle"

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECTANGLE)
pygame.display.update()

# define variables for spacing and size

LETTER_HORIZONTAL_SPACING = 85
LETTER_VERTICAL_SPACING = 12
LETTER_SIZE = 75

# define variables for guess count, 2D list to contain all guesses, a list for current guess, string for this guess, current letter spacing

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
current_letter_background_horizontal = 167.5
game_result = "" # string to represent the result of the game 
keyboard = []

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

class Alphabet:
    
    def __init__(self, horizontal, vertical, letter):
        self.horizontal = horizontal
        self.vertical = vertical
        self.text = letter
        self.rect = (self.horizontal, self.vertical, 57, 75)
        self.background_color = OUTLINE
        
    def draw(self):
        pygame.draw.rect(SCREEN, self.background_color, self.rect)
        self.text_display = LETTER_FONT.render(self.text, True, "white")
        self.text_rect = self.text_display.get_rect(center = (self.horizontal+27, self.vertical+30))
        SCREEN.blit(self.text_display, self.text_rect)
        pygame.display.update()
        
# draw the alphabet on screen

alphabet_horizontal, alphabet_vertical = 75, 600

for i in range(3):
    for letter in ALPHABET[i]:
        new_letter = Alphabet(alphabet_horizontal, alphabet_vertical, letter)
        keyboard.append(new_letter)
        new_letter.draw()
        alphabet_horizontal += 65
    alphabet_horizontal += 20
    alphabet_vertical += 100
    if i == 0:
        alphabet_horizontal = 110
    elif i == 1:
        alphabet_horizontal = 170
    
# function to check the guess
def check_guess(guess_to_check):
    global current_guess, current_guess_string, guesses_count, current_letter_background_horizontal, game_result, two_to_six_horizontal
    game_over = False

    for i in range(5):
        lowercase_letter = current_guess[i].text.lower() # first letter in current guess
        if lowercase_letter == CORRECT_WORD[i]:
            for letters in range(26):
                if(lowercase_letter == list2[letters]):
                    if(list[letters] > 0):
                        list[letters] -= 1
                print(list[letters])

    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower() # first letter in current guess
        
        # if letter is in the correct word
        
        if lowercase_letter in CORRECT_WORD: 
            if lowercase_letter == CORRECT_WORD[i]: # if letter is equal to letter at this position in the correct word
                guess_to_check[i].background_color = GREEN # letter is correct, make green

                for keyboard_i in keyboard:
                    if keyboard_i.text == lowercase_letter.upper():
                        keyboard_i.background_color = GREEN
                        keyboard_i.draw()

                guess_to_check[i].text_color = "white"
                if not game_over:
                    game_result = "W"
                    
            else:    
                
                guess_to_check[i].background_color = GREY

                for letters in range(26):
                    if(lowercase_letter == list2[letters]):
                        if(list[letters] > 0):
                            list[letters] -= 1
                            guess_to_check[i].background_color = YELLOW # if letter is in but not at correct position, make yellow

                for keyboard_i in keyboard:
                    if keyboard_i.text == lowercase_letter.upper():
                        keyboard_i.background_color = YELLOW
                        keyboard_i.draw()

                guess_to_check[i].text_color = "white"
                game_result = ""
                game_over = True
                
        # if letter is not in the correct word
            
        else:
            guess_to_check[i].background_color = GREY # otherwise, the letter is grey
            for keyboard_i in keyboard:
                    if keyboard_i.text == lowercase_letter.upper():
                        keyboard_i.background_color = GREY
                        keyboard_i.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_over = True
        guess_to_check[i].draw()
        pygame.display.update()
            
    
    guesses_count += 1 # increase guess count 
    current_guess = [] # clear current guess
    current_guess_string = "" # clear current guess string
    current_letter_background_horizontal = 167.5 # set letter spacing

    if guesses_count == 6 and game_result == "": # if guesses = 6 and game is not won, result is a loss
            game_result = "L"


#define a function to count number of occurences of letters in said word

def find_all_letters(word):
    """!Function marks down all letters used in word
    
    The function looks at each letter in the word and marks it down in an array of letters
    This is then used by other functions to determine what color to make the space if the letter is located in the
    word
    
    @param none
    @return none
    """

    for letters in range(5):
        for count in range(26):
            if(word[letters] == list2[count]):
                list[count] += 1

# define a function to reset the count
def reset_letters():
    for letters in range(26):
        list[letters] = 0

# define a function to create a new letter for display

def create_new_letter():
    """
    Adds a new letter to the current guess and updates display.

    This function adds the pressed key to the current guess string, creates a new Letter object
    with the key as its content, and updates its position horizontally. The new letter is appended
    to both the overall guesses list and the current guess list. Finally, it iterates through all
    letters in all guesses and displays them.

    Global Variables:
    - current_guess_string: str
        The current guess string.
    - current_letter_background_horizontal: int
        The horizontal position for the next letter background.
    - guesses: list of lists of Letter
        The list containing all previous guesses.
    - current_guess: list of Letter
        The list containing the letters of the current guess.

    Returns:
    None
    """
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
    
# define a function to display the play again screen

def play_again():
    pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))
    FUNCTION_FONT = pygame.font.Font("design/BrontidevpDemoStyle2-ZV8E3.otf", 35)
    play_again_font = FUNCTION_FONT
    correct_word_font = LETTER_FONT
    play_again_text = play_again_font.render("Press ENTER to Play Again", True, "black")
    play_again_rect = play_again_text.get_rect(center=(WIDTH/2, 775))
    correct_word_text = correct_word_font.render(f"The word was {CORRECT_WORD}", True, "black")
    correct_word_rect = correct_word_text.get_rect(center=(WIDTH/2, 675))
    SCREEN.blit(correct_word_text, correct_word_rect)
    SCREEN.blit(play_again_text, play_again_rect)
    pygame.display.update()
    
# define a function to reset the game, called when a new game is started

def wordle_reset():
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result, LETTER_HORIZONTAL_SPACING, LETTER_VERTICAL_SPACING, LETTER_SIZE, current_letter_background_horizontal
    LETTER_HORIZONTAL_SPACING = 85
    LETTER_VERTICAL_SPACING = 12
    LETTER_SIZE = 75
    current_letter_background_horizontal = 167.5
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECTANGLE)
    reset_letters() #resets letter guess count
    for count in range(26): # resets the count of each letter occurance
        list[count] = 0

    guesses_count = 0
    CORRECT_WORD = random.choice(WORDS)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    for letter in keyboard:
        letter.background_color = OUTLINE
        letter.draw()

    find_all_letters(CORRECT_WORD) #finds all letter occurances in new word

# main driver code of the program

#example: def test_upper(self):
#        self.assertEqual('foo'.upper(), 'FOO')

class TestStringMethods(unittest.TestCase):

    def test_reset_letters_firstValue(self): # first letter value in array
        reset_letters()
        self.assertEqual(list[0],0)

    def test_reset_letters_lastValue(self): # last letter value in array
        reset_letters()
        self.assertEqual(list[25],0)

    def test_for_letter_count(self): # check to make sure function correctly counts all letter instances
        word = "apple"
        find_all_letters(word)
        self.assertEqual(list[15], 2)
        self.assertEqual(list[0], 1)
        self.assertEqual(list[4], 1)
        self.assertEqual(list[11], 1)

    def test_reset_letters_allValues(self): # check if all values in the list are set to 0 after reset
        reset_letters()
        self.assertEqual(list, [0]*26)
    
    def test_create_new_letter(self): # check if a new letter is created and added to the current guess
        global current_guess_string, current_letter_background_horizontal, key_pressed
        current_guess_string = "" 
        current_letter_background_horizontal = 167.5
        key_pressed = "A"
        create_new_letter()
        self.assertEqual(len(current_guess), 1)
        self.assertEqual(len(guesses[0]), 1)
        self.assertEqual(current_guess_string, "A")
        self.assertEqual(current_letter_background_horizontal, 167.5 + LETTER_HORIZONTAL_SPACING)

    def test_delete_letter(self):  # chck that the last letter is deleted
        global current_guess_string, current_letter_background_horizontal
        current_guess_string = "ABCDE"
        current_letter_background_horizontal = 167.5
        guesses[0] = [Letter("A", (0, 0)), Letter("B", (0, 0)), Letter("C", (0, 0))]
        delete_letter()
        self.assertEqual(len(guesses[0]), 2)
        self.assertEqual(current_guess_string, "ABCD")
        self.assertAlmostEqual(current_letter_background_horizontal, 167.5 - LETTER_HORIZONTAL_SPACING)




    
    
        

while True:
    unittest.main() # used to run the tests
    if game_result != "":
        play_again()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if action.type == pygame.KEYDOWN:
            if action.key == pygame.K_RETURN:
                if game_result != "":
                    wordle_reset()
                else:
                    if len(current_guess_string) == 5 and current_guess_string.lower() in WORDS:
                        find_all_letters(CORRECT_WORD)
                        check_guess(current_guess) # check the guess
                        reset_letters()
            # else if key pressed is backspace
            elif action.key == pygame.K_BACKSPACE: # if key is backspace delete the last letter
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                key_pressed = action.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()
        if action.type == pygame.MOUSEBUTTONDOWN and action.button == 1:
            if boundaries.collidepoint(action.pos): #if mouse is clicked over the button
                wordle_reset()
        if boundaries.collidepoint(pygame.mouse.get_pos()): #if mouse is over button, change color
            button_surface.fill(color_dynamic)
        else:
            button_surface.fill(color_static) #else do nothing to button color
 
        screen.blit(button_surface, (button_x, button_y)) #Initializes the button on the screen
        screen.blit(text, text_rect.topleft) #Initializes text on the button
        pygame.display.flip()
