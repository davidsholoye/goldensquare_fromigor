1. Describe the Problem:

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries


2. Design the Class System

class Diary():
        PUBLIC PROPERTIES:
            entry_list : a list containing all the entries
            task_list : a list containing all the tasks

    def __init__(self):
        pass
    
    def add_entry(self, entry):
        PARAMETERS:
            entry = an instance of diaryEntry
        RETURNS
            nothing
        SIDE EFFECT
            adds an entry to the diary
    
    def add_task(self, task):
         PARAMETERS:
            task = an instance of TODO
        RETURNS
            nothing
        SIDE EFFECT
            adds a task to the task_list
    
    def show_all_entries(self):
         PARAMETERS:
            nothing
        RETURNS
            A list with all the entries
        SIDE EFFECT
            nothing
    
    def show_all_tasks(self):
        PARAMETERS:
            nothing
        RETURNS
            A list with all the tasks
        SIDE EFFECT
            nothing

class DiaryEntry():
        PUBLIC PROPERTIES
            title = a string with the title of the entry
            contents = a string with the contents of the entry

    def __init__(self):
        pass
    
    

3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

Encode one of these as a test and move to step 4.

4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

Encode one of these as a test and move to step 5.

5. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the class to behave according to your example.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.