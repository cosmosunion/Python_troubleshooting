class Unit :
  def __init__(self,name,hp,speed): # __init__(생성자)으로 class 정의할 때 self.변수 선언
     # 멤버변수 : 클래스 내에서 정의된 변수들
    self.name=name 
    self.hp=hp
    self.speed=speed
    
  def move(self,location):
    print("\n[지상 유닛 이동]")
    print("{}이(가) {}시 방향으로 이동합니다. [이동속도 : {}]".format(self.name,location,self.speed))

  def cured(self):  # (인스턴스)메소드 = self를 통해 인스턴스(속성)에 접근가능 / 다른 인스턴스 메소드 호출 가능  
    self.hp+=(self.hp*0.1)
    print("\n{}의 체력이 10% 회복되었습니다.\n[{} 현재 체력 : {}]".format(self.name,self.name,self.hp))

  def attack(self,location):
    print("{}이(가) {}시 방향의 적군을 향해 공격합니다.".format(self.name,location))    
    
  def attacked(self,damage): 
    self.hp-=damage
    if self.hp<0:
      self.hp=0
      print("\n{}이(가) 적군의 공격을 받아 체력이 {}만큼 감소되었습니다.\n[{} 현재 체력 : {}]".format(self.name,damage,self.name,self.hp))
      print("{}이 파괴되었습니다.".format(self.name))
    else:    
      print("\n{}이(가) 적군의 공격을 받아 체력이 {}만큼 감소되었습니다.\n[{} 현재 체력 : {}]".format(self.name,damage,self.name,self.hp))     
      
class Medic(Unit) : # Unit 클래스로부터 name,hp값을 상속(inheritance) 받음
  def __init__(self,name,hp,speed,heal): 
    Unit.__init__(self,name,hp,speed)
    self.heal=heal

  def __repr__(self):
    return "메딕(repr)"

  def confirm(self):
    print("\n{} 유닛이 생성되었습니다.".format(self.name))
    print("체력(hp) : {}, 치유력(heal) : {}, 이동력(speed) : {}".format(self.hp,self.heal,self.speed))

  def move(self,location): # Unit.move()가 존재하지만 '메소드오버라이딩'을 통해 새 클래스에서 move()값 초기화
    print("\n[치유 유닛 이동]")
    print("{}이(가) {}시 방향으로 이동합니다. [이동속도 : {}]".format(self.name,location,self.speed))


class Soldier(Unit) :
  def __init__(self,name,hp,speed,damage):
    Unit.__init__(self,name,hp,speed)
    self.damage=damage

  def __repr__(self):
    return "보병(repr)"  
  
  def confirm(self):
    print("\n{} 유닛이 생성되었습니다.".format(self.name))
    print("체력(hp) : {}, 공격력(damage) : {}, 이동력(speed) : {}".format(self.hp,self.damage,self.speed))

  def move(self,location):
    print("\n[지상 유닛 이동]")
    print("{}이(가) {}시 방향으로 이동합니다. [이동속도 : {}]".format(self.name,location,self.speed))

class Machinery(Unit):
  def __init__(self,name,hp,damage,speed):
    Unit.__init__(self,name,hp,speed)
    self.damage=damage

  def __repr__(self):
    return "탱크(repr)"

  def confirm(self):
    print("\n{} 유닛이 생성되었습니다.".format(self.name))
    print("체력(hp) : {}, 공격력(damage) : {}, 이동력(speed) : {}".format(self.hp,self.damage,self.speed))

  def attack(self,location):
    print("\n주변 정찰을 시작합니다.")
    print("{}이(가) {}시 방향의 적군을 향해 공격합니다.".format(self.name,location))
    # __init__함수에서 선언된 매개변수만 self.과 함께 쓴다. <-> location

class Flyable:
  def __init__(self,speed):
    self.speed=speed
    
  def confirm(self): # 생성된 유닛의 프로필을 __init__함수가 아닌 새로운 함수에서 선언 → or else 다중상속으로 들어가게 되면 프로필 소개 중복
    print("\n{} 유닛이 생성되었습니다.".format(self.name))
    print("체력(hp) : {}, 공격력(damage) : {}, 이동력(speed) : {}".format(self.hp,self.damage,self.speed))
  

class combatplane(Machinery,Flyable): 
# 다중 상속 : 2개 이상의 클래스로부터 변수값들을 상속받은 새로운 클래스 생성 가능
  def __init__(self,name,hp,damage,flying_speed):
    Machinery.__init__(self,name,hp,damage,0) # Machinery 지상 speed=0
    Flyable.__init__(self,flying_speed)
    self.speed=flying_speed

  def __repr__(self):
    return "알바트로스(repr)"

  def confirm(self): # 생성된 유닛의 프로필을 __init__함수가 아닌 새로운 함수에서 선언 → or else 다중상속으로 들어가게 되면 프로필 소개 중복
    print("\n{} 유닛이 생성되었습니다.".format(self.name))
    print("체력(hp) : {}, 공격력(damage) : {}, 이동력(speed) : {}".format(self.hp,self.damage,self.speed))
  
  def move(self,location):
    print("\n[공중 유닛 이동]")
    print("{}이(가) {}시 방향으로 이동합니다. [이동속도 : {}]".format(self.name,location,self.speed))


# print("="*60)    
# 클래스의 '인스턴스'가 생성될 때 (self)를 제외한 변수의 수를 동일하게 입력하여야 생성가능
# infantry1=Soldier("보병",50,5,5) 
# tank1=Machinery("탱크",300,20,50)
# tank1.confirm()
# tank1.move("1") # Unit 클래스에 move 메소드 선언 후, 클래스 상속받은 새로운 클래스에도 사용 가능
#                 # 반대로 Unit 클래스에 move 메소드 선언 후에도 새로운 클래스에서 같은 이름의 
#                 # 새로운 move 메소드 선언 가능 (Machinery에 move 메소드 없음)
# medic1=Medic("메딕",50,5,10)
# medic1.confirm()
# medic1.move("2")

# albatross1=combatplane("알바트로스",200,100,100)
# albatross1.confirm()
# albatross1.move("2") # Unit 클래스도 move() 메소드가 존재하지만, combatplane 클래스에서 move() 재정의
#                      # 출력되는 함수값(move())은 같은 클래스 메소드값


print("\n"+"="*60)
print("\n< 예제 활용 >")

print("\n[시스템] : 유닛이 3개 생성되면 전투가 시작됩니다.")
player_group=[]

for i in range(3):
  order=int(input("\n[1]보병 [2]메딕 [3]탱크 [4]알바트로스 \n번호를 입력하여 <{}번째> 유닛을 생성하세요. ".format(i+1)))
  # input을 int로 감싸주지 않으면 정상 실행하지 않는다.
  # input()함수가 키보드로 입력한 값을 무조건 '문자열'로 처리하기 때문
  if order==1:
    soldier1=Soldier("보병",50,5,5)
    soldier1.confirm()
    player_group.append(soldier1) # empty list인 group에 solider1 데이터 추가
  elif order==2:
    medic1=Medic("메딕",50,5,10)
    medic1.confirm()
    player_group.append(medic1)
  elif order==3:
    tank1=Machinery("탱크",300,20,50)
    tank1.confirm()
    player_group.append(tank1)
  elif order==4:
    albatross1=combatplane("알바트로스",200,100,100)
    albatross1.confirm()
    player_group.append(albatross1)
  i+=1
  
print("\n[시스템] : 유닛 3개가 모두 생성되어 자동으로 전투가 시작됩니다.")
print("플레이어 공격부대 :",player_group)

for player in player_group:
  player.move("2")