# -*- coding=utf-8 -*-
import re


def validate_name(name):
    if len(name) < 40:
        if re.match('^[a-zA-Z0-9_\u4e00-\u9fa5]+$', name):
            return True
    return False


def validate_email(email):
    if len(email) > 7:
        if re.match('\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*', email) is not None:
            return True
    return False


def validate_phone(phone):
    if len(phone) > 6:
        if re.match('1\d{10}', phone) is not None:
            return True
    return False


def validate_student_number(student_number):
    if len(student_number) > 6:
        if re.match('^[0-9]+$') is not None:
            return True
    return False


# add in the future
def validate_building(building):
    return True


def validate_gender(gender):
    if re.match('^[0,1]{1}$', gender) is not None:
        return True
    return False


def validate_file(filename):
    file_type = filename[filename.rfind('.'):]
    if not file_type in ('.doc', '.pdf', '.txt', '.ttf', '.jpg', '.jpeg', '.png', 'bmp'):
        return False
    else:
        return True


def validate_status(status):
    if re.match('^[0,1]{1}$', status) is not None:
        return True
    return False


def validate_color(color):
    if re.match('^[0,1]{1}$', str(color)) is not None:
        return True
    return False


def validate_method(method):
    if re.match('^[0,1]{1}$', str(method)) is not None:
        return True
    return False


update_profile_validate = {"name": validate_name, "phone": validate_phone, 'student_number': validate_student_number,
                           'building': validate_building, 'gender': validate_gender}

trial_order_validate = {"name": validate_name, "phone": validate_phone, 'building': validate_building,
                        'status': validate_status, 'filetype': validate_file}

print_order_validate = {'status': validate_status, 'filetype': validate_file, 'color': validate_color,
                        'method': validate_method}