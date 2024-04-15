def analyze_var(var):
    match var:
        case list():
            print('List')
        case tuple():
            print('Tuple')
        case set():
            print('Set')
        case dict():
            print('Dictionary')
        case _:
            print('Other')

print(analyze_var([3]))
print(analyze_var((5)))
print(analyze_var({6}))
print(analyze_var({'key':6}))            
     
    
        