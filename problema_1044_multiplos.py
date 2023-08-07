#n = input('').split()
#a = int(n[0])
#b = int(n[1])
a, b = map(int, input('').split())
if a % b == 0 or b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
