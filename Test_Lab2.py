import Lab2

def test_find_min_max():
   num_list=[12,8,23,45,67,89]
   assert Lab2.calc_min_max_temperature(num_list)==[8,89]

def test_calc_average():
   num_list=[5,10,15,20]
   assert Lab2.calc_average_temperature(num_list)==12.5

def test_calc_median_temperature():
   num_list=[5,10,15,20]
   assert Lab2.calc_median_temperature(num_list)==12.5
