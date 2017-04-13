import random
#Self-writing program
seed = random.randint(0,1000)
with open('selfish'+str(seed)+'.py','w') as k:
    with open('selfish.py') as f:
        for line in f:
            k.write(line)
