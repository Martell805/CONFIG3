from sly import Parser
from FLexer import FLexer


class FParser(Parser):
    tokens = FLexer.tokens

    @_('empty')
    def lessons(self, expr):
        return []

    @_('lesson lessons')
    def lessons(self, expr):
        return [expr.lesson] + expr.lessons

    @_('"(" "L" name group_list student_list ")"')
    def lesson(self, expr):
        return {
            'lesson': expr.name,
            'groups': expr.group_list,
            'students': expr.student_list
        }

    @_('"(" "S" students ")"')
    def student_list(self, expr):
        return expr.students

    @_('empty')
    def students(self, expr):
        return []

    @_('student students')
    def students(self, expr):
        return [expr.student] + expr.students

    @_('"(" age name name ")"')
    def student(self, expr):
        return {
            'age': expr.age,
            'group': expr.name0,
            'name': expr.name1,
        }

    @_('INTEGER')
    def age(self, expr):
        return int(expr.INTEGER)

    @_('"(" "G" groups ")"')
    def group_list(self, expr):
        return expr.groups

    @_('empty')
    def groups(self, expr):
        return []

    @_('name groups')
    def groups(self, expr):
        return [expr.name] + expr.groups

    @_('STRING')
    def name(self, expr):
        return expr.STRING[1:-1]

    @_('')
    def empty(self, expr):
        return []
