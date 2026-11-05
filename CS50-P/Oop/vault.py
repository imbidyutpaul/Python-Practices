class Vault:
  def __init__(self, galleons=0, sickles=0, knuts=0):
    self.galleons = galleons
    self.sickles = sickles
    self.knuts = knuts
  
  def __str__(self):
    return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
  
  def __add__(self, other):
    galleons = self.galleons + other.galleons
    sickles = self.sickles + other.sickles
    knuts = self.knuts + self.knuts
    return Vault(galleons, sickles, knuts)

Potter = Vault(100, 50, 25)
print("Potter's have", Potter)

Weasley = Vault(25, 50, 100)
print("Weasley's have", Weasley)

total = Potter + Weasley
print("Total was", total)