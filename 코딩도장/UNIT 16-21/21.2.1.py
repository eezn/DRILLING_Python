import turtle as t

angle = int(input())
t.shape('turtle')
t.color('#1fc4ae')

t.begin_fill()
for i in range(angle):
    t.forward(50)
    t.right(360/angle)
t.end_fill()