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
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:
def new_damage(ls1):
    new_damages = []
    for elements in ls1:
        if elements.startswith('Damages'):
            new_damages.append(elements)
        elif elements[-1] == 'M':
            elements = elements[:-1]
            elements = float(elements)
            elements = elements * 1000000
            new_damages.append(elements)
        elif elements[-1] == 'B':
            elements = elements[:-1]
            elements = float(elements)
            elements = elements * 1000000000
            new_damages.append(elements)
    return new_damages


updated_damages = new_damage(damages)
# write your construct hurricane dictionary function here:
def hurricans_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurrican_dict = {}
    index = len(names)
    for i in range(index):
        hurrican_dict[names[i]] = {'Name' : names[i],
                                'Month' : months[i],
                                'Year' : years[i],
                                'Max. Sustained Winds' : max_sustained_winds[i],
                                'Areas affected' : areas_affected[i],
                                'Damage' : damages [i],
                                'Deaths' : deaths[i]}
    return hurrican_dict


hurrican_information = hurricans_dict(
    names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurrican_information)

# write your construct hurricane by year dictionary function here:

def year_dict(hurricanes):
    hurricanes_by_year = dict()
    for cane in hurricanes:
        current_year = hurricanes[cane]['Year']
        current_cane = hurricanes[cane]
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [current_cane]
        else:
            hurricanes_by_year[current_year].append(current_cane)
    return hurricanes_by_year

#print(year_dict(hurrican_information))




# write your count affected areas function here:
def most_affected_areas(hurricanes):
    areas_dict = {}
    area_list = []
    for cane in hurricanes:
        areas = hurricanes[cane]['Areas affected']
        for area in areas:
            area_list.append(area)
        for a in area_list:
            areas_dict[a] = area_list.count(a)
    return areas_dict


ranking_areas = most_affected_areas(hurrican_information)

# write your find most affected area function here:
def most_affected_area(Areas):
    count = 0
    for value in Areas.values():
        if value > count:
            count = value
        else:
            continue
    for key, value in Areas.items():
        if value == count:
            return key, value

top_area_affected = most_affected_area(ranking_areas)

#print(top_area_affected)
        
# write your greatest number of deaths function here:
def maximun_number_deaths(hurricanes):
    biggest_death_count = 0
    hurrican_murderer = ''
    for cane in hurricanes:
        death = hurricanes[cane]['Deaths']
        if death > biggest_death_count:
            biggest_death_count = death
            hurrican_murderer = hurricanes[cane]['Name']
    return hurrican_murderer, biggest_death_count 

deadliest_hurricane = maximun_number_deaths(hurrican_information)

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def death_ranking_hurricane(hurricanes):
    ranked_hurricanes = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : []}
    for cane in hurricanes:
        current_cane = hurricanes[cane]
        if hurricanes[cane]['Deaths'] == 0:
            ranked_hurricanes[0].append(current_cane)
        elif hurricanes[cane]['Deaths'] <= 100:
            ranked_hurricanes[1].append(current_cane)
        elif hurricanes[cane]['Deaths'] <= 500:
            ranked_hurricanes[2].append(current_cane)
        elif hurricanes[cane]['Deaths'] <= 1000:
            ranked_hurricanes[3].append(current_cane)
        elif hurricanes[cane]['Deaths'] <= 10000:
            ranked_hurricanes[4].append(current_cane)
        else:
            ranked_hurricanes[5].append(current_cane)
    return ranked_hurricanes
              
#print(death_ranking_hurricane(hurrican_information))

# write your catgeorize by mortality function here:


def maximun_damage(hurricanes):
    most_damage = 0
    hurrican_expensive = ''
    for cane in hurricanes:
        try:
            top_damage = float(hurricanes[cane]['Damage'])
            if top_damage > most_damage:
                most_damage = top_damage
                hurrican_expensive = hurricanes[cane]['Name']
        except:
            continue
    return hurrican_expensive, most_damage

costly_hurricane = maximun_damage(hurrican_information)

#print(f'{costly_hurricane[0]} was the most costly hurricane in history with a damage valued in USD {costly_hurricane[1]}.')
        
def hurricanes_by_damage(hurricanes):
    ranking_by_damage = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : []}
    for cane in hurricanes:
        current_cane = hurricanes[cane]
        if hurricanes[cane]['Damage'] == 0 or hurricanes[cane]['Damage'] == 'Damages not recorded':
            ranking_by_damage[0].append(current_cane)
        elif hurricanes[cane]['Damage'] <= 100000000:
            ranking_by_damage[1].append(current_cane)
        elif hurricanes[cane]['Damage'] <= 1000000000:
            ranking_by_damage[2].append(current_cane)
        elif hurricanes[cane]['Damage'] <= 10000000000:
            ranking_by_damage[3].append(current_cane)
        elif hurricanes[cane]['Damage'] <= 50000000000:
            ranking_by_damage[4].append(current_cane)
        else:
            ranking_by_damage[5].append(current_cane)
    return ranking_by_damage 

              
print(hurricanes_by_damage(hurrican_information))







# write your greatest damage function here:







# write your catgeorize by damage function here:
