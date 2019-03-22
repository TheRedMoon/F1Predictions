from re import sub

scores = []
ranklist = []
filename = "permierleague.txt"
file = open(filename, encoding ="utf8")
lines =  [line.replace("-\n", "") for line in file]
for line in lines:
	if "-" in line:
		scores.append(line)
for score in scores:
	bothteams = score.split("-")
	firstteam = bothteams[0]
	secondteam = bothteams[1]
	firstteamnamewhitespaces = sub(r'\d+', '', firstteam)
	secondteamnamewhitespaces = sub(r'\d+', '', secondteam)
	firstteamname = firstteamnamewhitespaces.rstrip()
	secondteamname = secondteamnamewhitespaces.rstrip()
	scorefirstteam = [int(s) for s in firstteam.split() if s.isdigit()]
	scoresecondteam = [int(s) for s in secondteam.split() if s.isdigit()]
	if (scorefirstteam[0] > scoresecondteam[0]):
		teamexists = False
		for i in range(len(ranklist)):
			x,y = ranklist[i]
			if x == firstteamname:
				teamexists = True
				ranklist[i] = (x,y+3) 
				break
		if(teamexists == False):
			ranklist.append((firstteamname, 3))
	elif (scorefirstteam[0] < scoresecondteam[0]):
		teamexists = False
		for i in range(len(ranklist)):
			x,y = ranklist[i]
			if x == secondteamname:
				teamexists = True
				ranklist[i] = (x,y+3) 
				break
		if(teamexists == False):
			ranklist.append((secondteamname, 3))	
	else:
		teamexists = False
		for i in range(len(ranklist)):
			x,y = ranklist[i]
			if x == firstteamname:
				teamexists = True
				ranklist[i] = (x,y+1) 
				break
		if(teamexists == False):
			ranklist.append((firstteamname, 1))
		teamexists = False
		for i in range(len(ranklist)):
			x,y = ranklist[i]
			if x == secondteamname:
				teamexists = True
				ranklist[i] = (x,y+1) 
				break
		if(teamexists == False):
			ranklist.append((secondteamname, 1))
sortedrankedlist = ranklist.sort(key=lambda elem: elem[1])
output = open("Output.txt", "w")
resultstring = ""
rankedlist = list(reversed(ranklist))
for i in range(len(rankedlist)):
	x,y = rankedlist[i]
	resultstring += "Rank: " + str(i) + " Team: " + x + " with score: " + str(y) + "\n"
output.write(resultstring)
output.close()
print(resultstring)

