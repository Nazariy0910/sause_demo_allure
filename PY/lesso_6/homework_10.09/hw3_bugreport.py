class BugReport:
    def __init__ (self, title, component, reporter):
        self.title = title
        self.component = component
        self.reporter = reporter
        self.status = "open"
        self.priority = "medium"
    
    def set_priority(self, priority):
        self.priority = priority
        print(f"Priority change for: {self.priority}")

    def resolve(self):
        self.status = "resolved"
        print(f"✅ Bug '{self.title}' closed")

    def print_report(self):
        print(3 * "-", "Bug-Report", 3*"-")
        print(f"Title: {self.title}")
        print(f"Component: {self.component}")
        print(f"Reporter: {self.reporter}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self.status}")


bug = BugReport("Button doesn't respond ", "App", "Oleg")

bug.print_report()

bug.set_priority("high")
bug.resolve()

bug.print_report()