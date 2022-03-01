def volume_sphere(R):
    return (4 * 3.14 * R**3)/3

r=int(input("Enter radius of sphere: "))
v=round(volume_sphere(r),2)
print(f"Volume of sphere: {v}")