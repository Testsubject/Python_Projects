from turtle import *

def square(T, S):
  for k in range(0,4):
    T.forward(S)
    T.left(110)

def repeat(T, f, N, A, S, k):
  for j in range(0, N):
    f(T, S)
    T.left(A)
    S = k*S

nicholas = Turtle()
nicholas.speed("fastest")
repeat(nicholas, square, 108, 10, 200, 0.97)

exitonclick()
