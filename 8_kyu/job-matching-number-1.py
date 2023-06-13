
'''https://www.codewars.com/kata/56c22c5ae8b139416c00175d/train/python'''


def match(candidate, job):
    if 'min_salary' not in candidate or 'max_salary' not in job:
        raise ValueError("Invalid candidate or job data")

    min_salary = candidate['min_salary']
    max_salary = job['max_salary']

    min_salary_with_wiggle_room = min_salary - (min_salary * 0.1)

    return min_salary_with_wiggle_room <= max_salary
