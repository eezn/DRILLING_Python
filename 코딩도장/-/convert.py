NOTATION = '0123456789ABCDEF' 
def numeral_system(number, base): 
    q, r = divmod(number, base) 
    n = NOTATION[r] 
    return numeral_system(q, base) + n if q else n 
    
    
# 2진수 
result = numeral_system(4884, 3) 
# 4진수 
result1 = numeral_system(18, 2) 
# 11진수 
result2 = numeral_system(18, 11) 

print(result) 
print(result1) 
print(result2) 


