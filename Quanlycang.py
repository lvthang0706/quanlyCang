class HangHoa:
    def __init__(self, ten, trongLuong):
        self.ten = ten
        self.trongLuong = trongLuong
    def __str__(self):
        return f"Hang hoa: {self.ten}, Trong luong: {self.trongLuong}kg"
class Container(HangHoa):
    def __init__(self, ten, trongLuong, maContainer):
        super().__init__(ten, trongLuong)
        self.maContainer = maContainer
    def __str__(self):
        return f"Container {self.maContainer}: {self.ten}, Trong luong: {self.trongLuong}kg"
class ContainerDongLanh(Container):
    def __init__(self, ten, trongLuong, maContainer, nhietDo):
        super().__init__(ten, trongLuong, maContainer)
        self.nhietDo = nhietDo
    def __str__(self):
        return f"Container dong lanh {self.maContainer}: {self.ten}, Trong luong: {self.trongLuong}kg, Nhiet do: {self.nhietDo}°C"
class ContainerVatLieuNguyHiem(Container):
    def __init__(self, ten, trongLuong, maContainer, mucDoNguyHiem):
        super().__init__(ten, trongLuong, maContainer)
        self.mucDoNguyHiem = mucDoNguyHiem
    def __str__(self):
        return f"Container vat lieu nguy hiem {self.maContainer}: {self.ten}, Trong luong: {self.trongLuong}kg, Muc do nguy hiem: {self.mucDoNguyHiem}"
class Kho:
    def __init__(self):
        self.khoLuuTru = []
    def luuHangHoa(self, container):
        self.khoLuuTru.append(container)
        print(f"Luu tru vao kho: {container}")
    def xoaHangHoa(self, container):
        self.khoLuuTru.remove(container)
        print(f"Xoa khoi kho: {container}")
class Cang:
    def __init__(self):
        self.containerList = []
        self.khoList = []
    def themContainer(self, container):
        self.containerList.append(container)
        print(f"Them container vao cang: {container}")
    def xoaContainer(self, container):
        self.containerList.remove(container)
        print(f"Xoa container khoi cang: {container}")
    def themKho(self, kho):
        self.khoList.append(kho)
        print(f"Them kho vao cang.")
    def luuVaoKho(self, kho, container):
        kho.luuHangHoa(container)
        self.xoaContainer(container)
cang = Cang()
kho = Kho()
cang.themKho(kho)
container1 = ContainerDongLanh("Ca", 1000, "DL101", -18)
container2 = ContainerVatLieuNguyHiem("Hoa chat", 500, "VL201", 5)
cang.themContainer(container1)
cang.themContainer(container2)
cang.luuVaoKho(kho, container1)