friends = ['Alex', 'Monica', 'Rachel', 'Ross']
print(f"Hello {friends[0]}")
print(f"Hello {friends[1]}")
print(f"Hello {friends[2]}")
print(f"Hello {friends[3]}")

friends[0] = 'Chandler'
print(f"Hello {friends[0]}")
print(f"Hello {friends[1]}")
print(f"Hello {friends[2]}")
print(f"Hello {friends[3]}")

friends.insert(0, 'Lennard')
friends.insert(2, 'Sheldon')
friends.append('Penny')

print(f"Hello {friends[0]}")
print(f"Hello {friends[1]}")
print(f"Hello {friends[2]}")
print(f"Hello {friends[3]}")
print(f"Hello {friends[4]}")
print(f"Hello {friends[5]}")
print(f"Hello {friends[6]}")

print(f"{friends.pop()} removed")
print(f"{friends.pop()} removed")
print(f"{friends.pop()} removed")
print(f"{friends.pop()} removed")
print(f"{friends.pop()} removed")

del friends[1]
del friends[0]


places = ['Mexico', 'China', 'Singapore', 'Australia', 'Hawaii']
print(places)
print(sorted(places))
print(sorted(places, reverse=True))
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)


print(len(places))
print(len(friends))

