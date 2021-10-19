# Alisha Agrawal (aa3se)

import urllib.request


def instructors(department):
    """
    returns an alphabetically-sorted list containing each instructor listed in Lou's List for the
    given department
    """
    combine = 'http://cs1110.cs.virginia.edu/files/louslist/' + department
    url = combine
    f = urllib.request.urlopen(url)
    class_list = []
    teacher_list = []
    for each in f:
        line = each.decode('utf-8').strip().split('|')
        class_list.append(line)
    for field in class_list:
        name = field[4]
        if '+' in name:
            name = name[:-2]
        if name not in teacher_list:
            teacher_list.append(name)
    teacher_list = sorted(teacher_list)
    return teacher_list


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    """
    returns a list of lists which contains all the information for all the classes that meet
    the provided criteria
    """
    combine = 'http://cs1110.cs.virginia.edu/files/louslist/' + dept_name
    url = combine
    f = urllib.request.urlopen(url)
    class_list = []
    for each in f:
        line = each.decode('utf-8').strip().split('|')
        class_list.append(line)

    if has_seats_available:
        seat_list = []
        for field in class_list:
            enrollment = int(field[15])
            total = int(field[16])
            if enrollment < total:
                seat_list.append(field)
        class_list.clear()
        for i in seat_list:
            class_list.append(i)

    if level is not None:
        level_list = []
        level = str(level)
        letter = level[0]
        for classes in class_list:
            course = classes[1]
            course_letter = course[0]
            if letter == course_letter:
                level_list.append(classes)
        class_list.clear()
        for i in level_list:
            class_list.append(i)

    if not_before is not None:
        before_list = []
        for begin in class_list:
            time = begin[12]
            if not_before <= int(time):
                before_list.append(begin)
        class_list.clear()
        for i in before_list:
            class_list.append(i)

    if not_after is not None:
        after_list = []
        for after in class_list:
            time = after[12]
            if not_after >= int(time):
                after_list.append(after)
        class_list.clear()
        for i in after_list:
            class_list.append(i)

    return class_list
