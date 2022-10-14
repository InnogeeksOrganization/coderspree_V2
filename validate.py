import os
from pathlib import Path
from typing import Any, List
from mdutils.mdutils import MdUtils
import requests


home = os.path.abspath(Path(__file__).parent)

submission_architecture = {"Patterns": 5}

domains = ["AR-VR", "IOT", "ML", "Android", "Web"]


class Student:
    def __init__(self, name, githubID, lilbraryid, domain, year):
        self.name = name
        self.githubID = githubID
        self.libraryid = lilbraryid
        self.solved = 0
        self.domain = domain
        self.completed = True
        self.logs = ""
        self.year = year

    def add_questions_solved(self, count):
        self.solved += count

    def __repr__(self) -> str:
        return f"""
            Name: {self.name}
            GitHubID: {self.githubID}
            LibraryID: {self.libraryid}
            Domain: {self.domain}
            Year: {self.year}
            Questions Solved: {self.solved}
            Logs: {self.logs}
        """

    def log_value(self, val):
        self.logs += val


def check_structure(path, student: Student):
    folderName = os.listdir(path)
    folderNameLowered = [x.lower() for x in folderName]

    for key, value in submission_architecture.items():
        if key.lower() in folderNameLowered:
            solved = len(
                os.listdir(
                    os.path.join(path, folderName[folderNameLowered.index(key.lower())])
                )
            )
            if solved < value:
                student.completed = False

            student.add_questions_solved(solved)
            student.log_value(
                f"Completed `{solved}` with minimum `{value}` in `{key}`, "
            )
        else:
            student.completed = False
            student.log_value(f"`{key}` Folder not found, ")


for domain in domains:
    for filename in os.listdir(os.path.join(home, domain)):
        year = "Invalid Foldername"
        name = "Invalid Foldername"
        libId = "Invalid Foldername"
        githubid = "Invalid Foldername"
        try:
            [githubid, name, libId, year] = filename.split("_")
        except ValueError:
            raise ValueError(filename, "is not correct")
        if name == "Invalid Foldername":
            try:
                [githubid, name, libId] = filename.split("_")
            except ValueError:
                raise ValueError(filename, "is not correct")

        student = Student(name, githubid, libId, domain, year)
        check_structure(os.path.join(home, os.path.join(domain, filename)), student)