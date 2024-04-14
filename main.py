# test on https://www.puzzle-words.com/boggle-5x5-extreme/ 

import cmd

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
    # check if a a word can be made using the letters on the grid (this stops 
    # wasted searches to speed up the algorithm)
    new_words = []
    pool = list(letters)
    for letter in word:
        if letter in pool:
            pool.remove(letter)
        else:
            return False
    return True

def find_path(word, graph, letters):
    # check if the word can be made by travelling from a given starting node
    if len(word) == 1:
        if word in letters:
            return True

    if not word:
        return false
    
    # find all the potential start points
    starts = [i for i, c in enumerate(letters) if c == word[0]]
    for start in starts:
        stack = [start]
        needed = list(word[1::][::-1]) # top is the next letter to find
        visited = [start]

        current = start
        letter_needed = needed.pop()
        while stack:
            # find the valid exits onto the next letter in the word (you cannot 
            # backtrack onto a node you have already visited)
            exits = [i for i in graph[current] if letters[i] == letter_needed and i not in visited]
            if not exits:
                needed.append(letter_needed)
                letter_needed = letters[current]
                current = stack.pop()
            else:
                if not needed: 
                    # reached the final letter :. a path exists!
                    return stack

                stack.append(current) # add current to the stack to backtrack to if needed
                current = exits[0] # move on to the next exit
                visited.append(current) # mark the new node as visited
                letter_needed = needed.pop() # get the next letter needed to make the word
    return []

def get_answers(graph, letters):
    answers = []
    for word in open('words.txt','r').readlines():
        word = word.strip() # remove whitespace
        path = find_path(word, graph, letters)
        if word_is_possible(word, letters) and path:
            # the word is a valid answer
            answers.append(word)

    return sorted(answers, key=len, reverse=True) # answers sorted from longest

class App(cmd.Cmd):
    letters = "ousectesoreuabhtlfogcaesy"
    grid = {}
    prompt = f'{letters} >> '

    def do_set_letters(self, letters):
        """
        Set the letters in the grid (read left to right, row by row)
        """
        self.letters = letters

    def do_set_grid(self, dimensions):
        """
        Set the dimensions of the grid
        """
        x, y = map(int, dimensions.split())
        self.grid = create_graph(x, y)
    
    def do_top_words(self, num):
        """
        Print the top `num` words
        """
        num = num or 5
        answers = get_answers(self.grid, self.letters)
        for i in range(int(num)):
            print(answers[i])


if __name__ == "__main__":
    App().cmdloop()    

