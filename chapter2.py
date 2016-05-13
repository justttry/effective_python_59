# encoding:UTF-8

import time
import datetime
from time import sleep
import json

#----------------------------------------------------------------------
def index_words(text):
    """"""
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

#----------------------------------------------------------------------
def index_words_iter(text):
    """"""
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

#----------------------------------------------------------------------
def read_visits(data_path):
    """"""
    with open(data_path) as f:
        for line in f:
            yield int(line)

#----------------------------------------------------------------------
def normalize_func(get_iter):
    """"""
    total = sum(get_iter)
    results = []
    for value in get_iter():
        percent = 100.0 * value / total
        results.append(percent)
    return results
            
#----------------------------------------------------------------------
def normalize(numbers):
    """"""
    total = sum(numbers)
    results = []
    for value in numbers:
        percent = 100.0 * value / total
        results.append(percent)
    return results

#----------------------------------------------------------------------
def normalize_defensive(numbers):
    """"""
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    results = []
    for value in numbers:
        percent = 100.0 * value / total
        results.append(percent)
    return results


########################################################################
class ReadVisits(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, data_path):
        self.data_path = data_path
        
    #----------------------------------------------------------------------
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

#----------------------------------------------------------------------
def log(message, *values):
    """"""
    if not values:
        print message
    else:
        values_str = ','.join(str(x) for x in values)
        print '%s: %s' %(message, values_str)

#----------------------------------------------------------------------
def my_generator():
    """"""
    for i in range(10):
        yield i
    
#----------------------------------------------------------------------
def my_func(*args):
    """"""
    for i in args:
        print i
        
#----------------------------------------------------------------------
def remainder(number, divisor):
    """"""
    return number % divisor

#----------------------------------------------------------------------
def flow_rate(weight_diff, time_diff):
    """"""
    return weight_diff / time_diff
 
#----------------------------------------------------------------------
def log(message, when = time.ctime()):
    """"""
    print '%s : %s' %(when, message)

#----------------------------------------------------------------------
def decode(data, default={}):
    """"""
    try:
        return json.loads(data)
    except:
        return default

#----------------------------------------------------------------------
def safe_division(number, divisor, ignore_overflow,
                  ignore_zero_division):
    """"""
    try:
        if number > 10000:
            raise OverflowError('greater then 10000')
        return number / divisor
    except OverflowError as e:
        if ignore_overflow:
            return 0
        else:
            raise OverflowError(e)
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise ZeroDivisionError('zeroerror')

#----------------------------------------------------------------------
def safe_division_d(number, divisor, **kwargs):
    """"""
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_div = kwargs.pop('ignore_zero_div', False)
    if kwargs:
        raise TypeError('Unexpected **kwargs: %r' % kwargs)
    try:
        return number / divisor
    except OverflowError as e:
        if ignore_overflow:
            return 0
        else:
            raise OverflowError(e)
    except ZeroDivisionError:
        if ignore_zero_div:
            return float('inf')
        else:
            raise ZeroDivisionError('zeroerror')
        
########################################################################
class SimpleGradebook(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._grades = {}
    
    #----------------------------------------------------------------------
    def add_student(self, name):
        """"""
        self._grades[name] = []
    
    #----------------------------------------------------------------------
    def report_grade(self, name, score):
        """"""
        self._grades[name].append(score)
    
    #----------------------------------------------------------------------
    def average_grade(self, name):
        """"""
        grades = self._grades[name]
        return sum(grades) / len(grades)
        
########################################################################
class BySubjectGradebook(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._grades = {}
    
    #----------------------------------------------------------------------
    def add_student(self, name):
        """"""
        self._grades[name] = {}
        
    #----------------------------------------------------------------------
    def report_grade(self, name, subject, grade):
        """"""
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)
    
    #----------------------------------------------------------------------
    def average_grade(self, name):
        """"""
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

import collections
Grade = collections.namedtuple('haha', ('score', 'weight'))
        
########################################################################
class Subject(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._grades = []
    
    #----------------------------------------------------------------------
    def report_grade(self, score, weight):
        """"""
        self._grades.append(Grade(score, weight))
    
    #----------------------------------------------------------------------
    def average_grade(self):
        """"""
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight
        
########################################################################
class Student(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._subjects = {}
    
    #----------------------------------------------------------------------
    def subject(self, name):
        """"""
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]
    
    #----------------------------------------------------------------------
    def average_grade(self):
        """"""
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

########################################################################
class Gradebook(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._student = {}
    
    #----------------------------------------------------------------------
    def student(self, name):
        """"""
        if name not in self._student:
            self._student[name] = Student()
        return self._student[name]

#----------------------------------------------------------------------
def log_missing():
    """"""
    print 'key added'
    return 0

########################################################################
class BetterCountMissing(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.added = 0
    
    #----------------------------------------------------------------------
    def __call__(self):
        """"""
        self.added += 1
        return 0


########################################################################
class InputData(object):
    """"""

    #----------------------------------------------------------------------
    def read(self):
        raise NotImplementedError


########################################################################
class PathInputData(InputData):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, path):
        """Constructor"""
        super().__init__()
        self.path = path
        
    #----------------------------------------------------------------------
    def read(self):
        """"""
        return open(self.path).read()


########################################################################
class Worker(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, input_data):
        """Constructor"""
        self.input_data = input_data
        self.result = None
    
    #----------------------------------------------------------------------
    def map(self):
        """"""
        raise NotImplementedError

    #----------------------------------------------------------------------
    def reduce(self):
        """"""
        raise NotImplementedError
    
import os

#----------------------------------------------------------------------
def generate_inputs(data_dir):
    """"""
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))
        
#----------------------------------------------------------------------
def create_workers(input_list):
    """"""
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorder(input_data))
    return workers

#----------------------------------------------------------------------
def execute(workers):
    """"""
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result    

#----------------------------------------------------------------------
def mapreduce(data_dir):
    """"""
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)    

########################################################################
class LineCountWorder(Worker):
    """"""

    #----------------------------------------------------------------------
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')
    
    #----------------------------------------------------------------------
    def reduce(self, other):
        """"""
        self.result += other.result
        
########################################################################
class AddClassMethodTest(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.a = 1
        self.b = 2
        print ClassMethodTest.__name__
    
    #----------------------------------------------------------------------
    @classmethod
    def add(cls, a, b):
        """"""
        raise NotImplementedError


########################################################################
class Add1Test(AddClassMethodTest):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(Add1Test, self).__init__()
    
    #----------------------------------------------------------------------
    @classmethod
    def printmethod(self):
        """"""
        print Add1Test.__name__
    
    #----------------------------------------------------------------------
    @classmethod
    def add(cls, a, b = 1):
        """"""
        cls.printmethod()
        print '%d add %d' %(a, b)
        return a + b


########################################################################
class Add2Test(AddClassMethodTest):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(Add1Test, self).__init__()
    
    #----------------------------------------------------------------------
    @classmethod
    def printmethod(self):
        """"""
        print Add2Test.__name__
    
    #----------------------------------------------------------------------
    @classmethod
    def add(cls, a, b = 2):
        """"""
        cls.printmethod()
        print '%d add %d' %(a, b)
        return a + b
        
########################################################################
class MultiClassMethodTest(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.a = 1
        self.b = 2
        print MultiClassMethodTest.__name__
    
    #----------------------------------------------------------------------
    @classmethod
    def multi(cls, add_class, a, b):
        """"""
        raise NotImplementedError
    
    
########################################################################
class Multi2Test(MultiClassMethodTest):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(Add1Test, self).__init__()
    
    #----------------------------------------------------------------------
    @classmethod
    def printmethod(self):
        """"""
        print Multi2Test.__name__
    
    #----------------------------------------------------------------------
    @classmethod
    def multi(cls, add_class, a, b = 2):
        """"""
        cls.printmethod()
        print '%d multi %d' %(add_class.add(a), b)
        return add_class.add(a) * b
    
    
########################################################################
class Multi3Test(MultiClassMethodTest):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(Add1Test, self).__init__()
    
    #----------------------------------------------------------------------
    @classmethod
    def printmethod(self):
        """"""
        print Multi3Test.__name__
    
    #----------------------------------------------------------------------
    @classmethod
    def multi(cls, add_class, a, b = 3):
        """"""
        cls.printmethod()
        print '%d multi %d' %(add_class.add(a), b)
        return add_class.add(a) * b

#----------------------------------------------------------------------
def main():
    """"""
    print '*' * 30
    Multi2Test.multi(Add1Test, 3)
    print '*' * 30
    Multi2Test.multi(Add2Test, 4)
    print '*' * 30
    Multi3Test.multi(Add1Test, 3)
    print '*' * 30
    Multi3Test.multi(Add2Test, 4)
    
if __name__ == '__main__':
    main()