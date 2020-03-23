def likes(names):
    text = ""
    last_elem = len(names)-1
    
    if not names:
        return "no one likes this"
    
    if len(names) == 1:
        return names[0] + " likes this"
    
    for i, name in enumerate(names):
        if last_elem < 3:
            if i == last_elem:
                text = text + " and " + name + " like this"
            elif i:
                text = text + ", " + name
            else:
                text = name
        else:
            total = last_elem-1
            return names[0] + ", " + names[1] + " and " + str(total) + " others like this"


    return text