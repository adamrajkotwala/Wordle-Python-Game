##########################
#       Wordle
#      2/23/2024
#       main.py
##########################
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
import random
import re

class Wordle:
    def __init__(self, root):
        self.root = root
        self.tries = 0 #current try user is on
        self.word_bank = ["small", "chair", "table", "bread", "wreck", "queen", "grape", 
                        "hotel", "lemon", "mango", "ivory", "house", "ocean", "knife", 
                        "horse", "gloves", "music", "snake", "dress", "tiger", "zebra", 
                        "plane", "peach", "plate", "beach", "cloud", "river", "paper", 
                        "laser", "smile", "radio", "stone", "water", "clock", "brush", 
                        "green", "brown", "heart", "shark", "black", "white", "freak", 
                        "plant", "happy", "dance", "light", "laugh", "watch", "sleep", 
                        "dream", "ghost", "magic", "space", "leave", "salad", "stink", 
                        "jeans", "shirt", "socks", "shoes", "boots", "floor", "scarf", 
                        "skirt", "blouse", "pants", "purse", "creep", "tooth", "paste", 
                        "clean", "towel", "water", "rinse", "shake", "drink", "juice", 
                        "spoon", "apple", "marry", "melon", "loser", "whine", "chase", 
                        "toast", "bacon", "toast", "crank", "pizza", "pasta", "grave",
                        "steal", "olive", "first", "beans", "curry", "cream", "wheel"
                        "sugar", "honey", "syrup", "sauce", "gravy", "butter", "cheese", 
                        "crawl", "fruit", "broad", "camel", "drive", "glass", 
                        "stool", "shelf", "books"]
        self.word = self.get_word() #calls function to select random word from above list

        self.main_page() #created main page for Wordle game
    
    def get_word(self):
        return random.choice(self.word_bank)

    def main_page(self): #Creates main Window to interact with
        self.root.title("Wordle")
        self.root.geometry("500x500")
        self.root.configure(background="lightcyan3")

        #Title
        wordle = Label(self.root, bg="lightcyan3", text="Wordle", font=("Impact", 25))
        wordle.grid(row=1, column=5, padx=125, pady=5)

        #Tries 1-5
        self.try1 = Label(self.root, bg="lightcyan3", text="_ _ _ _ _", font=("Euromode", 18))
        self.try1.grid(row=2, column=5, padx=5, pady=5)
        self.try2 = Label(self.root, bg="lightcyan3", text="_ _ _ _ _", font=("Euromode", 18))
        self.try2.grid(row=3, column=5, padx=5, pady=5)
        self.try3 = Label(self.root, bg="lightcyan3", text="_ _ _ _ _", font=("Euromode", 18))
        self.try3.grid(row=4, column=5, padx=5, pady=5)
        self.try4 = Label(self.root, bg="lightcyan3", text="_ _ _ _ _", font=("Euromode", 18))
        self.try4.grid(row=5, column=5, padx=5, pady=5)
        self.try5 = Label(self.root, bg="lightcyan3", text="_ _ _ _ _", font=("Euromode", 18))
        self.try5.grid(row=6, column=5, padx=5, pady=5)

        #Entry Box
        self.entry = Entry(self.root, width=20)
        self.entry.grid(row=8, column=5, padx=5, pady=5)

        #Entry Button
        enter_button = Button(self.root, text="Enter", command=self.enter_guess)
        enter_button.grid(row=8, column=6, padx=0, pady=5)


    def update_main(self, guess): # reconfigures each of the tries to output the guess
        if self.tries == 1:
            self.try1.config(text="            " + guess[0] + " " + guess[1] + " " + guess[2] + " " + guess[3] + " " + guess[4] + "  Try 1/5")

        elif self.tries == 2:
            self.try2.config(text="            " + guess[0] + " " + guess[1] + " " + guess[2] + " " + guess[3] + " " + guess[4] + "  Try 2/5")

        elif self.tries == 3:
            self.try3.config(text="            " + guess[0] + " " + guess[1] + " " + guess[2] + " " + guess[3] + " " + guess[4] + "  Try 3/5")

        elif self.tries == 4:
            self.try4.config(text="            " + guess[0] + " " + guess[1] + " " + guess[2] + " " + guess[3] + " " + guess[4] + "  Try 4/5")

        elif self.tries == 5:
            self.try5.config(text="            " + guess[0] + " " + guess[1] + " " + guess[2] + " " + guess[3] + " " + guess[4] + "  Try 5/5")

    def enter_guess(self): #checks to see if guess is valid and then if it is correct
        guess = self.entry.get()

        if self.tries >= 5:
            messagebox.showinfo("Game Over", "You do not have any tries left, the correct word is " + self.word)

        else:

            if bool(re.match('^[a-zA-Z]+$', guess)): #check is guess contains letters
            
                if len(guess) != 5: #check if guess length is = to 5
                    messagebox.showwarning("Invalid guess", "Your guess must be 5 letters long")

                elif guess.lower() == self.word.lower(): #check if guess is equivalent to word
                    self.tries += 1 #increment try counter
                    messagebox.showinfo("Correct!", "You guessed the correct word!")
                    self.update_main(guess)
        
                else:
                    self.tries += 1 #increment try counter
                    self.update_main(guess)
            
            else:
                messagebox.showwarning("Invalid Guess", "Your guess must only contain letters")

def main():
    root = Tk()
    root.title("Wordle")
    game = Wordle(root)
    root.mainloop()

if __name__ == "__main__":
    main()