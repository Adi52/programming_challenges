import random, time

cls = lambda: print('\n' * 1000)

answers = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.',
           'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
           'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.',
           'Concentrate and ask again.', "Don't count on it.", 'My reply is no.', 'My sources say no.',
           'Outlook not so good.', 'Very doubtful.']

messege = """\nSpike's 8-Ball reaches into the future, to find the answers to your questions. It knows what will be, and is 
willing to share this with you. Just think of a question that can be answered "Yes" or "No", concentrate very, 
very hard, and print 'y'. Then let Spike's 8-Ball show you the way!"""



active = True
while active:
    print(messege)
    y = input('Ask: ')
    if y == 'y':
        pass
    else:
        break

    time.sleep(2)
    print('\n')
    answer = random.choice(answers)
    print(answer.upper())

    print('\n')

    x = input("Again? [y/n]: ")

    if x == "n":
        break

    cls()


