my_dict = { 'Vasya' :1975 , 'Egor' : 1999 , 'Masha' :2002 }
print(my_dict)
print(my_dict['Masha'])
print(my_dict.get('Alex'))
my_dict.update({ 'Ekaterina' : 2005, 'Nikol' : 2014})
del my_dict['Egor']
print(my_dict)
my_set = {1, 1 ,1, 'Яблоко' , 'Яблоко' , 42.314}
print(my_set)
my_set.add( 8 )
my_set.add( 15 )
my_set.discard( 1 )
print(my_set)

