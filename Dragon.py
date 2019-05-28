import turtle

wn = turtle.Screen()
#wn.tracer(0, 0)

tim = turtle.Turtle()
tim.ht()
tim.speed(0)

li = [True]

for x in range(13):
    inverse = []

    for x in range(len(li) - 1, -1, -1): # Funky, eh? Goes through backwards.
        inverse += [not li[x]] # Also funky, eh? Maximum practicality!

    li += [False] + inverse

for x in li:
    tim.fd(3)
    
    if x:
        tim.rt(90)
    else:
        tim.lt(90)
    
    wn.update()
