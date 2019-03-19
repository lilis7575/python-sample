# https://wikidocs.net/1418


print('값을 구할 최대값 입력 ::')
max = input()
arr = []
for i in range(int(max)):
    if i==0:
        pass
    elif i % 3 == 0 or i % 5 == 0:
        arr.append(i)
    else:
        pass

print("{max} 미만의 자연수에서 3과 5의 배수를 구하면 {arr} 이다. 이들의 총합은 {sum} 이다.".format(max=max, arr=arr, sum=sum(arr)))


