n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
for k in student_marks:
    if(k==query_name):
        v=student_marks[k]
        avg=sum(v)/3
        print('%.3f' % avg)
        break