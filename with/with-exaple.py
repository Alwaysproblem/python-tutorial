#%%

#%%

#%%
from contextlib import contextmanager

class Person:
    def __init__(self, name):
        self.name = name

    def say_something(self, msg):
        print(f'{self.name}: {msg}')

    @staticmethod
    @contextmanager
    def enter(name,  # <-- members of construct
              para_1, options: dict  # <-- Other parameter that you wanted.
              ):
        with Person(name) as instance_person:
            try:
                print(para_1)
                print(options)
                yield instance_person
            finally:
                ...

    def __enter__(self):
        print(self.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')


with Person.enter('Carson', para_1=1, options=dict(key='item_1')) as carson:
    carson.say_something('age=28')
    print('inside')
print('outside')

#%%
from contextlib import ContextDecorator

class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, *exc):
        print('</p>')
        return False

@makeparagraph()
def emit_html():
    print('Here is some non-HTML')

emit_html()

#%%
from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
   print("foo")

# %%
