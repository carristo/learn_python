def discounted(price: float, discount: float, max_discount = 20) -> float:
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
        if discount > max_discount:
            return price
        return discount / 100 * price
    except (ValueError, TypeError):
        print('price и discount должны быть вещественными числами, max_discount должно быть целым числом')


print(discounted(100, 10))
print(discounted('asdf', 10))
print(discounted(100, 'asdf'))
print(discounted(100, 10, 'asdf'))
print(discounted(None, 10, 10))