#学習1
num_1 = input("num_1 =>")
num_2 = input("num_2 =>")
ans = int(num_1) + int(num_2)

#完成イメージから分解して考えて書くと良い
#(完成形)num_1(10)+num_2(20)=30
#num_1(      文字部分
#10          代入部分
#)+num_2(    文字部分
#20          代入部分
#)=          文字部分
#30          代入部分

print("num_1("+str(num_1)+")+num_2("+str(num_2)+")="+str(ans))

msg_ans = "num_1({index0})+num_2({index1})={index2}".format(index0=num_1,index1=num_2,index2=ans)