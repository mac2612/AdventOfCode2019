
locations = {}

dir = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}

with open('input.txt', 'r') as fp:
    wire = 0
    for line in fp:
      moves = line.strip('\n').split(',')
      location = (0,0)
      steps = 0
      for move in moves:
          direction = move[0]
          amount = int(move[1:])
          print(f'command {move} start location {location}')
          for os in range(1, amount+1):
            steps += 1
            location = (location[0] + (1 * dir[direction][0]), location[1] + (1 * dir[direction][1]))
            if location not in locations:
                locations[location] = {}
            if wire not in locations[location]:
              locations[location][wire] = steps
            else:
              locations[location][wire] = min(locations[location][wire], wire)
      wire += 1

distances = []
steps = []
for location, wiresteps in locations.items():
    if len(wiresteps) >= 2:
      steps.append(sum(wiresteps.values()))
      distances.append(abs(location[0]) + abs(location[1]))

print(f"Min steps: {min(steps)}")
print(f"Min distance: {min(distances)}")
