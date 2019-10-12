from mycroft import MycroftSkill, intent_file_handler


class PacetasksEmployee(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('employee.pacetasks.intent')
    def handle_employee_pacetasks(self, message):
        self.speak_dialog('employee.pacetasks')


def create_skill():
    return PacetasksEmployee()

