import numpy
num = input("임의의 정수를 입력해주세요")

total = numpy.prod ([i+1 for i in range(int(num))])

print(total);
