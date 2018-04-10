# split()
colors = 'red,green,blue'
tokens = colors.split(',')
print(tokens)
words = 'hello world'
print(words.split())

# splitlines()
quote_text = '''First, solve the problem. Then, write the code. - John Johnson
Talk is cheap. Show me the code. - Linus Torvalds
Good design adds value faster than it adds cost. - Thomas C. Gale
Computers are good at following instructions, but not at reading your mind. - Donald Knuth
Without requirements or design, programming is the art of adding bugs to an empty text file. - Louis
Srygley'''
quotes = quote_text.splitlines()
for quote in quotes:
    print(quote)