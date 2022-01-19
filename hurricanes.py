# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def update_damages(damages, conversion):
  updated_damages = []
  for damage in damages:    
    if damage == 'Damages not recorded':
      updated_damages.append(damage)
    elif damage[-1] == "M":
      cost = float(damage[:-1]) * conversion.get("M")
      updated_damages.append(cost)
    else:
      cost = float(damage[:-1]) * conversion.get("B")
      updated_damages.append(cost)
  return updated_damages

# test function by updating damages
damage = update_damages(damages, conversion)

# 2 
# Create a Table
#{"Cuba I": {'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}}

def create_dict(names, months, years, max_sustained_winds, areas_affected, deaths):
  hurricanes = {}
  num_hurricanes = len(names)
  for i in range(num_hurricanes):
    hurricanes[names[i]] = {"Name": names[i],
                            "Month": months[i],
                            "Year": years[i],
                            "Max Sustained Wind": max_sustained_winds[i],
                            "Areas Affected": areas_affected[i],
                            "Damage": damage[i],
                            "Deaths": deaths[i]}
  return hurricanes

# Create and view the hurricanes dictionary
hurricanes_dict = create_dict(names, months, years, max_sustained_winds, areas_affected, deaths)
#print(hurricanes_dict)

# 3
# Organizing by Year
def hurricanes_by_year(hurricanes):
  hurricanes_year = {}
  for key, value in hurricanes.items():
    current_year = hurricanes[key]["Year"]
    if not hurricanes_year.get(current_year):
      hurricanes_year[current_year] = [value]
    else:
      hurricanes_year[current_year].append(value)
  return hurricanes_year

# create a new dictionary of hurricanes with year and key
hurricanes_by_year(hurricanes_dict)

# 4
# Counting Damaged Areas
def affected_areas(hurricanes):
  affected_areas_dict = {}
  for key, value in hurricanes.items():
    for area in hurricanes[key]["Areas Affected"]:
      if area not in affected_areas_dict:
        count = 1
      else:
        count += 1
      affected_areas_dict[area] = count
  return affected_areas_dict

# create dictionary of areas to store the number of hurricanes involved in
areas_dict = affected_areas(hurricanes_dict)

# 5 
# Calculating Maximum Hurricane Count
def max_count(areas):
  max_area = "Central America"
  max_area_count = 2
  for key in areas:
    if areas[key] > max_area_count:
      max_area_count = areas[key]
      max_area = key
  return f"The most affected area is {max_area} with {max_area_count} hurricanes."
print(max_count(areas_dict))

#alternative solution
def max_affected(areas):
  max_affected_sorted = {key: value for key, value in sorted(areas.items(), key= lambda x:x[1], reverse=True)}
  max_affected = list(max_affected_sorted.items())[0]
  return f"The most affected area is {max_affected[0]} with {max_affected[1]} hurricanes."

# find most frequently affected area and the number of hurricanes involved in
print(max_affected(areas_dict))

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(hurricanes):
  nr_deaths = 0
  most_deadly = ""
  for key, value in hurricanes.items():
    if hurricanes[key]["Deaths"] > nr_deaths:
      nr_deaths = hurricanes[key]["Deaths"]
      most_deadly = hurricanes[key]["Name"]
  return f"The most deadly hurricane was {most_deadly} with {nr_deaths} deaths."

# find highest mortality hurricane and the number of deaths
print(deadliest_hurricane(hurricanes_dict))

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

# categorize hurricanes in new dictionary with mortality severity as key
def hurricane_mortality(scale, hurricanes):
  hurricanes_by_mortality = {key:[] for key in scale}
  # {mortality rating: [{hurricane}, {hurricane}]}
  for key, value in hurricanes.items():
    mortality = hurricanes[key]["Deaths"]
    if mortality == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricanes[key]["Name"])
    elif mortality <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricanes[key]["Name"])
    elif mortality <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricanes[key]["Name"])
    elif mortality <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricanes[key]["Name"])
    elif mortality <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricanes[key]["Name"])
    else:
      hurricanes_by_mortality[5] = []
      hurricanes_by_mortality[5].append(hurricanes[key]["Name"])
  return hurricanes_by_mortality

print(hurricane_mortality(mortality_scale, hurricanes_dict))

# 8 Calculating Hurricane Maximum Damage
def highest_damage(hurricanes):
  biggest_damage = 0
  most_costly_hurr = ""
  for key, value in hurricanes.items():
    if type(hurricanes[key]["Damage"]) == str:
      continue
    elif hurricanes[key]["Damage"] > biggest_damage:
      biggest_damage = hurricanes[key]["Damage"]
      most_costly_hurr = hurricanes[key]["Name"]
  return f"The most damaging hurricane was {most_costly_hurr} that caused {biggest_damage} dollars of damage."


# find highest damage inducing hurricane and its total cost
print(highest_damage(hurricanes_dict))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def hurricanes_by_damage(hurricanes, scale):
  hurricanes_by_damage = {key:[] for key in scale}  
  for key, value in hurricanes.items():
    dmg = hurricanes[key]["Damage"]
    if type(dmg) == str or dmg == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricanes[key]["Name"])
    elif dmg <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes[key]["Name"])
    elif dmg <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes[key]["Name"])
    elif dmg <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes[key]["Name"])
    elif dmg <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes[key]["Name"])
    else:
      hurricanes_by_damage[5] = []
      hurricanes_by_damage[5].append(hurricanes[key]["Name"])
  return hurricanes_by_damage

print(hurricanes_by_damage(hurricanes_dict, damage_scale))