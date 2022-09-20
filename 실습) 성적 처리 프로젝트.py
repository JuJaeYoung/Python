#Student class 를 작성하세요.
#Person class 와 score class 를 작성하고 이를 이용하여 Student class 를 완성하세요.
#KBD 혹은 File을 이용하여 학생의 이름과 학번, 전화번호, 성적 정보를 입력하고 이를 출력하세요.

class Student :
    def __init__(self, nam) :               # 생성자 (이름)
        self.name = nam


class Person(Student) :
    def info(self, num1, num2, num3) :      # 나이, 학번, 전화번호
        self.age = num1
        self.clnum = num2
        self.phnum = num3
        
        return self.age, self.clnum, self.phnum
        
        
class score(Student) :                       

    def kor(self, kor) :                    # 국어 점수 
        self.kor = kor

        return self.kor
        
    def mat(self, mat) :                    # 수학 점수
        self.mat = mat

        return self.mat
        
    def eng(self, eng) :                    # 영어 점수
        self.eng = eng

        return self.eng
        
    def soc(self, soc) :                    # 사회 점수
        self.soc = soc

        return self.soc
        
    def sci(self, sci) :                    # 과학 점수
        self.sci = sci

        return self.sci

q = 'Y'    
while q == 'Y' :
    a = input('이름 : ')        
    x = Person(a)
    y = score(a)

    x_age, x_clnum, x_phnum = x.info(input('나이 : '), input('학번 : '), input('전화번호 : '))
    y_kor = y.kor(input('국어 : '))
    y_mat = y.mat(input('수학 : '))
    y_eng = y.eng(input('영어 : '))
    y_soc = y.soc(input('사회 : '))
    y_sci = y.sci(input('과학 : '))


    print(f'\n이름 : {a}')
    print(f'나이 : {x_age}, 학번 : {x_clnum}, 전화번호 : {x_phnum}')
    print(f'국어 : {y_kor}점, 수학 : {y_mat}점, 영어 : {y_eng}점, 사회 : {y_soc}점, 과학 : {y_sci}점')

    q = input('계속하시겠습니까?(Y / N) : ').upper()
    print('\n')







