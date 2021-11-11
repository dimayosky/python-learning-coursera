HowManyPenguins = input()
IsNumber = HowManyPenguins.isnumeric()
if IsNumber:
    int(HowManyPenguins)
# HowManyPenguins = int(input())
pinguin =        ("   _~_    " * int(HowManyPenguins) +
           "\n" + "  (o o)   " * int(HowManyPenguins) +
           "\n" + " /  V  \  " * int(HowManyPenguins) +
           "\n" + "/(  _  )\ " * int(HowManyPenguins) +
           "\n" + "  ^^ ^^   " * int(HowManyPenguins))
print(pinguin)
