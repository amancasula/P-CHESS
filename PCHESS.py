#!/usr/bin/env python3

import sys

print("WELCOME TO PCHESS!")


#board initialization
board=[[0 for i in range(10)] for j in range(8)]
#initialize players
for i in range(1,9):
  board[0][i]=1
  board[7][i]=2
  

#display board
def display():
  print("----------------------------")
  for i in board:
    print(i[1:9])
  print("----------------------------")


def gameup():
  one=0
  two=0
  for i in range(0,8):
    for j in range(0,10):
      if board[i][j]==1:
        one+=1
      elif board[i][j]==2:
        two+=1
   
  if one==two:
    print("DRAW MATCH!")
  elif one > two:
    print("PLAYER ONE WINS!") 
  else:
    print("PLAYER TWO WINS!")
  sys.exit(0)





#player1
def play1():
  def forward(move2,move1):
    if move2==7:
      print("INVALID MOVE")
      play1()
    else:
      if  board[move2+1][move1]==0 and board[move2+1][move1-1]!=oppo and  board[move2+1][move1+1]!=oppo:
        board[move2+1][move1]=player
        board[move2][move1]=0
      
      elif board[move2+1][move1]!=0 and board[move2+1][move1-1]==oppo and  board[move2+1][move1+1]!=oppo:
        board[move2+1][move1-1]=player
        board[move2][move1]=0
      
      elif board[move2+1][move1]!=0 and board[move2+1][move1-1]!=oppo and  board[move2+1][move1+1]==oppo:
        board[move2+1][move1+1]=player
        board[move2][move1]=0
      
      elif board[move2+1][move1]!=0 and board[move2+1][move1-1]==oppo and  board[move2+1][move1+1]==oppo:
        res1=input("Which pawn do you want to kill?(L/R)")
        if res1=="L":
          board[move2+1][move1-1]=player
          board[move2][move1]=0
        elif res1=="R":
          board[move2+1][move1+1]=player
          board[move2][move1]=0
      
      elif board[move2+1][move1]==0 and board[move2+1][move1-1]==oppo and  board[move2+1][move1+1]!=oppo:
        res1=input("Do you want to kill or move forward?(K/F)")
        if res1=="K":
          board[move2+1][move1-1]=player
          board[move2][move1]=0
        elif res1=="F":
          board[move2+1][move1]=player
          board[move2][move1]=0
      
      elif board[move2+1][move1]==0 and board[move2+1][move1-1]!=oppo and  board[move2+1][move1+1]==oppo:
        res1=input("Do you want to kill or move forward?(K/F)")
        if res1=="K":
          board[move2+1][move1+1]=player
          board[move2][move1]=0
        elif res1=="F":
          board[move2+1][move1]=player
          board[move2][move1]=0 
      
      elif board[move2+1][move1]==0 and board[move2+1][move1-1]==oppo and  board[move2+1][move1+1]==oppo:
        res1=input("Do you want to kill or move forward?(K/F)")
        if res1=="K":
          res2=input("Which pawn do you want to kill?(L/R)")
          if res2=="L":
            board[move2+1][move1-1]=player
            board[move2][move1]=0
          elif res2=="R":
            board[move2+1][move1+1]=player
            board[move2][move1]=0           
        elif res1=="F":
          board[move2+1][move1]=player
          board[move2][move1]=0 
        else:
          print("INVALID MOVE")
          play1()
  

  player=1
  oppo=2
  pieces=0
  counter=0
 
    
    #stop case
  
  for i in range(0,8):
    for j in range(0,10):
      if board[i][j]==player:
        pieces+=1
        if i==7:
          counter+=1
        else:
          if board[i+1][j]!=0 and board[i+1][j-1]!=oppo and board[i+1][j+1]!=oppo:
            counter+=1
            
  if pieces==counter:
      gameup()
  #take input          
  incol=[]
  move1=int(input("player:"+str(player)+">>>Enter move:"))
    
  for i in range(0,8):
    if board[i][move1]==player:
      incol.append(i)
        
  if len(incol) ==0:
    print("INVALID MOVE")
    play1()
  
  elif len(incol) ==1:
    move2=incol[0]
    forward(move2,move1)

  elif len(incol) > 1:
    print(incol)
    move2=int(input("Choose a pawn to move:"))  
    forward(move2,move1)
    
  
  

  display()
  play2()

 

#player2
def play2():
  def forward(move2,move1):
    if move2==0:
      print("INVALID MOVE")
      play2()
    else:
      if  board[move2-1][move1]==0 and board[move2-1][move1-1]!=oppo and  board[move2-1][move1+1]!=oppo:
        board[move2-1][move1]=player
        board[move2][move1]=0
      
      elif board[move2-1][move1]!=0 and board[move2-1][move1-1]==oppo and  board[move2-1][move1+1]!=oppo:
        board[move2-1][move1-1]=player
        board[move2][move1]=0
      
      elif board[move2-1][move1]!=0 and board[move2-1][move1-1]!=oppo and  board[move2-1][move1+1]==oppo:
        board[move2-1][move1+1]=player
        board[move2][move1]=0
      
      elif board[move2-1][move1]!=0 and board[move2-1][move1-1]==oppo and  board[move2-1][move1+1]==oppo:
        res1=input("Which pawn do you want to kill?(L/R)")
        if res1=="L":
          board[move2-1][move1-1]=player
          board[move2][move1]=0
        elif res1=="R":
          board[move2-1][move1+1]=player
          board[move2][move1]=0
      
      elif board[move2-1][move1]==0 and board[move2-1][move1-1]==oppo and  board[move2-1][move1+1]!=oppo:
        res1=input("Do you want to kill or move forward?(K/F)")
        if res1=="K":
          board[move2-1][move1-1]=player
          board[move2][move1]=0
        elif res1=="F":
          board[move2-1][move1]=player
          board[move2][move1]=0
      
      elif board[move2-1][move1]==0 and board[move2-1][move1-1]!=oppo and  board[move2-1][move1+1]==oppo:
        res1=input("Do you want to kill or move forward?(K/F)")
        if res1=="K":
          board[move2-1][move1+1]=player
          board[move2][move1]=0
        elif res1=="F":
          board[move2-1][move1]=player
          board[move2][move1]=0 
      
      elif board[move2-1][move1]==0 and board[move2-1][move1-1]==oppo and  board[move2-1][move1+1]==oppo:
        res1=input("Do you want to kill or move forward?(K/F)")
        if res1=="K":
          res2=input("Which pawn do you want to kill?(L/R)")
          if res2=="L":
            board[move2-1][move1-1]=player
            board[move2][move1]=0
          elif res2=="R":
            board[move2-1][move1+1]=player
            board[move2][move1]=0           
        elif res1=="F":
          board[move2-1][move1]=player
          board[move2][move1]=0 
        else:
          print("INVALID MOVE")
          play2()

  

  player=2
  oppo=1
  pieces=0
  counter=0
 
    
    #stop case
  for i in range(0,8):
    for j in range(0,10):
      if board[i][j]==player:
        pieces+=1
        if i==0:
          counter+=1
        else:
          if board[i-1][j]!=0 and board[i-1][j-1]!=oppo and board[i-1][j+1]!=oppo:
            counter+=1
            
  if pieces==counter:
      gameup()           
    
  #take input          
  incol=[]
  move1=int(input("player:"+str(player)+">>>Enter move:"))
    
  for i in range(0,8):
    if board[i][move1]==player:
      incol.append(i)
        
  if len(incol) ==0:
    print("INVALID MOVE")
    play2()
  
  elif len(incol) ==1:
    move2=incol[0]
    
    forward(move2,move1)

  elif len(incol) > 1:
    print(incol)
    move2=int(input("Choose a pawn to move:"))  
    forward(move2,move1)
    
  
  
  display()
  play1()
  
display()
play1()

      
