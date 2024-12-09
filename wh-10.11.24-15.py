# start
import statistics

import random

# 1:
list_ak: list[int] = []
for i in range(50):
    ty = random.randint(1, 100)
    list_ak.append(ty)
print(list_ak)
z = statistics.mean(list_ak)
# print(z)
y = max(list_ak)
print(y)
# a:
print(list(filter(lambda num: num > 50, list_ak)))

# b:
print(list(filter(lambda num: num % 7 == 0, list_ak)))

# c:
print(list(filter(lambda num: 10 < num < 99, list_ak)))

# d:
print(list(filter(lambda num: num // 10 == num % 10, list_ak)))

# e:
print(list(filter(lambda num: num // 10 + num % 10 == 9, list_ak)))

# f:
print(list(filter(lambda num: num > z, list_ak)))

# g:
print(list(filter(lambda num: num > y // 2, list_ak)))

# 2:

plays: list[str] = ["V Auto Theft Grand ", "Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]

# a:
print(list(filter(lambda g: len(g) > 8, plays)))

# b:
print(list(filter(lambda g: g.startswith("F"), plays)))

# c:
print(list(filter(lambda g: g.count(' ') == 1, plays)))

# d:
print(list(filter(lambda g: "V" in g.upper(), plays)))

# 3:

cv: list[int] = []
for i in range(20 + 1):
    rt = random.randint(-50, 50)
    cv.append(rt)
print(cv)

# a:
print(list(map(lambda m: m ** 3, cv)))

# b:
print(list(map(lambda m: m % 10, cv)))

# c:
print(list(map(lambda m: m * 9 / 5 + 32, cv)))

# d: bonos
print(list(map(lambda m: "positive" if  m > 0 else "negative", cv)))


# 4:

grop:list[str]=["Strawberry", "Pineapple", "Grapes", "Watermelon" ,"Mango ","Orange ","Banana ","Apple ",]

# a:
print(list(map(lambda w:w[::-1],grop)))

# b:
print(list(map(lambda w:w [0],grop)))

# c:
print(list(map(lambda w: w.upper(),grop)))

# d:
print(list(map(lambda w:w[len(w)//2] if len(w)//2 % 2==0 else w[len(w)//2-1],grop)))

# e: bonos ניסיתי !!!

print(list(map(lambda w: w+"!" if w.endswith(s) else w),grop))




# 5:
# גלובל משמעותו להשתמש בתא זיכרון בכללי שקיים בקובץ  ןנוכל להשתמש בפונקציה בגלובל עצצן לדוגמא אם האיקס והוא תא זיכרון
# נוכל לכתוב פונקציה ולציין בתוכה את האיקס הגלובלי (שבתא זיכרון) אך לא מומלץ להשתמש בכך כי יכול להיות פוננקציה שמציינת רק את איקס ואם לא תהיה קיימת איקס בגלובל זה לא יופעל הפונקציה
# נקבל שגיאה בתרגיל שציינת עקב שהגדרת וביקשת שידפיס לך את הגלובל את האיקס ואז פתאום אתה רוצה לשנות בפונקציה את האיקס ולהגיד ששוה ל 4 זה יתן שגיאה כי קודם תשנה את שינויים שאתה רוצה או להגדיר ואז לבקש בתוך הפונקציה לעשות פעולה כי אזור לשנות את האיקס כי אפשר להגיע לגלובל אך לא כדי לשנות את הגלובל


# stop
