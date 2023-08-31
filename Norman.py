print ("Welcome to the Resteraunt Rater :)" )
print("Here are some resteraunts for you to rate")
resteraunts = ["Dog Haus", " Ramen Tatsunoya","Russell's", "Dirt Dog","Jake's Burgers", "True Food Kitchen"]
new_resteraunt= (input ( "would you like to add to the list yes for no?"))
if new_resteraunt == "yes":
    answer = input("What resteraunt would you like to add to the list?")
    resteraunts.append(answer)

print ("Alright lets rank the existing resteraunts")
print ("ITS RANKING TIME")

top = resteraunts[0]
for res in resteraunts:
    str = "do you like" + top + "or" +  res + "a/b"
    rank = input(str)
    if rank == "b":
        top =  res
resteraunts.remove(top)
resteraunts.insert (0, top)


top2 = resteraunts[1]
for res in resteraunts[1:]:
    str = "do you like" + top2 + "or" +  res + "a/b"
    rank = input(str)
    if rank == "b":
        top2 =  res
resteraunts.remove(top2)
resteraunts.insert (1, top2)

top3 = resteraunts[2]
for res in resteraunts[2:]:
    str = "do you like" + top3 + "or" +  res + "a/b"
    rank = input(str)
    if rank == "b":
        top3 =  res
resteraunts.remove(top3)
resteraunts.insert (2, top3)

top4 = resteraunts[3]
for res in resteraunts[3:]:
    str = "do you like" + top4 + "or" +  res + "a/b"
    rank = input(str)
    if rank == "b":
        top4 =  res
resteraunts.remove(top4)
resteraunts.insert (3, top4)

top5 = resteraunts[4]
for res in resteraunts[4:]:
    str = "do you like" + top5 + "or" +  res + "a/b"
    rank = input(str)
    if rank == "b":
        top5 =  res
resteraunts.remove(top5)
resteraunts.insert (4, top5)

top6 = resteraunts[5]
for res in resteraunts[5:]:
    str = "do you like" + top6 + "or" +  res + "a/b"
    rank = input(str)
    if rank == "b":
        top6 =  res
resteraunts.remove(top6)
resteraunts.insert (5, top6)




