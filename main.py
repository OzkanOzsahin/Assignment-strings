# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


#Part 1 
#1 who scored?
player_0 = "Ruud Gullit"
player_1 = "Marco van Basten"
print (player_0, player_1)

#2 What minute?
goal_0 = 32
goal_1 = 54
print (goal_0, goal_1)

#3 Scorers 
# using + operator create string
# <scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
scorers = (f"{player_0} {goal_0}, {player_1} {goal_1}")
report = f"{player_0} scored in the {goal_0}nd minute\n{player_1} scored in {goal_1}th minute"
print(report)

#4 use f strings to create single string who scored when..



#Part 2
#1
player = 'Ruud Gullit'
#2
first_name = player[:player.find(' '):]
#3
last_name = player[:player.find(' '):]

first_name_len = len(first_name)
last_name_len = len(last_name)
#4
name_short = (player[0] + '. ' + last_name)
print (name_short)

#5 
yell = first_name + '! '
chant = yell *(first_name_len)
chant = chant.rstrip(chant[-1])
print(chant)

good_chant = (chant[-1] != ' ')
print (good_chant)


