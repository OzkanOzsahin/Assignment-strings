# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


#Part 1 
#1 who scored?
goalscorer0 = "Ruud Gullit"
goalscorer1 = "Marco van Basten"
print(goalscorer0, goalscorer1)
#2 What minute?
goal_time0 = 32
goal_time1 =  54
print(goal_time0, goal_time1)

#3 Scorers 
# using + operator create string
# <scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
scorers = (f"{goalscorer0} {goal_time0}, {goalscorer1} {goal_time1}")

#4 use f strings to create single string who scored when..
scorers = (f"{goalscorer0} {goal_time0} {goalscorer1} {goal_time1}")
report = (f"{goalscorer0} scored in the {goal_time0}nd minute\{goalscorer1} scored in {goal_time1}th minute")
print(report)

#Part 2
#1
player = 'Ruud Gullit'
#2
first_name = player[:player.find('')]
#3
last_name = player[:player.find('')]

first_name_len = len(first_name)
last_name_len = len(last_name)
#4
name_short = (player[0] + '.' + last_name)
print (name_short)

#5 
chant = first_name + 'Ruud '
chant = chant *3
chant = chant.rstrip(chant[-1])
print (chant)




