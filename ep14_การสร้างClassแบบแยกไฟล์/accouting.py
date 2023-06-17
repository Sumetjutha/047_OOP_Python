from employee import Employee

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)
        self.__age = age
        # super()._showData
    def _showData(self):
        # print("ชื่อพนักงาน = "+self.__name)
        # print("เงินเดือน = ",format(self.__salary))
        # print("ตำแหน่ง = "+self._department)
        super()._showData()
        print("อายุ = "+str(self.__age))
        # print("กำหนดคุณสมบัติเรียบร้อย")
    
    def __str__(self):
        return (super().__str__()+" , อายุ = {} ปี".format(self.__age))    