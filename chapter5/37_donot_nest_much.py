

from collections import defaultdict, namedtuple


# 1. 存储学生的分数
class SimpleGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def reprot_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


def test1():
    book = SimpleGradebook()
    # 书中每一行都直接写的'Isaac Newton', 我认为这容易敲错，故提出一个变量
    name = 'Isaac Newton'
    book.add_student(name)
    book.reprot_grade(name, 90)
    book.reprot_grade(name, 95)
    book.reprot_grade(name, 85)
    print('test1:', book.average_grade(name))


# 2. 需求变化，还得按照科目名存储分数
class BySubjectGradebook:
    def __init__(self):
        self._grades = {}  # 外层dict

    def add_student(self, name):
        self._grades[name] = defaultdict(list)  # 内存dict

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        # 因为是defaultdict，这里grade_list不需要初始化，会是一个list
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        # 这里会有除0报错吧？
        return total / count


def test2():
    book = BySubjectGradebook()
    name = 'Albert Einstein'
    book.add_student(name)
    # book.report_grade('xxx', 'Math', 75)
    book.report_grade(name, 'Math', 75)
    book.report_grade(name, 'Math', 65)
    book.report_grade(name, 'Gym', 90)
    book.report_grade(name, 'Gym', 95)
    print('test2:', book.average_grade(name))


# 3. 需求再变，分数需要有权重差异，期中和期末不一样
class WeightedGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def reprot_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for _, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight
            score_sum += subject_avg / total_weight
            score_count += 1
        return score_sum / score_count


def test3():
    book = BySubjectGradebook()
    name = 'Albert Einstein'
    book.add_student(name)
    book.report_grade(name, 'Math', 75)
    book.report_grade(name, 'Math', 65)
    book.report_grade(name, 'Gym', 90)
    book.report_grade(name, 'Gym', 95)
    print('test3:', book.average_grade(name))


# 3.1 传参太多，使用tuple优化一把写法
def test31():
    # 只重写一下计算average的函数
    grades = []
    grades.append((95, 0.45))
    grades.append((85, 0.55))
    total = sum(score * weight for score, weight in grades)
    total_weight = sum(weight for _, weight in grades)
    average_grade = total / total_weight
    print('test31 average_grade:', average_grade)


# 4. 害！如果再加一个评价呢？
def test4():
    grades = []
    grades.append((95, 0.45, 'Great job'))
    grades.append((85, 0.55, 'Better next time'))
    # 代码越写越难看了
    total = sum(score * weight for score, weight, _ in grades)
    total_weight = sum(weight for _, weight, _ in grades)
    average_grade = total / total_weight
    print('test4 average_grade:', average_grade)


# 5. 终极优化，使用namedtuple
Grade = namedtuple('Grade', ('score', 'weight', 'comment'))


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, grade):
        # 这里与书中不一致，我觉得直接传grade更好些，分数要再加些变量呢？
        self._grades.append(grade)

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]


def test5():
    # 这一节其实更多讲的是如何写出可读性更好的代码
    # 代码分层（Gradebook、Student、Subject、Grade）
    #     - 每一层代码少易于理解
    #     - 修改时只需要注意细节处就好
    book = Gradebook()
    albert = book.get_student('Albet Einstein')

    math = albert.get_subject('Math')
    math.report_grade(Grade(75, 0.05, '必须传递第3个参数'))
    math.report_grade(Grade(65, 0.15, '加油'))
    math.report_grade(Grade(70, 0.80, '有进步'))

    gym = albert.get_subject('Gym')
    gym.report_grade(Grade(100, 0.4, '完美'))
    gym.report_grade(Grade(85, 0.6, '怎么退步了呢？'))

    print('test5:', albert.average_grade())


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test31()
    test4()
    test5()
