# def bracketMatch(string):
#
#     open_counter = 0
#     close_counter = 0
#     for bracket in string:
#         if bracket == ')' and open_counter <= 0:
#             close_counter += 1
#         elif bracket == ')':
#             open_counter -= 1
#         elif bracket == '(':
#             open_counter += 1
#     return open_counter + close_counter


def bracketMatch(string):

    open_counter = 0
    close_counter = 0
    for bracket in string:
        if bracket == '(':
            open_counter += 1
        elif bracket == ')':
            open_counter -= 1
        if open_counter < 0:
            open_counter += 1
            close_counter += 1
    return open_counter + close_counter

print bracketMatch("()))(")  #1
print bracketMatch("(())") #0
print bracketMatch("())(") #2