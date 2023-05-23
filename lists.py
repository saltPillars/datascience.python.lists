# List Exercises 2

# 3-8 Seeing the World
travel_locations = ['japan', 'greece', 'germany', 'wales']
print(travel_locations)
print("\nsorted()")
print(sorted(travel_locations))
print(travel_locations)
print(sorted(travel_locations, reverse=True))
print(travel_locations)

travel_locations.reverse()
print("\nreverse()")
print(travel_locations)
travel_locations.reverse()
print(travel_locations)

travel_locations.sort()
print("\nsort()")
print(travel_locations)
travel_locations.sort(reverse=True)
print(travel_locations)

# 3-9 Locations
print(f"\nI want to travel to {len(travel_locations)} locations!")