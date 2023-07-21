def block():
    t.fillcolor('gray')
    t.begin_fill()
    for k in range(2):
        t.forward(200)
        t.right(90)
        t.forward(150)
        t.right(90)
    t.end_fill() 
def mai_nha():
    t.begin_fill()
    t.fillcolor('red')
    t.left(30)
    for k in range(2):
        t.forward(120)
        t.right(62)
    t.end_fill()