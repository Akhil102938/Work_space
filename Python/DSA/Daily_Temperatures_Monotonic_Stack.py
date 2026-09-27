def dailyTemperatures(temperatures):
n = len(temperatures)
answer = [0] * n
stack = []

for i in range(n):  
    current_temp = temperatures[i]  

      
    while len(stack) > 0 and temperatures[stack[-1]] < current_temp:  
        previous_day = stack.pop()  
        answer[previous_day] = i - previous_day  

    stack.append(i)  

return answer

temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temps))
