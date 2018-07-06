from django.apps import AppConfig

class TodoConfig(AppConfig):
    name = 'app.todo'
    verbose_name = 'To-do'

    def ready(self):
        base_url='localhost' 
        pass
