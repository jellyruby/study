import turtle as t 


t.shape("turtle")
t.color("blue")    #문제의 요구사항에 따라 선 색 변경

# 정다각형을 그린다.
def make_regular_Polygon(t, angle,length):
    def make_line(t):
        t.forward(length)
        t.right(360/angle)

    for i in range(1,abs(angle)+1):
        make_line(t)





make_regular_Polygon(t,4,150)


