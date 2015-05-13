# -*- coding=utf-8 -*-
import re


def validate_Name(name):
    if len(name) < 40:
        if re.match('^[a-zA-Z0-9_\u4e00-\u9fa5]+$', name):
            return True
    return False


def validate_Email(email):
    if len(email) > 7:
        if re.match('\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*', email) != None:
            return True
    return False


def validate_Phone(phone):
    if len(phone) > 6:
        if re.match('1\d{10}', phone) != None:
            return True
    return False


def validate_StudentNumber(studentnumber):
    if len(studentnumber) > 6:
        if re.match('^[0-9]+$') != None:
            return True
    return False


# add in the future
def validate_Building(building):
    return True


def validate_Gender(gender):
    if re.match('^[0,1]{1}$', gender) != None:
        return True
    return False


def validate_file(filename):
    file_type = filename[filename.rfind('.'):]
    if not file_type in ('.doc', '.pdf', '.txt', '.ttf', '.jpg', '.jpeg', '.png', 'bmp'):
        return False
    else:
        return True


def validate_status(status):
    if re.match('^[0,1]{1}$', status) != None:
        return True
    return False


def validate_color(color):
    if re.match('^[0,1]{1}$', str(color)) != None:
        return True
    return False


def validate_method(method):
    if re.match('^[0,1]{1}$', str(method)) != None:
        return True
    return False


update_profile_validate = {"name": validate_Name, "phone": validate_Phone, 'student_number': validate_StudentNumber,
                           'building': validate_Building, 'gender': validate_Gender}

trial_order_validate = {"name": validate_Name, "phone": validate_Phone, 'building': validate_Building,
                        'status': validate_status, 'filetype': validate_file}

print_order_validate = {'status': validate_status, 'filetype': validate_file, 'color': validate_color,
                        'method': validate_method}