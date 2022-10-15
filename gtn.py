# gen_1 = (i for i in range(10))
# gen_2 = [i for i in range(10)]
# list_ = []
# for i in range(10):
#     list_.append(i)
#
#
#
# for i in gen_1:
#     print(i)
#
# print(gen_2)

# def test_gen():
#     for i in range(10):
#         yield i
# for j in test_gen():
#     print(j)

def bus_ticket():
    numbers = [i for i in range(100000, 999999)]
    for i in numbers:
        number = [int(i) for i in str(i)]
        sum_ticket_1 = sum(number)
        if sum_ticket_1 % 7 ==0 and (sum_ticket_1 + 1) % 7 == 0:
            print(f'bilet {i} top')


bus_ticket()

