# codewars problems
n = 348597
def digitize(n):
    result = []
    number_string = str(n)
    for i in number_string:
        i = int(i)
        result.append(i)
    return result[::-1]
print (digitize(n))

