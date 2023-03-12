#!/usr/bin/python3

def func(e):
  return len(e)
 
x=int(input())
vet=[]

for i in range(0,x):
  aux=input()
  vet.append(aux)

vet.sort(key=func)

for s in vet:
  print(s)
