def create_graph(x, y):
    # creates the adjacency list dictionary for a boggle graph
    graph = {}
    for i in range(x*y):
        nodes = [i-x, i+x]

        if i%x != 0: # not on the left edge
            nodes += [i-x-1, i-1, i+x-1]

        if (i+1)%x != 0: # not on the right edge
            nodes += [i-x+1, i+1, i+x+1]

        graph[i] = [n for n in nodes if 0 <= n < x*y]
    return graph

def word_is_possible(word, letters):
    new_words = []
    pool = list(letters)
    for letter in word:
        if letter in pool:
            pool.remove(letter)
        else:
            return False
    return True

def word_in_graph(word, graph, letters):
    starts = [i for i, c in enumerate(letters) if c == word[0]]
    for start in starts:
        stack = [start]
        needed = list(word[1::][::-1]) # top is the next letter to find
        found = False
        current = start
        while len(stack) > 0:
            letter_needed = needed.pop()
            exits = [n for n in graph[current] if letters[n] == letter_needed]
            if not exits:
                current = stack.pop()
                needed.append(letter_needed)
            else:
                current = exits[0]

                

    
    return False
        

letters = "abcdefghijklmnopqrstuvwxy"
    
# for word in open('words.txt','r').readlines():
#     if word_is_possible(word, letters):
        

