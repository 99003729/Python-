s=input()
s_new = s.split(" ")
s_new2 = str(s_new[0].split())
s_new3 = str(s_new[1].split())
s_new2 = list(s_new2)
s_new3 = list(s_new3)
s_new4 = s_new2[2].upper()
s_new2.replace(s_new2[2],s_new4)
s_new5 = s_new3[2].upper()
s_new3.replace(s_new3[2],s_new5)
ss = s+s2
s_final = " ".join(ss)
print(s_new)
print(s_new2)
print(s_new3)
print(s_final)
"""
s_new2 = s_new[0].split()
s_new3 = s_new[1].split()
s_new4 = s_new2[0].upper()
s_new5 = s_new3[0].upper()
s = "".join(s_new4)
s2 = "".join(s_new5)
ss = s+s2
s_final = " ".join(ss)
"""