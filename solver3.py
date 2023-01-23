dict_date = {}
dict_ping = {}
N = 2
m = 3 #パラメータ。あるIPアドレスの直近 ”m” 回あたりの平均応答時間を求めるために使用
t = 5 #パラメータ。あるIPアドレスの平均応答時間が"t"を超えたときに過負荷とみなす
while True:
	try:
		date,address,ping = map(str,input().split(","))
		year = date[0:4]
		month = date[4:6]
		day = date[6:8]
		hour = date[8:10]
		minute = date[10:12]
		second = date[12:14]
		date = str(year)+"年"+str(month)+"月"+str(day)+"日"+str(hour)+"時"+str(minute)+"分"+str(second)+"秒"

		if ping == "-":#タイムアウトしている場合
			dict_date[address] = [date]
			dict_ping[address] = [0]*m #予め長さmの配列を用意

		else:#タイムアウトしていない場合
			if address not in dict_date.keys():
				dict_ping[address] = [0]*m #予め長さmの配列を用意
				dict_ping[address].pop(0) #先頭要素を取り除く
				dict_ping[address].append(int(ping)) #一番後ろに応答時間を追加
				dict_date[address] = [date]
			else:
				dict_date[address].append(date)
				dict_ping[address].pop(0)
				dict_ping[address].append(int(ping))
			if sum(dict_ping[address]) >= m*t: #あるアドレスの合計応答時間がm*t(=平均応答時間がt)以上の時
				print("過負荷サーバー "+str(address)+" 過負荷期間"+str(dict_date[address][0])+"~"+str(date))
	except EOFError:
		break
