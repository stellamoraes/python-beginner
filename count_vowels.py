#Python Exercise: Create a code to count vowels

vowels= ['a', 'e', 'i', 'o', 'u']

quote = """As long as I live, I’ll hear waterfalls 
and birds and winds sing. I’ll interpret the rocks, 
learn the language of flood, storm, and the avalanche. 
I’ll acquaint myself with the glaciers and wild gardens,
 and get as near the heart of the world as I can."""

counter= 0
for word in quote: 
    if word in vowels: 
        counter = counter + 1
print(counter)