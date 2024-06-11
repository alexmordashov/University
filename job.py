class Job:
    def __init__(self, name, salary, health, mood, energy, iq):
        self.name = name
        self.salary = salary
        self.health = health
        self.mood = mood
        self.energy = energy
        self.iq = iq

    def is_job(self, student):
        if float(student.health) >= self.health and float(student.mood) >= self.mood and float(student.energy) >= self.energy and float(student.iq) >= self.iq:
            return 1
        else:
            return 0

    def process(self, student):
        student.is_job = 1
        student.date_start_job = student.date
        student.salary = self.salary
