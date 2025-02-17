universities_input = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
    ]

def enrollment_status(universities):
    """Lists of number of enrolled students and tuition price"""
    enrollment = [uni[1] for uni in universities]
    tuition_ = [uni[2] for uni in universities]
    return enrollment, tuition_

def mean(val):
    """Calculates mean"""
    return sum(val)/len(val)

def median(val):
    """Calculates median"""
    val = sorted(val)
    if len(val)%2 == 0:
        return (val[int(len(val)/2)] + val[int(len(val)/2)-1])/2
    else:
        return val[int(len(val)//2)]

students, tuition = enrollment_status(universities_input)

print(f'Total students: {sum(students)}')
print(f'Total tuition: {sum(tuition)}')

print(f'Student mean: {round(mean(students), 2)}')
print(f'Student median: {median(students)}')

print(f'Tuition mean: {round(mean(tuition),2)}')
print(f'Tuition median: {median(tuition)}')