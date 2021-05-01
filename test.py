import pyupbit

access = "oo"          # 본인 값으로 변경
secret = "oo"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-QKC"))     # KRW-QKC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
