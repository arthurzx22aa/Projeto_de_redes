def calc(num1, num2, operation):
    
    if operation == "+":
        return num1 + num2
    
    elif operation == "-":
        return num1 - num2
    
    elif operation == "*":
        return num1 * num2
    
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Divisão por zero não é permitida"
        
    else:
        return "operação inválida"