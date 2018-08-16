result = []
for bread in "1":
	for hot_dog in "01":
		for tomato in "01":
			for mustard in "01":	
				for onion in "01":
					result.append(bread+hot_dog+tomato+mustard+onion)
print(result)
print("一共有%d种组合。" % len(result))
