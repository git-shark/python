#学習1
num_1 = input("num_1 =>")
num_2 = input("num_2 =>")
ans = int(num_1) + int(num_2)
print("num_1("+str(num_1)+")+num_2("+str(num_2)+")="+str(ans))

#完成イメージから分解して考えて書くと良い
#num_1(10)+num_2(20)=30

print(
"num_1("
+str(num_1)+
")+num_2("
+str(num_2)+
")="
+str(ans)
)

msg_ans = "num_1({num_1})+num_2({num_2})={ans}".format(num_1=num_1,num_2=num_2,ans=ans)
print(msg_ans)
msg_ans = "num_1({key0})+num_2({key1})={key2}".format(key0=num_1,key1=num_2,key2=ans)
print(msg_ans)
