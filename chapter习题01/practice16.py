bread_cal = 140
hot_dog_cal = 120
tomato_cal = 80
mustard_cal = 20
onion_cal = 140
total_cal = 0
count = 1
print("\tbread\thot_dog\ttomato\tmustard\tonion\total_cal")
for bread in [1]:
	for hot_dog in [0,1]:
		for tomato in [0,1]:
			for mustard in [0,1]:	
				for onion in [0,1]:
					total_cal = bread*bread_cal+hot_dog*hot_dog_cal+tomato*tomato_cal+mustard*mustard_cal+onion*onion_cal
					print(count,"\t",bread,"\t",hot_dog,"\t",tomato,"\t",mustard,"\t",onion,"\t",total_cal)
					count += 1
