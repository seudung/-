import pyupbit

access = "oIEH7JUxtFDPsgYqdSxAjKymQad5Dau3mr81yrrA"          # 본인 값으로 변경
secret = "2op4XxzEyt4uWUj0A2JsDyzvslvK8h9vyyJVNJrQ"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-QKC"))     # KRW-QKC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회