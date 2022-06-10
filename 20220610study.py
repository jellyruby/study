from functools import reduce

#limit 값 이상의 list만 반환하는 함수
def get_limit_over(arr,limit):
    return list(filter(lambda x : int(x) > limit , arr))

#평균을 구하는 함수
def get_average(arr):
    return reduce(lambda x, y : int(x)+int(y) , arr)/len(arr)

#성적을 설정하는 함수
def set_grade(length):
    return list(map(lambda x : input("성적을 입력하세요:"),[0 for x in range(length)]))


grade = set_grade(5)
print("성적 평균은 ", get_average(grade), "입니다.")
print("80점 이상 성적을 받은 학생 수는 ", len(get_limit_over(grade,80)), "입니다.")

