import logging
from dataclasses import dataclass, field
from pprint import pprint

import regex as re


@dataclass
class Passport():
    byr: str = ""
    iyr: str = ""
    eyr: str = ""
    hgt: str = ""
    hcl: str = ""
    ecl: str = ""
    pid: str = ""
    cid: str = ""
    simple_validity: bool = False
    complex_validity: bool = False
    errors: list[str] = field(default_factory=list)

    def __init__(self, raw_record: str, *args, **kwargs):
        self.raw_record = raw_record
        self.errors = []
        regex = "(\S{3}):(\S+)"

        matches = re.finditer(regex, self.raw_record, re.IGNORECASE | re.DOTALL)

        # for groupNum in range(0, len(match.groups())):

        for matchNum, match in enumerate(matches, start=1):
            key = match.groups()[0]
            if key == "byr":
                self.byr = match.groups()[1]
            elif key == "iyr":
                self.iyr = match.groups()[1]
            elif key == "eyr":
                self.eyr = match.groups()[1]
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
                if len(self.pid) == 9:
                    if not self.pid.isnumeric():
                        self.errors.append("pid restriction failed.")
                else:
                    self.errors.append("pid restriction failed.")
                if self.byr is None:
                    self.errors.append("byr empty.")
                if int(self.byr) < 1920 or int(self.byr) > 2002:
                    self.errors.append("byr restriction failed.")
                if self.iyr is None:
                    self.errors.append("iyr empty.")
                if int(self.iyr) < 2010 or int(self.iyr) > 2020:
                    self.errors.append("iyr restriction failed.")
                if self.eyr is None:
                    self.errors.append("eyr empty.")
                if int(self.eyr) < 2020 or int(self.eyr) > 2030:
                    self.errors.append("eyr restriction failed.")
                if self.ecl not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                    self.errors.append("ecl format failed.")
                if len(self.hcl) == 7 and self.hcl[:1] == "#":
                    result: re = [re.fullmatch("([0-9a-f]*)", self.hcl[-6:], 0, re.IGNORECASE | re.DOTALL)]
                    if result[0].string != self.hcl[-6:]:
                        self.errors.append("hcl format failed.")
                else:
                    self.errors.append("hcl format failed.")
                if self.hgt[-2:] not in {"cm", "in"}:
                    self.errors.append("hgt format failed.")
                else:
                    if self.hgt[-2:] == "in":
                        size: int = int(self.hgt[:2])
                        if size < 59 or size > 76:
                            self.errors.append("IN restriction failed.")
                    elif self.hgt[-2:] == "cm":
                        size: int = int(self.hgt[:3])
                        if size < 150 or size > 193:
                            self.errors.append("CM restriction failed.")
                    else:
                        self.errors.append("hgt size failed.")
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

    print(f"\n\nSUMMARY")
    print(f"Valid count = {valid_count}")
    print(f"Valid2 count = {valid_count2}")


if __name__ == "__main__":
    logging.basicConfig()
    log = logging.getLogger('custom_log')
    log.setLevel(logging.DEBUG)

    main()
