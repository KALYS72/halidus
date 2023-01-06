'1'
# import random
# class Sniper:
#     health = 100

#     def __init__(self, name):
#         self.name = name

#     def shoot(self, name):
#         name.health -= 20    
    
#     def __str__(self):
#         # когда принтим обьект
#         # когда оборачиваем в строку
#         return self.name

# sniper1 = Sniper('Daniel')
# sniper2 = Sniper('Kalys')
# while sniper1.health != 0 and sniper2.health != 0:
#     choise = random.randint(1,2)
#     if choise == 1:
#         sniper1.shoot(sniper2)
#         print(f'{sniper1} попал по {sniper2}. у него осталось {sniper2.health} здоровья!\n')
#     else:
#         sniper2.shoot(sniper1)
#         print(f'{sniper2} попал по {sniper1}. у него осталось {sniper1.health} здоровья!\n')

# if sniper1.health == 0:
#     print(f'победил {sniper2}!!!')
# else:
#     print(f'победил {sniper1}!!!')


'2'
# CRED = '\033[31m'
# CEND = '\033[0m'    
# CGREEN = '\33[32m'
# CBLUE = '\33[34m'
# CYELLOW = '\33[93m'
# class Hogwarts:
#     courage = 'Gryffindor'.upper()
#     intelligence = 'Ravenclaw'.upper()
#     justice = 'Hufflepuff'.upper()
#     ambition = 'Slytherin'.upper()
#     def __init__(self,name:str,co:int,intel:int,just:int,amb:int):
#         self.name = name
#         self.co = co
#         self.intel = intel
#         self.just = just
#         self.amb = amb

#     def sorting_hat(self):
#         if self.co > self.intel and self.co > self.just and self.co > self.amb:
#             return f'{self.name} enters {CRED + self.courage + CEND}!!!'
#         elif self.intel > self.co and self.intel > self.just and self.intel > self.amb:
#             return f'{self.name} enters {CBLUE + self.intelligence + CEND}!!!'
#         elif self.amb > self.co and self.amb > self.intel and self.amb > self.just:
#             return f'{self.name} enters {CGREEN + self.ambition + CEND}!!!'
#         else:
#             return f'{self.name} enters {CYELLOW + self.justice + CEND} !!!'
            


    
# student1 = Hogwarts('Harry Potter',2,1,1,1)
# student4 = Hogwarts('Draco Malfoy',15,1,2,99999)
# student5 = Hogwarts('Cedrig Diggory',11,21,34,31)
# student2 = Hogwarts('Cho Chang',15,20,2,3)
# print(student1.sorting_hat())
# print(student4.sorting_hat())
# print(student5.sorting_hat())
# print(student2.sorting_hat())


'3'
# class Languages:
#     amount_students = 23
#     def coding(self):
#         pass
  
# class Python(Languages):
#     amount_Python = 10
#     def __init__(self):
#         Python.amount_Python+=1
#         Languages.amount_students+=1

#     def coding(self):
#         super().coding()
#         return 'I am Python student. I am coding now'

# class  JavaScript(Languages):
#     amount_JS = 21
#     def __init__(self):
#         JavaScript.amount_JS+=1
#         Languages.amount_students+=1

#     def coding(self):
#         super().coding()
#         return 'I am JavaScript student. I am coding now'



# student1 = Python()
# student2 = JavaScript()

# def quess():
#     import random
#     gg = int(input('Quess student(1-P 2-JS): '))
#     comp = random.randint(1, 2)
#     if comp == 2:
#         print(student2.coding())
#     else:
#         print(student1.coding())
#     if gg == comp:
#         print('Good job!')
#     else:
#         print('No bueno :(')
# quess()



'4'
# class Smartphone:
#     def where_to_wear(self):
#         return 'You can keep me anywhere'
#     def call(self, number):
#         assert type(number) == str, 'Номер должен быть строкой'
        # assert len(number) == 9, 'Номер должен состоять из 9 цифр'
#         n = number
        # return f'+996 {n[:3]} {n[3:5]}-{n[5:7]}-{n[7:]}\n    звоним...\n'

# class Watch:
#     def see_time(self):
#         from datetime import datetime
#         return 'Время - ' +  datetime.now().strftime("%H:%M:%S")
#     def where_to_wear(self):
#         return 'You should wear me on your hand'


# class Smartwatch(Watch,Smartphone):
#     pass

# gg = Smartwatch()
# print(gg.call('505190406'))
# print(gg.see_time())
# print(gg.where_to_wear())

'5'
# class CheckMixin:
#     def __init__(self,name,password):
#         self.name = name
#         self.password = password

#     def check(self, name, password):
#         if name == self.name and password == self.password:
#             return True
#         else:
#             return False


# class TikTok(CheckMixin):
#     amount = 0
#     posts = []

#     def post_video(self,post,name,password:str):
#         if super().check(name, password):
#             TikTok.amount += 1
#             TikTok.posts.append(post)
#             return f'Succesfully created\nПост: {post}\n'
#         else:
#             return 'No, u cant:)\n'

#     def get_videos_data(self):
#         return f'Количество постов: {TikTok.amount}\nПосты: {TikTok.posts}'

# class Instagram(CheckMixin):
#     amount = 0
#     posts = []

#     def post_post(self,post,name,password:str):
#         if super().check(name, password):
#             Instagram.amount += 1
#             Instagram.posts.append(post)
#             return f'Succesfully created\nПост: {post}\n'
#         else:
#             return 'No, u cant:)\n'
        
#     def get_posts_data(self):
#         return f'Количество постов: {Instagram.amount}\nПосты: {Instagram.posts}'
        
    

# tik = TikTok('Kalys', 19042006)
# ins = Instagram('Daniel', 1234)
# print(tik.post_video('White', 'Kalys', 19042006))
# print(tik.post_video('Yellow', 'Kalys', 19042006))
# print(tik.post_video('Blue', 'Kalys', 19042006))
# print(ins.post_post('NO', 'Daniel', 1234))
# print(ins.post_post('YES', 'Daniel', 1234))
# print(ins.post_post('Maybe', 'Daniel', 1234))
# print(tik.get_videos_data())
# print(ins.get_posts_data())

'6'
# class Terminal:
#     balance = 0
#     def __init__(self,card,code):
#         if type(card) == int and type(code) == int:
#             assert len(str(card)) == 16, 'Номер карты не действителен!'
#             self.card = card
#             assert len(str(code)) == 4, 'Код карты не действителен!'
            # self.__code = code
#         else:
#             print('Введите число!')
#     def put(self,password,som):
#         assert self.__code == password, 'Доступ запрещен!!!'
#         Terminal.balance += som
#         return f'Вы добавили на счет {str(som)} сомов, теперь на балансе {str(Terminal.balance)} сомов'
    
#     def get(self,password,som):
        # assert self.__code == password, 'Доступ запрещен!!!'
#         sp = []
#         som = str(som)
#         for i in som[1:]:
#             if i == '0':
#                 sp.append(True)
#             else:
#                 sp.append(False)  
        # assert not False in sp, 'Вы можете снимать только десятичные числа по типу: 200, 5000, 1000 и тд'
#         if Terminal.balance >= int(som):
#             Terminal.balance -= int(som)
            # return f'Вы сняли со счета {str(som)} сомов, на балансе осталось {str(Terminal.balance)} сомов'
#         else:
#             return 'Недостаточно средств для проведения данной операции!'

# bal = Terminal(4567645223221234, 2345)
# print(bal.put(2345, 1542))
# print(bal.put(2345, 1542))
# print(bal.get(2345, 1000))
# print(bal.get(2345, 1000))
# print(bal.card)
# print(bal._Terminal__code)


# остатки прошлого варианта округления

# som = '350'
# num = 0
# if int(som[1:2]) >= 5:
#     num = int(str(int(som[:1]) + 1) + (len(som) - 1) * '0')
# else:
#     num = int(str(int(som[:1])) + (len(som) - 1) * '0')
# print(num)

'7'
# class Taxi:
#         def __init__(self, name, cost, cost_km):
#                 self.name = name
#                 self.cost = cost
#                 self.cost_km = cost_km
#         def get_total_cost(self,km):
#                 res = self.cost_km * km + self.cost
#                 return f'Такси {self.name}, стоимость поездки: {res} сом'

# taxi1 = Taxi('Namba',35,20)
# taxi2 = Taxi('Yandex',40,30)
# taxi3 = Taxi('Jorgo',334524,1234567)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14)) 


'8'
# class WhatsApp:
#         def __init__(self, num:int):
#                 self.num = num
#         def send(self, text):
#                 return f'I am sending a text {text}'


# class SnapChat:
#         def __init__(self, num:int):
#                 self.num = num
#         def send(self, image:bool, text):
#                 if image == True:
#                         return f'I am sending a text {text} with some image'
#                 else:
#                         return f'I am sending a text {text} without image'

# class Telegram:
#         def __init__(self, num:int, username):
#                 self.num = num
#                 self.username = username
#         def send(self, voice):
#                 return f'I am sending a voice message {voice}'
# t = Telegram(+996505190406, 'Kalys')
# s = SnapChat(+996505190406)
# w = WhatsApp(+996505190406)
# print(t.send('how are you?'))
# print(s.send(True, 'I am sick:('))
# print(w.send('You"re Welcome!'))

'9'
# class A:
#     gl = ['а','у','о','ы','э','я','ю','ё','и','е']
#     def __init__(self):
#         pass
#     def count(self,word): 
#         g = 0
#         for i in A.gl:
#             for v in word.lower():
#                 if i == v:
#                     g += 1
#                 else:
#                     continue
#         return f'Количество гласных в слове {word} составляет: {g}'
            
# class B:
#     so = ['б', 'в', 'г', 'д', 'ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ']
#     def __init__(self):
#         pass
#     def count(self,word):
#         g = 0
#         for i in B.so:
#             for v in word.lower():
#                 if i == v:
#                     g += 1
#                 else:
#                     continue
#         return f'Количество согласных в слове {word} составляет: {g}'

# g = A()
# s = B()
# print(g.count('С Днем Рождения!!!'))
# print(s.count('С Днем Рождения!!!'))


'10'
# class Phone():
#         def __init__(self,name,last_name,phone):
#                 self.name = name
#                 self.last_name = last_name
#                 self.phone = phone
#         def get_info(self):
#                 return f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}'
# contact = Phone('Jhon', 'Snow', +996707707707)
# print(contact.get_info())
                

'11'
# class Salary:
#     percent = 8
#     def __init__(self,salary,experience):
#         self.salary = salary
#         self.experience = experience
#     def get_salary(self):
#         return (Salary.percent / 100) * self.salary * self.experience 
    
# obj = Salary(10000, 10)
# print(obj.get_salary())

'12'
# class Word:
#     def __new__(cls, **kwargs):
#         print(args)
#         return super().__new__(cls)

#     def __init__(self, string):
#         self.string = string
    
#     def __len__(self):
#         return len(self.string)

#     def __eq__(self, other):
#         if type(other) != Word:
#             raise TypeError
#         return len(self.string) == len(other.string)

# obj2 = Word('hello')
# obj1 = Word('world')
# print(len(obj1))
# print(obj2.__eq__(obj1))
# print(obj2.__new__())

'13'
# class Nobel:
#     def __init__(self,category,year,winner):
#         self.winner = winner
#         self.category = category
#         self.year = year
#     def get_year(self):
#         from datetime import datetime
#         nowi = datetime.now()
#         return f'выиграл {nowi.year - self.year} лет назад'

# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

'14'
# class Password:
#     def __init__(self,password):
#         self.password = password
#         self.password = self.password[0] + ('*' * len(self.password[1:]))
#     def validate(self):
#         assert len(self.password) >= 8 and len(self.password) <= 15, 'Password should be longer than 8, and less than 15'
#         assert not self.password.isalpha(), 'Password should contain numbers too'
#         assert not self.password.isdigit(), 'Password should contain letters as well'
#         for i in ['@', '#', '&', '$', '%', '!', '~', '*']:
#             if i in self.password:
#                 return 'Ваш пароль сохранен.'
#             return 'Your password should have some symbols'      
#     def __str__(self):
#         s = len(str(self.password))
#         return '*' * s
# ibj = Password('gggggg23%')
# print(ibj.password)
# print(ibj.validate())

'15'

# class MyUser:
#     password = ''
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name
#         for i in name:
#             if i in ['a', 'e', 'i', 'o', 'u', 'y']:
#                 MyUser.password += i
#             continue
#         for h in last_name:
#             if h in ['a', 'e', 'i', 'o', 'u', 'y']:
#                 MyUser.password += h
#             continue
#     def __str__(self):
#         g = self.name.replace(self.name[1:],'*' * len(self.name[1:])) 
#         s = self.last_name = str(self.last_name[0]) + ('*' * len(str(self.last_name[1:])))
#         MyUser.password = 'Exception: Forbidden'
#         return f'{g} {s}'

        
# user = MyUser('Makers', 'Bootcamp')
# print(user)     
# print(user.password)                

'16'

# class Mytuple:
#     def __init__(self,*args):
#         self.res = args
#         self.res = sum(args)
#     def __eq__(self, num):
#         return self.res == num.res
#     def __gt__(self, num):
#         return self.res > num.res
#     def __lt__(self, num):
#         return self.res < num.res
#     def __ne__(self, num):
#         return self.res != num.res
    
# a = Mytuple(1,2,3,4,5)
# b = Mytuple(6,7,8)
# print(a == b) # eq
# print(a > b) # gt
# print(a < b) # lt
# print(a != b) # ne

'17'

# class Math:
#     def __init__(self,value):
#         self.value = value
#     def get_factorial(self):
#         f = 1
#         for i in range(1, self.value):
#             f *= i
#         return f
#     def get_sum(self):
#         g = 0
#         for i in str(self.value):
#             g += int(i)
#         return g
#     def get_mul_table(self):
#         res = ''
#         for i in range(1, 11):
#             res += f'{self.value}x{i}={self.value * i}' + '\n'
#         return res
# obj = Math(0)
# print(obj.get_sum())
# print(obj.get_factorial())
# print(obj.get_mul_table())

'18'
# class ToDo:
#     instances = {}
#     def __init__(self):
#         pass
#     def give_priority(self, num, instance):
#         g = {num:instance}
#         ToDo.instances.update(g)
#     def list_of_tasks(self):
#         res = []
#         for k,v  in ToDo.instances.items():
#             res.append([k,v])
#         return res


# obj = ToDo()
# print(obj.give_priority(1, 'yes me'))
# print(obj.give_priority(2, 'no u'))
# print(obj.give_priority(3, 'maybe we'))
# print(obj.list_of_tasks())

'19'

# from abc import ABC, abstractmethod, abstractproperty
# from datetime import date

# class AbstractDaysAndDates(ABC):
#     @abstractmethod
#     def define_date(self):
#         'Выводит текущюю дату'
#         ...
#     @abstractmethod
#     def define_days(self):
#         'Выводит текущие дни'
#         ...


# class Current(AbstractDaysAndDates):
#     def define_date(self):
#         'Выводит текущюю дату'
        # today = date.today()
#         g = today.day,'/',today.month,'/',today.year
#         res = ''
#         for i in g:
#             res += str(i)
#         return res
#     def define_days(self):
#         'Выводит текущее число'
#         today = date.today()
#         return f'Сегодняшнее число {today.day}'

# class MonthStart(AbstractDaysAndDates):
#     def define_date(self):
#         'Выводит первый день недели'
#         today = date.today()
#         g = 1,'/',today.month,'/',today.year
#         res = ''
#         for i in g:
#             res += str(i)
#         return res
#     def define_days(self):
#         'Выводит количество прошедших дгней с начала месяца'
#         today = date.today()
#         return f'С начала месяца прошло {today.day - 1} дней'

# class MonthEnd(AbstractDaysAndDates):
#     day = 0
#     def __init__(self):
#         'Определяет последний день недели по месяцу'
#         today = date.today()
#         if today.month == 1 or today.month == 3 or today.month == 5 or today.month == 7 or today.month == 8 or today.month == 10 or today.month == 12:
#             MonthEnd.day += 31
#         elif today.month == 2:
#             MonthEnd.day += 28
#         else:
#             MonthEnd.day += 30

#     def define_date(self):
#         return f'{MonthEnd.day} числа - последний день текущего месяца'

#     def define_days(self):
#         today = date.today()
#         return f'До конца месяца осталось {MonthEnd.day - today.month} дней'

# y = Current()
# print(y.define_date())
# print(y.define_days(),'\n')

# p = MonthStart()
# print(p.define_date())
# print(p.define_days(),'\n')

# g = MonthEnd()
# print(g.define_date())
# print(g.define_days(),'\n')

'20'
# 3. Создайте абстрактный класс Bank с атрибутами экземпляра класса name, interest_rate, term, loan_balance, interest_balance и методами: get_product, loan_issue, interest_accrual и loan_repayment.
# а) Создайте класс StartupLoan, переопределите метод get_product, чтобы он выводил информацию о кредитном продукте:
# Кредитный продукт: “Стартап”
# Процентная ставка: 20% годовых
# Срок кредита: 2 года
# b) Добавьте методы:
# - loan_issue для выдачи кредита, который увеличивает сумму loan_balance и выводит сообщение “Кредит в сумме {сумма} сомов выдан {дата} года.”
# - interest_accrual для начисления процентов со дня выдачи до конца месяца с выводом информации “Задолженность по процентам: {interest_balance} сомов”
# - loan_repayment для погашения основной суммы и процентов с выводом информации: “Кредит погашен в сумме {сумма}. Остаток по кредиту: {loan_balance} сомов, остаток по процентам: {interest_balance} сомов.”

# class Bank(ABC):
#     @abstractproperty
#     def name(self):
#         ...
#     @abstractproperty
#     def interest_rate(self):
#         ...
#     @abstractproperty
#     def term(self):
#         ...
#     @abstractproperty
#     def loan_balance(self):
#         ...
#     @abstractproperty
#     def interest_balance(self):
#         ...
#     @abstractmethod
#     def get_product(self):
#         ...
#     @abstractmethod
#     def loan_issue(self):
#         ...
#     @abstractmethod
#     def interest_accrual(self):
#         ...
#     @abstractmethod
#     def loan_repayment(self):
#         ...
# class StartupLoan(Bank):
#     name = 'Стартап'
#     interest_rate = 20
#     term = 2
#     loan_balance = 0
#     interest_balance = 0
      
#     def get_product(self):
#         return f'Кредитный продукт: "{self.name}"\nПроцентная ставка: {self.interest_rate}% годовых\nСрок кредита: {self.term} года'
   
#     def loan_issue(self,summ):
#         today = date.today()
#         self.loan_balance += summ
#         return f'Кредит в сумме {summ} сомов выдан {today.year} года.'

#     def interest_accrual(self):
#         self.interest_balance =  (self.loan_balance + self.loan_balance) * 20 / 100
#         return f'Задолженность по процентам: {self.interest_balance} сомов'
        
#     def loan_repayment(self, summ):
#         if summ > self.interest_balance:
#             self.loan_balance += (self.interest_balance- summ)
#             # self.interest_balance -= summ
#             del self.interest_balance
#             if self.loan_balance <= 0:
#                 print('долг погашен')
#             elif self.loan_balance > 0:
#                 print(f'долг {self.loan_balance}, процентов нет')
#         elif summ == self.interest_balance:
#             del self.interest_balance
#             print(f'долг {self.loan_balance}, проценты {self.interest_balance}')
#         elif summ < self.interest_balance:
#             self.interest_balance -= summ
#             print(self.loan_balance, self.interest_balance)

# Kaidzi = StartupLoan()
# print(Kaidzi.loan_issue(100000))
# print(Kaidzi.interest_accrual())
# print(Kaidzi.interest_balance)
# print(Kaidzi.get_product())
# Kaidzi.loan_repayment(140000)

            
'21'

# class Person:
#     def __init__(self, name,last_name):
#         self.name = name
#         self.last_name = last_name
    
#     def get_human_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}')

# class Employee(Person):
#     def __init__(self, name, last_name, work, status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status
    
#     def get_human_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} и копыта на должности {self.status}.')

# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.course = course
#         self.university = university
    
#     def get_human_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе.')

# def get_human_info(obj):
#     obj.get_human_info()


# person = Person('Иван', 'Петров')
# employee = Employee('Иван', 'Петров', 'Рога и Копыта', 'Директор')
# student = Student('Иван', 'Петров', 'КГТУ', 3)

# get_human_info(person) 
# get_human_info(employee)
# get_human_info(student) 
