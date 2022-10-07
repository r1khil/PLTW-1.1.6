#   a116_buggy_image.py
from operator import le
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used


# create a spiderBody
spiderBody = trtl.Turtle()
spiderBody.pensize(40)
spiderBody.circle(20)

# configure the spider legs
legCount = 8
legLength = 90
legAngle = 180 / legCount
spiderBody.pensize(5)
spiderLeg = 0

# draw the spider legs

while (spiderLeg < legCount):
  spiderBody.goto(0,20)
  spiderBody.setheading(legAngle*spiderLeg - 30)
  spiderBody.setheading(legAngle*spiderLeg + 30)
  spiderBody.forward(legLength)
  spiderLeg = spiderLeg + 1

spiderBody.penup()

spiderBody.goto(0,-30)
spiderBody.pendown()
spiderBody.pensize(30)
spiderBody.circle(10)

spiderBody.goto(15,-30)
spiderBody.color("white")
spiderBody.pensize(5)
spiderBody.stamp()

spiderBody.penup()

spiderBody.goto(-20,-30)
spiderBody.pendown()
spiderBody.stamp()

spiderBody.hideturtle()



wn = trtl.Screen()
wn.mainloop()