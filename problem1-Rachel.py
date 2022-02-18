#
# Name:
# Collaborator(s):
#
secs=int(input("How many seconds? "))
totalsec=secs
days=secs//86400
secs-=days*86400
hr=secs//3600
secs-=hr*3600
mins=secs//60
secs-=mins*60
print(str(totalsec) + " seconds is equivalent to " + str(days) + " days, " + str(hr) + " hours, " + str(mins) +" minutes, and " + str(secs)+" seconds.")
