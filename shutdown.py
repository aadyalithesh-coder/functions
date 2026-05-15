def shut_down(check):
    if check=="yes":
        return("shutting down")

    elif check=="no":
        return("aborting shutdown")

    else:
        return("sorry")
       
print(shut_down(input("did you close all apps(yes/no):")))
    