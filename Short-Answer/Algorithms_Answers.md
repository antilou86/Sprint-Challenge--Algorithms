#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - with the way this is written, the function has to perform n operations every time it runs before it hits the limit specified by the while loop. making it O(n)

b) O(n^2) - if this were only performing one operation for each number leading up to N it would be O(n), but this is performing the operations within the while loop for each integer from 0 to n. doubling up our operations compaired to doing a single loop


c) O(n) - this is a recursive function that will call itself as many times as there are bunnies. may as well be a for loop.

## Exercise II

since i'm really greedy for eggs, i want to figure out how to minimize the number of dropped AND broken eggs.

this is rough because if n is equal to soemthing on the first floor, the most minimal way is to loop through floors, dropping on at a time until one breaks. but since we cant make assumptions like that, the safest way is to use a binary search, basically.

so, 1st, within a function that is given n, i would make an array like this: 
    stories = []
    for i in range(n):
        stories.append(i)

then write a recursive binary search function -> 

    def find_safe_floor(stories):  
    
    define variables-
        current_floor = stories[len(stories)//2]

    add a base case-
        if (len(stories) == 1):
            return stories[0]
    
    lets say "drop_egg" is a function that returns either broken or unbroken. pick the middle point in the array, and test.
    if it breaks everything above it is useless to me.
    
        if (drop_egg(current_floor) == "broken"):
            find_safe_floor(stories[:len(stories)//2])

    if not, everything below it is useless to me

        else:
            find_safe_floor(stories[len(stories)//2:])

translates to roughly => 
    O(n) + O(1) + O(log n /2) + O(log n /2) rough translation of above
    o(n) + O(1) + O(log n) + O(log n) simplified.
    O(n) + O + 2(O(log n)) remove simple integers
    O(n) + O(log n) remove single elements and simple integers
    O(log n) Dominates.

    run-time complexity = O(log n)


        
        
