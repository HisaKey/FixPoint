dict = {}
N = 2
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
    IP = address.split("/")[0]#アドレスをIPとサブネットに分解
    subnet = address.split("/")[1]
    
    if ping == "-":
      dict[subnet] = [date]#solver1~3.pyまでと異なり、辞書のキーにサブネットを使用
      
    elif subnet in dict.keys() and ping != "-":
        dict[subnet].append(date)
        if len(dict[subnet]) >= N:
            print("故障サブネット "+str(subnet)+" 故障期間 "+str(dict[subnet][0])+"~"+str(dict[subnet][-1]))
            dict.pop(subnet)

  except EOFError:
    break
