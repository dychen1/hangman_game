import WordGenerator

def CheckChosenWord(ChosenWord):
    NumberOfLetters = len(ChosenWord)
    ArrayForWord = list(ChosenWord)
    HolderArray = ["_"] * NumberOfLetters
    print(HolderArray)
    print("The word is {} letters long.\n".format(NumberOfLetters))
    return NumberOfLetters, ArrayForWord, HolderArray


def LifeDeduction(CurrentNumberOfLives):
    CurrentNumberOfLives -= 1
    print("Incorrect Guess")
    print("The player has {} lives remaining.".format(CurrentNumberOfLives))
    if CurrentNumberOfLives == 0:
        print("-- Game Over --")
        quit()
    return CurrentNumberOfLives


def LetterVerification(UserLetter, ChosenWord, ArrayForWord, HolderArray):
    for LetterPosition in range(0, len(ChosenWord)):
        if UserLetter == ArrayForWord[LetterPosition]:
            HolderArray[LetterPosition] = UserLetter
    print(HolderArray)
    if UserLetter not in ChosenWord:
        return False
    else:
        return ArrayForWord


def main(NumberOfLives, ChosenWord):
    # CHOOSE WORD FUNCTION NEEDED HERE
    NumberOfLetters, ArrayForWord, HolderArray = CheckChosenWord(ChosenWord)
    while NumberOfLives > 0:
        UserLetter = str(input("What is your guess?: "))
        while UserLetter.isalpha() == False or len(UserLetter) != 1:
            UserLetter = str(input("Please pick a single letter: "))
        if LetterVerification(UserLetter, ChosenWord, ArrayForWord, HolderArray) == False:
            NumberOfLives = LifeDeduction(NumberOfLives)
        elif HolderArray == ArrayForWord:
            print("-- YOU WIN! --")
            quit()


if __name__ == "__main__":
    StartingNumberOfLives = 10
    print("The player is starting with {} lives".format(StartingNumberOfLives))
    GeneratedWord = WordGenerator.word_generator()
    main(StartingNumberOfLives, GeneratedWord)