{% include navigation.html %}
## Create Task

GitHub page that documents intended Create Task project for College Board, snippets, and links to Runtime.

### Intended Create Task Project

My intended create task project is a memory game, where you have to copy the computers randomly generated sequence.  

[Here is a link to the video](https://drive.google.com/file/d/1u65AfSh-Gb_r3Nikpgz4iJ0cdh_3WcMg/view?usp=sharing)

### Snippets

Instructions for input:

```
sleep = input('enter your hours of sleep: ')
exercise = input('enter your minutes of exercise: ')
calories = input('enter your amount of calories: ')
screentime = input('enter your hours of screentime: ')
```

Use a list:

```
def healthy(list):
    list[sleep, exercise, calories, screentime]
```

Procedure/An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure/Calls to your student-developed procedure/Instructions for output (tactile, audible, visual, or textual) based on input and program functionality:

```
if int(sleep) < 8:
        print("get some more sleep!")
    else:
        print("you are getting enough sleep :)")
    if int(exercise) < 30:
        print("stand up and go for a walk!")
    else:
        print("you are very active :)")
    if int(calories) < 2000:
        print("consume some more fats, carbs, protein!")
    else:
        print("you have good eating habits :)")
    if int(screentime) > 12:
        print("rest your eyes!")
    else:
        print("you are keeping your eyes healthy :)")
```
