class answer:
    def parentheses(self,line):
        if len(line)%2==1:
            print('Invalid')
        else:
            for i in range(0, len(line), 2):
                if line[i:i+2] not in ['()', '[]', '{}']:
                    print('Invalid')
                    break
            else:
                print('Valid')

string= str(input('Enter parentheses string: '))
for i in string:
    if i not in '(){}[]':
        string= str(input('Enter ONLY parentheses string: '))
        
answer().parentheses(string)
