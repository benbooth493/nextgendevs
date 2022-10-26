def say(s):
    print(s)


say('hello world')
say('How are you?')

def sum(a, b):
    print(a + b)

sum(10, 12)
sum(4, 2)


def divide(a, b):
    return a / b

result = divide(4, 2)

if result == 2:
    print(result)


def error_msg(n):
    if n == 0:
        return 'ErrNoFileExists'
    if n == 1:
        return 'ErrNoDirectoryExists'

        
print(error_msg(0))
print(error_msg(1))