import module_1
import module_2
import module_3

array = module_1.array
vector_gauss = module_2.vector_gauss
solve_out_of_the_box = module_1.solve_out_of_the_box
norm = module_1.norm
test_error = module_3.test_error


a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)
solution = vector_gauss(a, b)
oob_solution = solve_out_of_the_box(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))
print(test_error(vector_gauss))