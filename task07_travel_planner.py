# Travel Planner
class travel_planner:
   def __init__(self,destination,distance,speed):
      self.destination = destination
      self.distance = distance
      self.speed = speed

   def time_travel(self):
    time = self.distance / self.speed
    return time 

   def time_converter(self):
    min = self.time / 60
    return min

   def __str__(self):
       print(f'Destination: {self.destination}')
       print(f'Distance: {self.distance} km')
       print(f'Average Speed: {self.speed} km/hr')
       print(f'Estimated Travel Time : {self.time_travle()} Hours')
       print(f'Travle Time in hr:min : {self.time}:{self.time_converter} hr')


destination = input('Enter your destination: ')
distance = float(input('Enter your distance: '))
speed = float(input('Enter the Average speed: '))

traveler_1 = travel_planner(destination,distance,speed)
print(traveler_1.__str__())