n=int(input('>>>'))
def chisla(num):
    if num==1:
        print(1)
    else:
        chisla(num-1)
        print(num)
chisla(n)