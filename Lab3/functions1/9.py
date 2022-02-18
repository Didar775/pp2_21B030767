def volume_sphere(R):
    return (4*3.14*r**3)/3

r = int(input("Enter your radius: "))
k = round(volume_sphere(r),3)
print(f"Volume of the sphere = {k} meter cube")