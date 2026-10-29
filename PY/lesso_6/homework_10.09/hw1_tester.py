class Tester:
    def __init__(self, name, level):
        self.name = name

        if level in ["junior", "middle", "senior"]:
            self.level= level
        else:
            raise ValueError("Leven need by 'junior', 'middle' or 'senior'")

    def introduce (self):
        print(f"Hello i'm {self.name}, {self.level} QA-engineer")

    def find_bug(self, bug_description):
        print(f"🐛{self.name} found bug: {bug_description}")

    def write_report(self,component):
        print(f"📝{self.name} write bug-report for component{component}")


tester1 = Tester("Petr", "junior")
tester2 = Tester("Pavel", "senior")

tester1.introduce()
tester1.find_bug("The button won't respond")
tester1.write_report("Trash")


print('='* 20)

tester2.introduce()
tester2.find_bug("The page won’t load")
tester2.write_report("Authorisation")

    