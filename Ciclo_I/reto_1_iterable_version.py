"""
PROBLEMA #I:
Un profesor debe calcular el promedio de la nota de quinces de sus estudiantes para
subirla a la plataforma de notas finales. Sin embargo, el profesor acordó con sus
estudiantes que los ayudará eliminando la peor de las 5 notas antes de calcular el
promedio que finalmente resportará. Adicionalmente, el profesor se ha dado cuenta
que las notas registradas en su plantailla se encuentra en una escala de números
enteros entre 0 y 100, pero la plataforma está diseñada para recibir el promedio
únicamente en la escala estandar de la universidad de 0 a 5, redondeado a 2 decimales.

REQUERIMIENTOS:
Escriba una funcion que reciba una cadena con el codigo alfanumerico del estudiante
y cinco números enteros (n1, n2, n3, n4, n5), que representa las notas de los quinces
del semestre y retorne una cadena de caracteres que le proporciona al profesor la
información que desea obtener. La cadena debe de tener la siguiente estructura: "El
promedio ajustado del estudiantes [codigo] es [promedio]" donde, el promedio reportado
debe cumplir con las siguientes especificaciones mencionadas anteriormente (redondeando
a dos decimales, en escala de 0 a 5 y eliminando del calculo la peor de las 5 notas del
estudiante).

#TEST
    print(quizzes_grade("AA0010276", 19, 90, 38, 55, 68))
    print(quizzes_grade("IS0020162", 37, 10, 50, 19, 79))
    print(quizzes_grade("BIO220181", 45, 46, 33, 74, 22))
    print(quizzes_grade("IQ1022018", 57, 100, 87, 93, 21))
    print(quizzes_grade("MA0020152", 5, 14, 76, 91, 5))

#OUTPUT
    El promedio ajsutado del estudiante AA0010276 es: 3.14
    El promedio ajustado del estudiante IS0020162 es: 2.31
    El promedio ajustado del estudiante BIO220181 es: 2.48
    El promedio ajustado del estudiante IQ1022018 es: 4.21
    El promedio ajustado del estudiante MA0020152 es: 2.33
"""

if __name__ == '__main__':

    # Variables iniciales

    run = True
    mutable_grade = 100
    current_grades = []

    # Loop principal

    while run:

        # Ingreso del codigo y validacion

        student_code = input("Ingrese el codigo alfanumerico del estudiante: ")

        while not isinstance(student_code, str):
            student_code = input("Por favor ingrese un codigo valido: ")

        # Loop de llenado y validacion de notas

        for iterator in range(5):

            grade = int(input("Ingresa la nota " + str(iterator + 1) + ": "))

            while not isinstance(grade, int) or grade > 100 or grade < 0:
                grade = int(input("Por favor ingrese una nota valida: "))

            current_grades.append(grade * 0.05)

        # Primera seccion de mostrado

        print("El estudiante: " + "\n" + student_code.center(45))
        print("\n" + "Tiene por notas".center(45, "_"))

        for current in current_grades:
            print("{:20}{:0.2f}{:>20}".format("|", current, "|"))

        print("{:-^45}".format(""))

        # Busqueda y muestra de la peor nota

        for current in current_grades:
            if mutable_grade > current:
                mutable_grade = current

        print("{:_^45}".format("") + "\n" + "La peor nota fue".center(45, "-") + "\n" +
              str(mutable_grade).center(45, "-") + "\n" + "{:-^45}".format("") + "\n")

        # Calculo y muestra del promedio

        mutable_grade *= -1

        for current in current_grades:
            mutable_grade += current

        mutable_grade /= len(current_grades) - 1

        print("{:#^45}".format("") + "\n" + " La nota final es ".center(45, "#") + "\n" +
              str(mutable_grade).center(45, "#") + "\n" + "{:#^45}".format("") + "\n")

        # Validacion de continuacion

        if input("¿Deseas continuar? [s/n]: ") == 'n':
            run = False
        else:
            mutable_grade = 100
            current_grades = []
