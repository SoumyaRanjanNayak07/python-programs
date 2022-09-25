#program to generates the numbers which are divisible by 7 but are not a multiple of 5 ,between 2000 to 3200(both incliuded) .print these numbers in comma separated form.

# so here we have to consider that divisible of 7 but not a multiple of 5 then we do find all these numbers between 2000 and 3200 .ok let's start 
 
 #here we know that both are included so here taking a range function and 3200+1 for not excluded 3200.
  
 #if statement to check the condition of divisible of 7 and not multiple of 5
 # and at last this end="," means to print these numbers in one line 
 # so thank you guys do like and subscribe my channel comment out how's it thanks guys 

start=int(input("Enter the start number from where you want to test the condition:"))
end=int(input("Enter the end number from where you want to test the condition:"))
for i in range(start,end):
    if i%7==0 and i%5!=0:
        print(i,end=",")

