#print("Hello World!")
print("Good-bye World!")

f = open("/home/ec2-user/environment/NSC-AWS/STARTraq/frog.txt", "x")
f.write("Ribbit!")
f.close()

f = open("/home/ec2-user/environment/NSC-AWS/STARTraq/frog.txt", "r")
print(f.read())
f.close()