#print("Hello World!")
print("Good-bye World!")

fname = input("Enter your file name: ") 
msg = input("Enter your message: ")

f = open("/home/ec2-user/environment/NSC-AWS/STARTraq/ {} .txt".format(fname), "x")
f.write(msg)
f.close()

f = open("/home/ec2-user/environment/NSC-AWS/STARTraq/ {} .txt".format(fname), "r")
print(f.read())
f.close()


#>>> shepherd = "Mary"
#>>> age = 32
#>>> stuff_in_string = "Shepherd {} is {} years old.".format(shepherd, age)