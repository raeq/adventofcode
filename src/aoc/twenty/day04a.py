import dataclasses
import logging
from dataclasses import field
from pprint import pprint
from typing import List, Optional

import regex as re
from pydantic import (
    BaseModel,
    conint,
    constr,
)


class Passport(BaseModel):
    raw_record: str = ""

    byr: Optional[conint] = conint(gt=1920, lt=2002)
    iyr: Optional[conint] = conint(gt=2010, lt=2020)
    eyr: Optional[conint] = conint(gt=2020, lt=2030)
    hgt: Optional[constr] = constr(regex=r'^((1[5-8][0-9]|19[0-3])(cm))|((59|6[0-9]|7[0-6])(in))$')
    hcl: Optional[constr] = constr(regex=r'^([0-9a-f]*)$')
    ecl: Optional[constr] = constr(regex=r'^(amb|blu|brn|gry|grn|hzl|oth)$')
    pid: Optional[constr] = constr(regex=r'^[0-9]{9}]$')
    cid: Optional[str] = ""

    simple_validity: Optional[bool] = False
    complex_validity: Optional[bool] = False
    errors: Optional[list[str]] = list

    def __init__(self, raw_record: str, *args, **kwargs):
        self.raw_record = raw_record.replace('\n', ' ')
        self.errors = []
        regex = "(\S{3}):(\S+)"

        matches = re.finditer(regex, self.raw_record, re.IGNORECASE | re.DOTALL)

        # for groupNum in range(0, len(match.groups())):

        for matchNum, match in enumerate(matches, start=1):
            key = match.groups()[0]
            if key == "byr":
                self.byr = int(match.groups()[1])
            elif key == "iyr":
                self.iyr = int(match.groups()[1])
            elif key == "eyr":
                self.eyr = int(match.groups()[1])
            elif key == "hgt":
                self.hgt = match.groups()[1]
            elif key == "hcl":
                self.hcl = match.groups()[1]
            elif key == "ecl":
                self.ecl = match.groups()[1]
            elif key == "pid":
                self.pid = match.groups()[1]
            elif key == "cid":
                self.cid = match.groups()[1]

        self.simple_validity = self.is_simple_valid()
        self.complex_validity = not bool(self.is_complex_valid())

    def is_simple_valid(self) -> bool:
        if (
                self.byr and self.iyr and self.eyr and self.hgt and self.hcl and
                self.ecl and self.pid
        ):
            return True

        else:
            return False

    def is_complex_valid(self) -> bool:
        if self.simple_validity:
            try:
                pass
            except ValueError as e:
                self.errors.append("conversion error {e.msg}.")
            except Exception as e:
                raise

            return len(self.errors) > 0
        else:
            return True


def load_file(file_name: str) -> str:
    with open(file_name, 'r') as fd:
        return fd.read()


def main():
    fields = load_file("day04.txt")
    full_text = "".join(fields)

    all_passports: list = []

    regex = r"(.*?)\n\n"
    matches = re.finditer(regex, full_text, re.IGNORECASE | re.DOTALL)

    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            all_passports.append(Passport(raw_record=str(match.group(groupNum))))

    valid_count: int = 0
    valid_count2: int = 0

    _: Passport = None
    print(f"\nPassports failing simple validity checks:")
    for _ in all_passports:
        if not _.simple_validity:
            pprint(_)

    print(f"\nPassports failing rigorous checks:")
    for _ in all_passports:
        if not _.complex_validity:
            pprint(_)

    print(f"\nPassports passing simple validity checks:")
    for _ in all_passports:
        if _.simple_validity:
            valid_count += 1
            pprint(_)

    print(f"\nPassports passing rigorous validity checks:")
    for _ in all_passports:
        if _.complex_validity:
            valid_count2 += 1
            pprint(_)
    for _ in all_passports:
        if _.complex_validity:
            valid_count2 += 1

    print(f"\n\nSUMMARY")
    print(f"Valid count = {valid_count}")
    print(f"Valid2 count = {valid_count2}")


if __name__ == "__main__":
    logging.basicConfig()
    log = logging.getLogger('custom_log')
    log.setLevel(logging.DEBUG)

    main()
