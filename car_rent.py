age = int(input('enter your age: ')) 
name = input('enter your name: ')
if age >= 18:
    cars = ['BMW', 'SKODA', 'AUDI'] 
    bmw_models = {'bmw_m3': 5000, 'bmw_x7': 7000}
    skoda_models = {'skoda_1': 4500, 'skoda_2': 7400} 
    audi_models = {'audi_1': 6000, 'audi_2': 6400}
    print('enter the car which you want to borrow: ') 
    print(cars)
    selected_car = input()
    if selected_car == 'BMW':
        print('please select model')
        print(list(bmw_models.keys())) 
        selected_model = input()
        days = int(input('Enter how many days you want to borrow: ')) 
        charges = days * bmw_models[selected_model]
    elif selected_car == 'SKODA':
        print('please select model')
        print(list(skoda_models.keys())) 
        selected_model = input()
        days = int(input('Enter how many days you want to borrow: ')) 
        charges = days * skoda_models[selected_model] 
    else:
        pass
else:
    print('Your are not eligible to borrow the car')

print('Customer Name: ', name) 
print('Age: ', age) 
print('borrowed_days: ', days) 
print('Total charges: ', charges)