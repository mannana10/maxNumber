
numbers = []  

print("მითხარი რიცხვები და მათ შორის მაქსიმალურს მარტივად გაპოვნინებ.\nპროგრამიდან გასასვლელად კოდური სიტყვაა 'გასვლა'.")

while True:
    num = input("\nშეიტანეთ რიცხვი: ")
    if num =="გასვლა":
         break
    elif num.isdigit():
        numbers.append(num)
    else:
        print("გთხოვთ შეიტანოთ რიცხვი!")
        continue

def find_max(numbers):
    return max(numbers)

maximum = find_max(numbers)

print(f"თქვენი შეტანილი რიცხვებიდან: {numbers}, მაქსიმალურია : {maximum}.")