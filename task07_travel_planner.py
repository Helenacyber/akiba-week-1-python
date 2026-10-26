# Travel Planner
class travle_planner:
   def __init__(self,destination,distance,speed):
      self.destination = destination
      self.distance = distance
      self.speed = speed

   def time_travle(self):
    time = self.distance / self.speed
    return time 