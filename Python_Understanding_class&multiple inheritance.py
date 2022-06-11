    # 클래스 Name과 Color의 값을 직접 입력하는 경우
# class Name:
#   def __init__(self,name):
#     self.name=name

#   def confirm(self):
#     print("\nName 클래스입니다.")
#     print("[멤버변수] name:{}".format(self.name))

# class Color:
#   def __init__(self,color):
#     self.color=color

#   def confirm(self):
#     print("\nColor 클래스입니다.")
#     print("[멤버변수] color:{}".format(self.color))    




    # 클래스 Name과 Color의 값이 고정된 경우
class Name:  
  def __init__(self):
    self.name="코스모스"
  def confirm(self):
    print("\nName 클래스입니다.")
    print("[멤버변수] name:{}".format(self.name))
  def action_Name(self):
    print("\nName 클래스 고유 메소드")
 
class Color:
  def __init__(self):
    self.color="화이트"
  def confirm(self):
    print("\nColor 클래스입니다.")
    print("[멤버변수] color:{}".format(self.color))    
  def action_Color(self):
    print("\nColor 클래스 고유 메소드")
    
class Num_Name1(Name):  # 기존 멤버변수(name만)는 상속받고 추가변수(num)만 입력해야 하는 경우
  def __init__(self,num):
    Name.__init__(self)
    self.num=num
  def confirm(self):
    print("\nNum_Name1 클래스입니다.")
    print("[멤버변수] num:{} name:{}".format(self.num,self.name))
  def action_Num_Name1(self):
    print("\nNum_Name1 클래스 고유 메소드")

class Num_Name2(Name):  # 기존 멤버변수(name만)상속받고 추가 변수(num)은 고정된 경우
  def __init__(self):
    Name.__init__(self)
    self.num=2
  def confirm(self):
    print("\nNum_Name2 클래스입니다.")
    print("[멤버변수] num:{} name:{}".format(self.num,self.name))
  def action_Num_Name2(self):
    print("\nNum_Name2 클래스 고유 메소드")

class Num_Name3(Name):  # 부모클래스(Name)로부터 메소드만 상속받고 기존 변수(name)과 추가 변수(num) 모두 입력해야하는 경우
  def __init__(self,num,name):
    Name.__init__(self)
    self.name=name
    self.num=num
  def confirm(self):
    print("\nNum_Name3 클래스입니다.")
    print("[멤버변수] num:{} name:{}".format(self.num,self.name))
  def action_Num_Name3(self):
    print("\nNum_Name3 클래스 고유 메소드")

class Name_Color1(Name,Color):  # 부모클래스(Name,Color)로부터 멤버변수값(name,color) 모두 상속받는 경우
  def __init__(self):
    Name.__init__(self)
    Color.__init__(self)
  def confirm(self):
    print("\nName_Color1 클래스입니다.")
    print("[멤버변수] name:{} color:{}".format(self.name,self.color))
  def action_Name_Color1(self):
    print("\nName_Color1 클래스 고유 메소드")
    
class Name_Color2(Name,Color):  # 부모클래스로부터 멤버변수값 모두 상속받지 않는경우(메소드는 상속받음)
  def __init__(self):
    Name.__init__(self)
    Color.__init__(self)
    self.name="장미"
    self.color="레드"
  def confirm(self):
    print("\nName_Color2 클래스입니다.")
    print("[멤버변수] name:{} color:{}".format(self.name,self.color))
  def action_Name_Color2(self):
    print("\nName_Color2 클래스 고유 메소드")

class NCSize1(Name_Color1):  # 부모클래스(Name_Color1)으로부터 멤버변수값 상속받고, 새로운 변수값(size)입력/추가
  def __init__(self,size):
    Name_Color1.__init__(self)
    self.size=size
  def confirm(self):
    print("\nNCSize1 클래스입니다.")
    print("[멤버변수] name:{} color:{} size:{}".format(self.name,self.color,self.size))
  def action_NCSize1(self):
    print("\nNCSize1 클래스 고유 메소드")    

class Size:  
  def __init__(self):
    self.size="large"

class NCSize2(Name_Color1,Size):
  # 부모클래스(Name_Color1)로부터 멤버변수값 상속받고, 
  # size=large로 고정된 멤버변수값을 갖는 새로운 부모클래스(Size) 추가 상속
  def __init__(self):
    Name_Color1.__init__(self)
    Size.__init__(self)
  def confirm(self):
    print("\nNCSize2 클래스입니다.")
    print("[멤버변수] name:{} color:{} size:{}".format(self.name,self.color,self.size))
  def action_NCSize2(self):
    print("\nNCSize2 클래스 고유 메소드")    
    
class NCSize3(Name_Color1,Size):  # 위와 동일 but 멤버변수 size값만 입력/추가
  def __init__(self,size):
    Name_Color1.__init__(self)
    Size.__init__(self)
    self.size=size
  def confirm(self):
    print("\nNCSize3 클래스입니다.")
    print("[멤버변수] name:{} color:{} size:{}".format(self.name,self.color,self.size))
  def action_NCSize3(self):
    print("\nNCSize3 클래스 고유 메소드")    
    

a=Name()
b=Color()
c=Num_Name1(1)
d=Num_Name2()
e=Num_Name3(3,"장미")
f=Name_Color1()
g=Name_Color2()
h=NCSize1("small")
i=NCSize2()
j=NCSize3("large")

a.confirm()
b.confirm()
c.confirm()
d.confirm()
e.confirm()
f.confirm()
g.confirm()
h.confirm()
i.confirm()
j.confirm()

g.action_Name_Color2()
g.action_Name() #부모클래스(Name)의 고유 메소드가 상속된 것 확인