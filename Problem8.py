#Solution for problem #8

num = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

index = 0

max_root = 0 #Keeps track of best adjusted digital root so far
best_string = "" #String that yielded max_root
current_root = 0 #Keeps track of current adjusted digital root in current iteration

while index < len(num) - 13: #We iterate through all indices of the string except the last thirteen (to avoid IndexErrors)
    substr = num[index:index+13] #String slice of each thirteen-digit section
    for ind, char in enumerate(substr):
        if char == "0": #If a substring contains a zero, we skip past it (since a zero guarantees a product of 0)
            index += ind
            break
        if char != "1": #We do not add values of 1, since they do not contribute to the product
            current_root += int(char)
    if current_root > max_root: #We update the max_root if necessary
        max_root = current_root
        best_string = substr
    index += 1 #Then, we adjust the index and reset the current_root for the next iteration
    current_root = 0

product = 1
for char in best_string: #Product of best_string is calculated for user friendliness
    product *= int(char)

print("Congratulations! The best substring found was: " + best_string + " with a product of " + str(product)) # :))