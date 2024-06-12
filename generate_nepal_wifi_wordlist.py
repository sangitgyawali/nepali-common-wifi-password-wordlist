import itertools
common_words = ['password', 'nepal', 'internet', 'wifi', 'router', 'connect', 'secure', 'home', 'office']
names = ['ram', 'sita', 'hari', 'gita', 'shyam', 'rita', 'bishal', 'anita', 'mohan', 'raju']
places = ['kathmandu', 'pokhara', 'biratnagar', 'lalitpur', 'bhaktapur', 'dharan', 'butwal', 'hetauda']
numbers = ['123', '456', '789', '1010', '2020', '1111', '2222', '3333', '1234', '4321']
wordlist = set()
wordlist.update(common_words)
wordlist.update(names)
wordlist.update(places)
for combo in itertools.product(common_words + names + places, repeat=2):
    wordlist.add(''.join(combo))
for word in common_words + names + places:
    for number in numbers:
        wordlist.add(f'{word}{number}')
        wordlist.add(f'{number}{word}')
wordlist = list(wordlist)
with open('nepal_wifi_wordlist.txt', 'w') as file:
    for password in wordlist:
        file.write(password + '\n')
print(f"Generated wordlist with {len(wordlist)} entries.")
