def split_it(seq):
    first_string = ""
    sec_string = ""
    for elem in seq:
        if elem.islower() or elem == "_" or elem == ".":
            first_string += elem
        elif elem.isupper() or elem == " " or elem == "|":
            sec_string += elem
    return (first_string,sec_string)

def split_rec(seq):
    first_string = ""
    sec_string = ""

    if not seq:
        return ("","")
    
    elif seq[0].islower() or seq[0] == "_" or seq[0] == ".":
        new_tuple = split_rec(seq[1:])
        first_string = seq[0] + new_tuple[0]
        sec_string = new_tuple[1]

        return (first_string,sec_string)


    elif seq[0].isupper() or seq[0] == " " or seq[0] == "|":      
        new_tuple = split_rec(seq[1:])
        first_string = new_tuple[0]
        sec_string = seq[0] + new_tuple[1]

        return (first_string,sec_string)    
    
    else:
        new_tuple = split_rec(seq[1:])
        first_string = new_tuple[0]
        sec_string =  new_tuple[1]

    return (first_string,sec_string)




def interpret(expression,dict):
    if isinstance(expression,str):
        if expression in dict:
            return dict[expression]
        elif expression == "true" or "false":
            return expression
        
    elif len(expression) == 2:
        if interpret(expression[1],dict) == "true":
            return "false"
        else:
            return "true"
        
    elif expression[1] == "AND":
        if interpret(expression[0],dict) == "true" and interpret(expression[2],dict) == "true":
            return "true"
        else:
            return "false"
        
    elif expression[1] == "OR":
        if interpret(expression[0],dict) == "true" or interpret(expression[2],dict) == "true":
            return "true"
        else:
            return "false"
 