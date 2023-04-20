import cowsay
flames = ["FRIENDS","LOVERS","AFFECTIONATE","MARRIAGES","ENEMIES","SIBLINGS"]
your_name = str(input("What is your name? "))
crush_name = str(input("What is your crush's name? "))
alpha= [i for i in your_name.lower()]
beta = [i for i in crush_name.lower()]
for i  in alpha:
    if i in beta:
        alpha.remove(i)
        beta.remove(i)
for i in beta:
    alpha.append(i)
if len(alpha) > len(flames):
    flames = flames*5
x=len(alpha)-1
cowsay.trex(flames[x])


     