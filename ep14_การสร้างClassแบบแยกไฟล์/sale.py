from employee import Employee

class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName)
        self.__area = area
        # super()._showData
        
    def _showData(self):
        # print("ชื่อพนักงาน = "+self.__name)
        # print("เงินเดือน = ",format(self.__salary))
        # print("ตำแหน่ง = "+self._department)
        super()._showData()
        print("พื้นที่การขาย = "+self.__area)
        # print("กำหนดคุณสมบัติเรียบร้อย")
        
    def __str__(self):
        return (super().__str__()+"  , พื่นที่รับผิดชอบ = {}".format(self.__area))