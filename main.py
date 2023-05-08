cesar= lambda message, roundVal: print(''.join(chr(ord(i)+roundVal) for i in message))
cesar("Hello Friend", 8)