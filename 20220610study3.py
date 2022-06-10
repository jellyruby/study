import turtle as t 


t.shape("turtle")

t.bgcolor("black")  #문제의 요구사항에 따라 백그라운드 컬러 변경
t.color("green")    
t.speed(100)        #문제의 요구사항에 따라 빠르게하기
for x in range(10):
    t.circle(100)   #원 크기 100으로 그리기
    t.forward(10)   #앞으로나아가면서 그림
