
print('Hi, welcome to this test quiz thing')
print('Try to get as many questions correct as possible...')

totalQuestions = 4
score = 0
cr = 'Correct'
incr = 'Incorrect'

ans = input('1. Question 1 ')

if ans.lower() == '1':
    print(cr)
    score += 1
else:
    print(incr)


ans = input('2. Question 2 ')

if ans == "2":
    print(cr)
    score += 1
else:
    print(incr)


ans = input('3. Question 3 ')

if ans.lower() == "3":
    print(cr)
    score += 1
else:
    print(incr)


ans = input('4. Question 4 ')

if ans.lower() == "4":
    print(cr)
    score += 1
else:
    print(incr)


print("Thank you for playing, you got " + str(score) + ' questions correct!' )
percent = (score/totalQuestions) * 100
print("Mark: " + str(int(percent)) + '%')

if percent >= 50:
    print('Nice! You passed!')
else:
    print('Better luck next time')
