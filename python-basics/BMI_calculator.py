#Hello a little program to check your ideal body mass index 
weight = int(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: ")) 
height_square = height * height
ideal_bmi = weight / height_square

print(f"your ideal body mass index is {ideal_bmi:.2f}")

