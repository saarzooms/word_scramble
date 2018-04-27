import random
def scramble(text):
     return ''.join(random.sample(text,len(text)))
f= open("test1.txt","r")
f_out = open("output.txt",'w')
data =  f.read()
token = data.split(' ')
for t in token:
    if len(t) > 3:
         if t[-1:]=='!' or t[-1:]=='?' or t[-1:]==',' or t[-1:]=='.' or t[-1:]==';':
            s = t[1:-2]
            s = scramble(s)
            s = t[0] + s + t[-2:]
            f_out.write(s + ' ')
         else :
            s = t[1:-1]
            s = scramble(s)
            s = t[0] + s + t[-1:]
            f_out.write(s + ' ')
     else:
          f_out.write(t +' ')

f.close()
f_out.close()
