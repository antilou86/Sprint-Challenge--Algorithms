'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    index = 0
    def count_helper(word, index, count):
        if index >= len(list(word))-1:
            return count
        elif list(word)[index] == "t" and list(word)[index+1] =="h":
            count += 1
            index += 2
            return count_helper(word, index, count)
        else: 
            index += 1
            return count_helper(word, index, count)
    return count_helper(word, index, count)


