account = Accounting("มีนา",20000,24)
print(account.__str__())
print("แผนกบัญชี รายได้ต่อปีรวมโบนัส + OT = "+str(account._getIncome(5000,500))+" บาท")
print("###############")

programmer = Programmar("ติ๊ก",60000,3,"All Data Skill")
print(programmer.__str__())
print("แผนกบัญชี รายได้ต่อปีรวมโบนัส + OT = "+str(programmer._getIncome(50000,500))+" บาท")
print("###############")

sale = Sale("เบล",30000,"ดินแดง")
print(sale.__str__())
print("แผนกบัญชี รายได้ต่อปีรวมโบนัส + OT = "+str(sale._getIncome(40000,500))+" บาท")
print("###############")