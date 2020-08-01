import random, sys
class Player:
    def __init__(self):
        self.Hscore = 0
        self.Cscore = 0
class Computer(Player):
    def play(self):
        d = {1: "stone", 2: "paper", 3: "scissor"}
        h_val = input("Enter stone, paper or scissor:-->  ")
        h_val = h_val.lower()
        try:
            if  h_val != 'stone' and h_val != 'paper' and h_val != 'scissor':
                return "Oops! Please provide a valid input...."
            elif int(h_val):
                return "Oops! Please provide a valid input...."
        except ValueError:
            pass
        x = random.randint(1, 3)
        c_val = d.get(x)
        print("Computer Choosed : " + str(c_val))
        if c_val == h_val:
            return self.Cscore, self.Hscore
        elif (c_val == "stone" and h_val == "scissor") or (c_val == "paper" and h_val == "stone") or (
                c_val == "scissor" and h_val == "paper"):
            self.Cscore += 1
        else:
            self.Hscore += 1
        return self.Cscore, self.Hscore
name = input("Enter your Name: ")
try:
    if int(name):
        sys.exit("Oops! Please provide a valid name....")
except ValueError:
    pass
while (True):
    c = Computer()
    try:
        m = int(input("Enter how many Final Counts(upto You will play):  "))
    except ValueError:
        print("Oops! Please provide only valid input..")
        s = input("If u want to continue press Y/y or N/n to quit: ")
        if s == 'Y' or s == 'y':
            continue
        else:
            print("************Thanks For Playing**************")
            break
    final = []
    i = 0
    while (i < m):
        r = c.play()
        if type(r) == tuple:
            print("comuter and your score: ", r)
            i += 1
        else:
            print(r)
            s = input("If u want to continue press Y/y or N/n to quit: ")
            if s == 'Y' or s == 'y':
                continue
            else:
                print("************Thanks For Playing**************")
                break
        final.append(r)
    if final[-1][0] < final[-1][1]:
        print("congragulations {} well played! Your final score is {} ---- > Computer Final Score is {}".format(
            name.upper(),
            final[
                -1][
                1],
            final[
                -1][
                0]))
    elif final[-1][0] == final[-1][1]:
        print("Your final score is {} ---- > Computer Final Score is {}".format(final[-1][1], final[-1][0]))
        print("***************Match Draw!***************")
    else:
        print("Sorry! {} Better luck next time Your final score is {} ---- > Computer Final Score is {}".format(
            name.upper(), final[-1][1], final[-1][0]))
    s = input("If u want to play again press Y/y or N/n to quit: ")
    if s == 'Y' or s == 'y':
        continue
    else:
        print("************Thanks For Playing**************")
        break
