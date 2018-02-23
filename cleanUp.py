import string
x = input("Please enter a sentence: ").lower()

removeA = x.replace("a", "")
removeE = removeA.replace("e", "")
removeI = removeE.replace("i", "")
removeO = removeI.replace("o", "")
removeU = removeO.replace("u", "")

print("All vowels have been removed: " + removeU)

swap = removeU.translate(bytes.maketrans(b"vb",b"bv"))
print("V's and B's have been swapped: "+swap)

total = len(swap) - swap.count(" ")
print("Total number of letters: " + str(total))

