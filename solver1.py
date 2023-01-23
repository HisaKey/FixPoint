dict = {} #IPアドレスを保管するための辞書(IP:キー 日付:値)
while True:
  try:
    date,IP,ping = map(str,input().split(","))
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    hour = date[8:10]
    minute = date[10:12]
    second = date[12:14]
#    print(year,month,day,hour,minute,second)
    date = str(year)+"年"+str(month)+"月"+str(day)+"日"+str(hour)+"時"+str(minute)+"分"+str(second)+"秒"#日時をYYYYMMDD~からYYYY年MM月DD日~に変更している
    if IP not in dict.keys() and ping == "-":
      dict[IP] = date #あるIPアドレスが初めてタイムアウトしたときに辞書にIPと日時を挿入
    elif IP in dict.keys() and ping != "-":
        print("故障IP "+str(IP)+" 故障期間 "+str(dict[IP])+"~"+str(date))#タイムアウトしたIPが復旧したときの故障IPとタイムアウトした日時、そして復旧した時の日時を出力
        dict.pop(IP)#出力したIPを辞書からとりのぞく
  except EOFError:
    break
#print(dict)
