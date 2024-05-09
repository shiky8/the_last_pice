#!/bin/env python3
import base64 
from math import sqrt
import json
from collections import OrderedDict
import random



class LastPice:

	#encode
	def encode(plane_text):
		plane_text_ascii = [ ord(ch) for ch in plane_text]

		# print(f"accii = {plane_text_ascii}")
		music_genre ={"":[],}
		c = 70
		key = []
		cipher_list = []

		path_to_file = "gnera_last_pice.json";

		with open(path_to_file) as data_file:
			data = OrderedDict(json.load(data_file))
		#y^2 = x^2 + c
		for x in plane_text_ascii:
			y =  (pow(x,2))+c
			# y =  int(sqrt(y))
			w = y%131
			if w > 124:	w = 124
			# print(w)
			cipher_list.append(random.choice(list(data["genre"].values())[w])) 
			key.append(y)
		key = base64.b64encode(json.dumps(key).encode("ascii") )
		return key,cipher_list

	#decode
	def decode(key,cipher):
		key = json.loads(base64.b64decode(key))
		# print(f"key decode = {key}")
		plane_text_list = []
		# c = 25
		#x^2 = y^2 - c
		index = 0
		path_to_file = "gnera_last_pice.json";

		with open(path_to_file) as data_file:
			data = OrderedDict(json.load(data_file))
		for y in key:
			# x =  pow(y,2)-c
			x =  int(sqrt(y))
			if x == 33:	x = x-1
			elif x == 34:	x = x-1 
			elif x == 35:	x = x-1 
			# print(f"plane_text = {x}")
			w = y%131
			if w > 124:	w = 124
			if not (cipher[index] in list(data["genre"].values())[w]):
				return "stop brute-forcing"
			index = index + 1
			plane_text_list.append(chr(x))
		# print(f"len of key = {len(key)}, len of x = {len(plane_text_list)}, len of cipher = {len(cipher)}")



		plane_text = "".join(plane_text_list)
		return plane_text

if __name__=="__main__":
	# plane_text = "asdfghjklzxcvbnmqwertyuiop ASDFGHJKLZXCVBNMQWERTYUIOP 0123456789 10 22 /\"\\!<?:;'[]{}!@#$%^&*() "

	plane_text = "hi  "

	print(f"before plane_text = {plane_text}\n")
	key,cipher = LastPice.encode(plane_text)

	print(f"key = {key} , \n\ncipher = {cipher}\n")
	# cipher =  ['kkop47', 'ss64', 'ss114', 'ss124', 'kkop68', 'kkop13', 'kkop40', 'kkop122', 'ss75', 'kkop20', 'ss60', 'kkop46', 'ss108', 'kkop111', 'ss118', 'ss30', 'ss1', 'kkop83', 'kkop53', 'kkop97', 'ss33', 'kkop39', 'kkop4', 'ss91', 'ss77', 'ss38', 'ss46', 'kkop103', 'kkop16', 'kkop109', 'ss123', 'ss2', 'ss14', 'ss44', 'ss62', 'ss82', 'kkop48', 'kkop85', 'kkop105', 'ss124', 'kkop103', 'ss124', 'kkop104', 'ss81', 'kkop41', 'ss115', 'ss113', 'kkop52', 'ss0', 'ss90', 'kkop28', 'ss23', 'kkop51', 'kkop46', 'ss16', 'ss113', 'kkop81', 'ss51', 'ss23', 'kkop124', 'ss104', 'kkop82', 'kkop62', 'ss44', 'kkop46', 'kkop113', 'ss16', 'kkop46', 'ss81', 'kkop81', 'ss46', 'ss52', 'ss47', 'ss19', 'kkop111', 'kkop2', 'ss109', 'kkop28', 'ss14', 'kkop19', 'ss98', 'kkop73', 'ss3', 'kkop106', 'kkop111', 'ss105', 'ss116', 'kkop56', 'kkop124', 'ss124', 'kkop73', 'ss0', 'ss98', 'kkop48', 'ss46']
	
	# cipher = str(cipher)
	
	
	# cipher = cipher.split(',')
	# print(cipher)
	# cipher = cipher.split(',')
	# cipher = list(cipher)
	# print(cipher)
	plane_text = LastPice.decode(key,cipher)
	print(f"plane_text = {plane_text}")