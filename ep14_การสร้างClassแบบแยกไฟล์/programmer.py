from employee import Employee

class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departmentName)
        self.__exp = experience
        self.__skill = skill
        # super()._showData
    def _showData(self):
        # print("ชื่อพนักงาน = "+self.__name)
        # print("เงินเดือน = ",format(self.__salary))
        # print("ตำแหน่ง = "+self._department)
        super()._showData()
        print("ประสบการณ์ = "+str(self.__exp))
        print("ทักษะ = "+self.__skill)
        # print("กำหนดคุณสมบัติเรียบร้อย")
        
    def __str__(self):
        return (super().__str__()+" , ประสบการณ์ = {} ปี, ทักษะ = {} ".format(self.__exp,self.__skill))