# bool логический тип данных, может принимать одно из двух значений, True | False
is_rainy: bool = True
cats_can_fly: bool = False

# not- логическое отрицание
print(not is_rainy)
print(not cats_can_fly)

# and- логическое И (конъюнкция)
print(is_rainy and cats_can_fly)

# or- логическое или (дизъюнкция)
print(is_rainy or cats_can_fly)

# ==- логическая эквиваленция (только для логического типа)
print(is_rainy == cats_can_fly)
