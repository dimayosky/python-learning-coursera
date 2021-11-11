HowManyPenguins = input()
IsNumber = HowManyPenguins.isnumeric()
if IsNumber:
        int(HowManyPenguins)
#HowManyPenguins = int(input())
pinguinRow1 =        "   _~_    " * int(HowManyPenguins)
pinguinRow2 = "\n" + "  (o o)   " * int(HowManyPenguins)
pinguinRow3 = "\n" + " /  V  \  " * int(HowManyPenguins)
pinguinRow4 = "\n" + "/(  _  )\ " * int(HowManyPenguins)
pinguinRow5 = "\n" + "  ^^ ^^   " * int(HowManyPenguins)
pinguin = pinguinRow1 + pinguinRow2 + pinguinRow3+ pinguinRow4+ pinguinRow5
print(pinguin)
