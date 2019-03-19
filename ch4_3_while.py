# while문
import keyboard


state = True
while state:
    print('당신은 누구십니까?')
    your_name = input()
    if your_name == '도깨비':
        print('안녕하세요. 도깨비님!')
    elif your_name == '저승사자':
        print('저승사자님, 또 야근이시군요!')
    elif your_name == "패스":
        continue
    elif your_name == "끝":
        break
        state = False
    elif keyboard.is_pressed('a') :
        break
    else:
        print(your_name + '..., 뉘신지?')
    print()


# while True:#making a loop
#     try: #used try so that if user pressed other than the given key error will not be shown
#      if keyboard.is_pressed('a'): #if key 'a' is pressed
#       print('You Pressed A Key!')
#       break #finishing the loop
#      else:
#       pass
#     except:
#      break #if user pressed other than the given key the loop will break