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


# print validate_Email('1526840124@qq.com')
# print validate_Gender('0')

update_profile_validate = {"name": validate_Name, "phone": validate_Phone, 'student_number': validate_StudentNumber,
                  'building': validate_Building, 'gender': validate_Gender}