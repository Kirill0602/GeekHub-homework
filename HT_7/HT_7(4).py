def my_generator(gen):
    b = 0
    while True:
        try:
            yield gen[b]
        except IndexError:
            b = 0
            yield gen[b]
        b += 1
 
 
a = my_generator([1, 2, 3])

