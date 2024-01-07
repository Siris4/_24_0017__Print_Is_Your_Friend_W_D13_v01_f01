#Print is Your Friend
pages = 0
word_per_page = 0
print(pages)
pages = int(input("Number of pages: "))
print(pages)
word_per_page == int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words)
#0
#Number of pages: 2
#2
#Number of words per page: 4
#0
#0



# Using a Debugger:
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = (item * 2)
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

