cgpa=float(input())
backlog=int(input())
skill=input()
if cgpa>8.5:
    if backlog<2:
        if skill=='python':
            print('congralations ur selected')
        else:
            print('learn python')
    else:
        print('clear backlogs')
else:
    print('cgpa is less')