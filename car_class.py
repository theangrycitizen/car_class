class Car(object):
  speed = 0

  def __init__(self, name='General', model='GM', car_type=None):
    self.name = name
    self.speed = 0
    self.model = model
    self.car_type = car_type


    if self.name in ['Porshe', 'Koenigsegg']:
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4

    if self.car_type == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4


  def is_saloon(self):
    if self.car_type is not 'trailer':
        self.car_type == 'saloon'
        return True
    return False

  def drive(self, moving_speed):
    if moving_speed == 3:
      self.speed = 1000
    elif moving_speed == 7:
      self.speed = 77

    return self