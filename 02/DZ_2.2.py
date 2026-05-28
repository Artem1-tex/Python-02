tot_time = input("Вкажіть кількість хвилин")

time = int(tot_time)

hours = time // 60
print(hours, "г")

mins = time % 60
print(mins, "хв")