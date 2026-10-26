#Exam Result Report

name = input('Enter Student Name: ')
python_score = float(input('Enter Your Python score: '))
english_score = float(input('Enter Your English score: '))
maths_score = float(input('Enter your Mathematics score: '))
average_score = (python_score + english_score + maths_score)/3

print('==' *20)
print('             Student Result                ')
print('==' *20)
print(f'Student: {name}')
print(f'Python: {python_score}')
print(f'English: {english_score}')
print(f'Mathematics: {maths_score}')
print('--'*20)
print(f'Average: {average_score:.2f}')
print('==' *20)