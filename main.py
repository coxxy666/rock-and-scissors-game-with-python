import random


user_choose = input ('choose 0 for scissors ,1 for rock and 2 for paper : '  )

user_choose_int = int(user_choose)

print(user_choose_int)

computer_time = random.randint(0,2)

print(computer_time)

if computer_time == 0 and user_choose_int == 2 :

    print('You won')

elif computer_time == 1 and user_choose_int == 0 : 

     print('You won')

elif computer_time == 2 and user_choose_int == 1 : 

     print('You won')


elif computer_time == 1 and user_choose_int == 1 : 

     print('Draw')

elif computer_time == 0 and user_choose_int == 0 : 

     print('Draw')
elif computer_time == 2 and user_choose_int == 2 : 

     print('Draw')


else :

    print('You lose')



