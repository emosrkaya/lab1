import random

def create_random_list(n, lower_bound=-12, upper_bound=24):
    """
    Verilmiş n sayda təsadüfi tam ədədlərdən ibarət siyahı yaradır.
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]

def product_of_even_index_elements(lst):
    """
    Verilmiş siyahının cüt indeksli elementlərinin hasilini hesablayır.
    """
    product = 1
    for i in range(0, len(lst), 2):
        product *= lst[i]
    return product

random_list = create_random_list(n)
print("Təsadüfi siyahı:", random_list)

result = product_of_even_index_elements(random_list)
print("Cüt indeksli elementlərin hasili:", result)
