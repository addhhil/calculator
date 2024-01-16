

user_input="{}()[]"

bracket_pairs={

    "{":"}",
    "(":")",
    "[":"]",
    "<":">"
}

top=-1
symbol_stack=[]

for symbol in user_input:#symbol=}
    if symbol in bracket_pairs:
        symbol_stack.append(symbol)
        top+=1
    else:
        current_symbol=symbol_stack[top]#{
        current_symbol_closing=bracket_pairs.get(current_symbol)
        if symbol==current_symbol_closing:
            symbol_stack.pop()
            top=top-1
        else:
            print("invaid")
            break
if len(symbol_stack)==0:
    print("valid")