import random  # برای تولید مقادیر تصادفی در کروموزوم‌ها و جهش

# تابع ارزیابی (محاسبه تعداد برخوردها)
def fitness(chromosome):
    n = len(chromosome)
    clashes = 0
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == abs(i - j):
                clashes += 1
    return clashes
