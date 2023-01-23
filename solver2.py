dict = {}
N = 3 #パラメータ N回以上タイムアウトしたときに故障とみなす
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
    
    if ping == "-" and address not in dict.keys():
      dict[address] = [date]
    elif ping == "-" and address in dict.keys():
        dict[address].append(date) #solver.pyからの変更点 一度タイムアウトしたアドレスが再びタイムアウトしたときに日時を追加している。
    elif ping != "-" and address in dict.keys():
        dict[address].append(date)
        if len(dict[address]) > N:
#solver.pyからの変更点 あるアドレスが復旧したときに、そのアドレスの値の要素がN+1個以上(=N回以上タイムアウト)しているときに先頭の日時を出力
            print("故障IP "+str(address)+" 故障期間 "+str(dict[address][0])+"~"+str(date))
        dict.pop(address)
  except EOFError:
    break
