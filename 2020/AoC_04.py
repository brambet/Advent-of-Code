from typing import List, NamedTuple, Dict, Callable, DefaultDict

import re
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=4)


TEST_BATCH = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


INVALID_TEST_BATCH = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""


VALID_TEST_BATCH = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""



class Passport():
    passport : Dict[str, str]
    validations : Dict[str, Callable]
    # byr: str #(Birth Year)
    # iyr: str #(Issue Year)
    # eyr: str #(Expiration Year)
    # hgt: str #(Height)
    # hcl: str #(Hair Color)
    # ecl: str #(Eye Color)
    # pid: str #(Passport ID)
    # cid: str #(Country ID)

  


    @staticmethod
    def _validate_byr(byr: str) -> bool:
        return 1920 <= int(byr) <= 2002
    
    
    @staticmethod
    def _validate_iyr(iyr: str) -> bool:
        return 2010 <= int(iyr) <= 2020

    
    @staticmethod
    def _validate_eyr(eyr: str) -> bool:
        return 2020 <= int(eyr) <= 2030

    
    @staticmethod
    def _validate_hgt(hgt: str) -> bool:
        if hgt.strip().endswith('cm'):
            return 150 <= int(hgt.strip('cm')) <= 193
        elif hgt.strip().endswith('in'):
            return 59 <= int(hgt.strip('in')) <= 76
        else:
            return False

    
    @staticmethod
    def _validate_hcl(hcl: str) -> bool:
        return bool(re.match('^#([A-F0-9a-f]{6})$', hcl))

    
    @staticmethod
    def _validate_ecl(ecl: str) -> bool:
        return (ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    

    @staticmethod
    def _validate_pid(pid: str) -> bool:
        return bool(re.match('^[0-9]{9}$', pid))

    
    _field_validations = { 'byr': _validate_byr.__func__, 
                            'iyr': _validate_iyr.__func__,
                            'eyr': _validate_eyr.__func__,
                            'hgt': _validate_hgt.__func__, 
                            'hcl': _validate_hcl.__func__,
                            'ecl': _validate_ecl.__func__,
                            'pid': _validate_pid.__func__}

    def __init__(self, raw: str):
        self.passport = {key_value.split(":")[0] : key_value.split(":")[1] for key_value in raw.split()}

        # self._field_validations = { 'byr': _validate_byr, 
        #                     'iyr': _validate_iyr,
        #                     'eyr': _validate_eyr,
        #                     'hgt': _validate_hgt, 
        #                     'hcl': _validate_hcl,
        #                     'ecl': _validate_ecl,
        #                     'pid': _validate_pid}

    def is_valid(self) -> bool:
        return (len(self.passport.keys())==8) or (len(self.passport.keys())==7 and ('cid' not in self.passport.keys()))

    
    def is_valid2(self) -> bool:

        return self.is_valid() and all(self._field_validations[key](value) for key,value in self.passport.items() if key != 'cid')


    # def _validate_byr(byr):
    #     return 1920 <= int(byr) <= 2020

    # def _validate_iyr(iyr):
    #     return 1920 <= int(byr) <= 2020



    # @staticmethod
    # def parse(raw : str):
    #     passport_dict = {key_value.split(":")[0] : key_value.split(":")[1] for key_value in raw.split()}

    #     return Passport(**passport_dict)



# print(TEST_BATCH.split("\n\n")[0])

if __name__ == "__main__":

    assert [Passport(raw).is_valid() for raw in TEST_BATCH.split("\n\n")].count(True) == 2
    
    print([Passport(raw).is_valid() for raw in puzzle.input_data.split("\n\n")].count(True))

    assert [Passport(raw).is_valid2() for raw in INVALID_TEST_BATCH.split("\n\n")].count(True) == 0
    assert [Passport(raw).is_valid2() for raw in VALID_TEST_BATCH.split("\n\n")].count(True) == 4

    print([Passport(raw).is_valid2() for raw in puzzle.input_data.split("\n\n")].count(True))
    #print(Passport(TEST_BATCH.split("\n\n")[0])._field_validations[''])