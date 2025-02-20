def incoming(ch):
    if ch=='+' or '-':
        return 1
    if ch=='*' or '/' or '%':
        return 3
    if ch=='^':
        return 6
    if ch=='(':
        return 9
    if ch==')':
        return 0
    else:
        return 7
def in_stack(ch):
    if ch=='+' or '-':
        return 2
    if ch=='*' or '/' or '%':
        return 4
    if ch=='^':
        return 5
    if ch=='(':
        return 0
    if ch=='#':
        return -1
infix=input()