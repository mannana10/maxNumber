
numbers = []
print("მითხარი რიცხვები და მათ შორის მაქსიმალურს მარტივად გაპოვნინებ.\nპროგრამიდან გასასვლელად კოდური სიტყვაა 'გასვლა'.")

while True:
    num = input("\nშეიტანეთ რიცხვი: ")
    if num == "გასვლა":
        break
    try:
        number = float(num)
        numbers.append(number)
    except ValueError:
        print("გთხოვთ შეიტანოთ  რიცხვი სწორი ფორმატით (მაგ., 3, 2.5, ან -1)!")

if numbers:    #თუ  ერთი რიცხვი მაინც შეიტანა მომხმარებელმა
    def find_max(numbers):
        return max(numbers)

    maximum = find_max(numbers)
    print(f"\nთქვენი შეტანილი რიცხვებიდან: {numbers}, მაქსიმალურია : {maximum}.")
else:
    print("\nრიცხვები არ არის შეტანილი.")
