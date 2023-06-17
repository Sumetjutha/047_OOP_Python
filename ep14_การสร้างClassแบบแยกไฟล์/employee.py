class Employee: # การสร้าง class ควรเป็นตัวพิมพ์ใหญ่ตัวแรก
    ## class variable
    __minSalary = 12000
    maxSalary = 50000
    companyName = "SCTGOLD"

    def __init__(self,name,salary,department):
        # protected attribute
        self.__name = name
        self.__salary = salary
        self._department = department
    
    # protected method
    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = "+self._department)
        # print("กำหนดคุณสมบัติเรียบร้อย")
    
    # รายได้ต่อปี 
    # def _getIncome(self):
    #     return self.__salary * 12
    def _getIncome(self,bonus=0,overtime=0):
        return (self.__salary * 12)+bonus+overtime
    
    def __str__(self):
        return ("ชื่อพนักงาน = {}, แผนก = {}, เงินเดือน = {}".format(self.__name,self._department,self.__salary))