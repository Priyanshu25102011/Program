class Flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
flash = []
print("Welcome to Flashcards Application")
while(True):
    word = input("Enter the name you want to add to Flashcrads: ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(Flashcard(word,meaning))
    option = int(input("enter 0, if you want to add another flashvard otherwise enter 1: "))
    if(option):
        break
print("\n Your Flashcards are:")
for i in flash:
    print(">",i)