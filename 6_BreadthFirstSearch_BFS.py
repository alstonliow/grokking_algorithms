
# graph

graph = {
    "you":    ["alice", "bob", "claire"],
    "bob":    ["anuj", "peggy"],
    "alice":  ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj":   [],
    "peggy":  [],
    "thom":   [],
    "jonny":  []
}

from collections import deque #deque is a double-ended queue
def person_is_seller(name):
    return name[-1] == 'm' # If the name ends with 'm', then this person is a mango seller #return True or False

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
    
search("you")
search("bob")