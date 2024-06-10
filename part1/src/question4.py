import src.pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """

select an.name, an.species, an.age from animals as an where an.animal_id NOT IN (select animal_id from animals as a inner join people_animals as pa on a.animal_id = pa.pet_id); 

"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """

select count(a.age) from animals as a inner join people_animals as pa on a.animal_id = pa.pet_id inner join people as p on pa.owner_id = p.person_id where a.age > p.age

"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 

select p1.name, a1.name, a1.species from animals as a1 
inner join people_animals as pa1 on a1.animal_id = pa1.pet_id 
inner join people as p1 on pa1.owner_id = p1.person_id 
where p1.name like 'bessie' and a1.animal_id not in
(select a2.animal_id from animals as a2 
inner join people_animals as pa2 on a2.animal_id = pa2.pet_id 
inner join people as p2 on pa2.owner_id = p2.person_id 
group by  a2.animal_id, a2.name
having count(p2.person_id)  > 1)

"""