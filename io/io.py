with open('./example.txt', 'r') as f:
    l = f.readlines()
    l = [i.strip('\n') for i in l]

print(l)