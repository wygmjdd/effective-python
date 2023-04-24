

from collections import defaultdict


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


if __name__ == '__main__':
    test1()
    test2()
    test3()
