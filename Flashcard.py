class Flahcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+' (  '+self.meaning+')'
flash = []
print("WELCOME TO FLASHCARD APPLICATION")
while(True):
 word = input("Enter the NAME you want to add to flashcard :")
 meaning = input("Enter the MEANING of the word:")
 flash.append(Flahcard(word, meaning))
 option = int(input("Enter 0 , if you want to add another FLASHCARD otherwise enter 1 :"))
 if(option):
    break
print("\nYour flashcards")
for i in flash:
   print(">", i)