def laptop_user(turn_on,network,to_slow) :
    if turn_on == "NO":
        return "to check the power charger "
    elif network == "NO":
        return "to check the wifi networks "
    elif to_slow == "yes" :
        return " close the unused program and restart the laptop"
    else :
        return " no problem in the laptop"
turn_on = input("does the laptop turn on? yes/no:").lower()
network=input("does the laptop is working? yes/no:").lower()
to_slow=input("does the laptop is slow ? yes/no:").lower()

advice =laptop_user(turn_on,network,to_slow)
print(advice)
