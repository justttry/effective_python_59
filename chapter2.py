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
    

########################################################################
class ToDictMixin(object):
    """"""

    #----------------------------------------------------------------------
    def to_dict(self):
        return self._traverse_dict(self.__dict__)
    
    #----------------------------------------------------------------------
    def _traverse_dict(self, instance_dict):
        """"""
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output
    
    #----------------------------------------------------------------------
    def _traverse(self, key, value):
        """"""
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value
        
        
########################################################################
class BinaryTree(ToDictMixin):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, value, left=None, right=None):
        """Constructor"""
        self.value = value
        self.left = left
        self.right = right


########################################################################
class BinaryTreeWithParent(BinaryTree):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, value, left=None, right=None, parent=None):
        """Constructor"""
        super().__init__(value, left=left, right=right)
        self.parent = parent
    
    
########################################################################
class A(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.__private = 'haha'
        

########################################################################
class Resistor(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, ohms):
        """Constructor"""
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


########################################################################
class VoltageResistance(Resistor):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, ohms):
        """Constructor"""
        super(VoltageResistance, self).__init__(ohms)
        self._voltage = 0
        
    #----------------------------------------------------------------------
    @property
    def voltage(self):
        """"""
        return self._voltage
    
    #----------------------------------------------------------------------
    @voltage.setter
    def voltage(self, voltage):
        """"""
        self._voltage = voltage
        self.current = self._voltage / self.ohms
    

########################################################################
class BoundedResistance(Resistor):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, ohms):
        """Constructor"""
        super(BoundedResistance, self).__init__(ohms)
    
    #----------------------------------------------------------------------
    @property
    def ohms(self):
        """"""
        return self._ohms
        
    #----------------------------------------------------------------------
    @ohms.setter
    def ohms(self, ohms):
        """"""
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' %ohms)
        self._ohms = ohms
    

########################################################################
class FixedResistance(Resistor):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, ohms):
        """Constructor"""
        super(FixedResistance, self).__init__(ohms)
    
    #----------------------------------------------------------------------
    @property
    def ohms(self):
        """"""
        return self._ohms
    
    #----------------------------------------------------------------------
    @ohms.setter
    def ohms(self, ohms):
        """"""
        if hasattr(self, '_ohms'):
            raise AttributeError("can't set attribute")
        self._ohms = ohms
    
from datetime import timedelta
from time import ctime

########################################################################
class Bucket(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, period):
        """Constructor"""
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0
    
    #----------------------------------------------------------------------
    def __repr__(self):
        """"""
        return 'Bucked(max_quota=%d, quota_condumed=%d)' %(self.max_quota,
                                                           self.quota_consumed)
    
    #----------------------------------------------------------------------
    @property
    def quota(self):
        """"""
        return self.max_quota - self.quota_consumed
    
    #----------------------------------------------------------------------
    @quota.setter
    def quota(self, amount):
        """"""
        delta = self.max_quota - amount
        if amount == 0:
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


#----------------------------------------------------------------------
def fill(bucket, amount):
    """"""
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount

#----------------------------------------------------------------------
def deduct(bucket, amount):
    """"""
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount< 0:
        return False
    bucket.quota -= amount
    return True
    
        
        
########################################################################
class Homework0(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._grade = 0
    
    #----------------------------------------------------------------------
    @property
    def grade(self):
        """"""
        return self._grade
    
    #----------------------------------------------------------------------
    @grade.setter
    def grade(self, value):
        """"""
        if not 0 <= value <= 100:
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value
    
    
########################################################################
class Exam0(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._writing_grade = 0
        self._math_grade = 0
        
    #----------------------------------------------------------------------
    @staticmethod
    def _check_grade(value):
        """"""
        if not 0 <= value <= 100:
            raise ValueError('Grade must be between 0 and 100')
    
    #----------------------------------------------------------------------
    @property
    def writing_grade(self):
        """"""
        return self._writing_grade
    
    #----------------------------------------------------------------------
    @writing_grade.setter
    def writing_grade(self, value):
        """"""
        self._check_grade(value)
        self._writing_grade = value 
        
    #----------------------------------------------------------------------
    @property
    def math_grade(self):
        """"""
        return self._math_grade
    
    #----------------------------------------------------------------------
    @math_grade.setter
    def math_grade(self, value):
        """"""
        self._check_grade(value)
        self._math_grade = value


from weakref import WeakKeyDictionary


########################################################################
class Grade(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._values = WeakKeyDictionary()
    
    #----------------------------------------------------------------------
    def __get__(self, instance, instance_type):
        """"""
        if instance is None:
            return self
        return self._values.get(instance, 0)
    
    #----------------------------------------------------------------------
    def __set__(self, instance, value):
        """"""
        if not 0 <= value <= 100:
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value
        

########################################################################
class Exam(object):
    """"""
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pass
    

########################################################################
class LazyDB(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.exists = 5
        
    #----------------------------------------------------------------------
    def __getattr__(self, name):
        """"""
        value = 'value for %s' % name
        setattr(self, name, value)
        return value

########################################################################
class LoggingLazyDB(LazyDB):
    """"""

    #----------------------------------------------------------------------
    def __getattr__(self, name):
        """"""
        print 'Called __getattr__(%s)' %name
        return super(LoggingLazyDB, self).__getattr__(name)
    

########################################################################
class ValidatingDB(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.exists = 5
        
    #----------------------------------------------------------------------
    def __getattribute__(self, name):
        """"""
        print 'Called __getattribute__(%s)' %name
        try:
            return super(ValidatingDB, self).__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' %name
            setattr(self, name, value)
            return value


########################################################################
class SavingDB(object):
    """"""

    #----------------------------------------------------------------------
    def __setattr__(self, name, value):
        """"""
        super(SavingDB, self).__setattr__(name, value)
    
    
########################################################################
class LoggingSavingDB(SavingDB):
    """"""

    #----------------------------------------------------------------------
    def __setattr__(self, name, value):
        """"""
        print 'Called __setattr__(%s, %r)' %(name, value)
        super(LoggingSavingDB, self).__setattr__(name, value)
        

########################################################################
class BrokenDictionaryDB(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._data = {}
    
    #----------------------------------------------------------------------
    def __getattribute__(self, name):
        """"""
        
    

        
    
#----------------------------------------------------------------------
def main():
    """"""
    data = LoggingSavingDB()
    print('Before: ', data.__dict__)
    data.foo = 5
    print('After: ', data.__dict__)
    data.foo = 7
    print('Finally:', data.__dict__)   
    
if __name__ == '__main__':
    main()