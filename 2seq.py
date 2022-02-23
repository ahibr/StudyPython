input_str = input()
# print(input_str)
result_str = [] 
end_str = []  
for i in range(0, len(input_str)): 
  if input_str[i] != ",": 
    # print(input_str[i])
    result_str.append(input_str[i])
print (result_str)
result_str=set(result_str)
print(result_str)
