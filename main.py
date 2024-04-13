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

        path_exists = True
        current = start
        letter_needed = needed.pop()
        visited = []
        while path_exists:
            exits = [i for i in graph[current] if letters[i] == letter_needed and i not in visited]
            if not exits:
                needed.append(letter_needed)
                letter_needed = letters[current]

                visited.append(current)
                current = stack.pop()
            else:
                if len(needed) == 0:
                    return True

                stack.append(current)
                current = exits[0]
                letter_needed = needed.pop()

            if not stack and current == start:
                path_exists = False

    return False
        

letters = "ahulsangirdeitmp"
graph = create_graph(4, 4)
print(word_in_graph('ahulgep', graph, letters))
    
# for word in open('words.txt','r').readlines():
#     if word_is_possible(word, letters):
        

