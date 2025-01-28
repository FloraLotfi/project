# باز کردن و خواندن فایل
with open("p.txt", "r") as file:
    content = file.readlines()

# حذف کاراکترهای اضافی مثل '\n' و تبدیل خطوط به لیست
result = [item for line in content for item in line.split()]

print(result)