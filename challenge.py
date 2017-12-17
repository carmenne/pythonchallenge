s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

s_l = list(s)
s_l_replaced = []

for el in s_l:
	if el == 'y':
		s_l_replaced.append('a')
	elif el == 'z':
		s_l_replaced.append('b')
	elif ord(el)>= ord('a'):
		s_l_replaced.append(chr(ord(el) + 2))
	else:
		s_l_replaced.append(el)

print("".join(s_l_replaced))


