# 5.2.2 Avoiding Duplicates
#def check_voter(name)

voted = {}

def check_voter(name):
    if name in voted:
        print('out')
    else:
        voted[name] = True
        print('in')

check_voter("tom")
check_voter("bob")
check_voter("tom")

print(voted)

#Cache
#5.2.3 

cache = {}

def get_page(url):
    if url not in cache:
        cache[url] = get_data_from_server(url)
    return cache[url]