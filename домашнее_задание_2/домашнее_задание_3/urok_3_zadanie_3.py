
def myfync(c,d,e):
        return sum((c,d,e)) - min(c,d,e)

print(f"{myfync(c=int(input('Enter c:')), d=int(input('Enter d: ')), e=int(input('Enter e: ')))}")
