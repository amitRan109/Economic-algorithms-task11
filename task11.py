from typing import List
import math


class Player:
    def __init__(self, values: List[int], id: int):
        self.values = values
        self.match = None
        self.id = id

    def get_value(self, match: int) -> int:
        return self.values[match]

    def set_value(self, index: int, value: int):
        self.values[index] = value


# in: list of students and their preferences, list of departments and their preferences
# out: the matches
def deferred_acceptance(students: List[Player], departments: List[Player]) -> list[int]:
    # each student choose the best dep
    while not_all_match(departments):
        for s in students:
            match_idx = 0
            for d in departments:
                if s.get_value(d.id) < s.get_value(match_idx):
                    match_idx = d.id
            s.match = match_idx

        # for each dep make list of students and choose the best
        for d in departments:
            # make list of students
            students_who_wants = []
            for s in students:
                if s.match == d.id:
                    students_who_wants.append(s.id)

            # choose the best student
            if students_who_wants:  # list doesnt empty
                match_idx = students_who_wants[0]
                for s_idx in students_who_wants[1:]:
                    if d.get_value(s_idx) < d.get_value(match_idx):
                        students[match_idx].set_value(d.id, math.inf)  # the student cant choose this dep anymore
                        match_idx = s_idx
                    else:
                        students[s_idx].set_value(d.id, math.inf)  # the student cant choose this dep anymore
                d.match = match_idx
    for d in departments:
        print("Department:", d.id, "with student", d.match)


def not_all_match(departments: List[Player]):
    result = False
    for d in departments:
        if d.match is None:
            result = True
    return result


if __name__ == "__main__":
    import doctest

    doctest.testfile("test.txt", verbose=True)
