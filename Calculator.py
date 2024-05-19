'''!
    \brief Класс с функционалом калькулятора.

    Данный класс предоставляет функционал разных математических операций для шаблоных типов.
'''
class Calculator:
    def __init__(self):
        pass


    def add(self, x, y):
        '''!
                \brief Шаблонная функция суммирования двух чисел

                \param [in] x Первый объект, который нужно сложить
                \param [in] y Второй объект, который нужно сложить

                \return Сумма *x* и *y*.
            '''
        return x + y


    def subtract(self, x, y):
        '''!
                \brief Шаблонная функция вычитания двух чисел

                \param [in] x Первый объект, из которого нужно вычесть
                \param [in] y Второй объект, который нужно вычесть

                \return Разница *x* и *y*.
            '''
        return x - y

    def multiply(self, x, y):
        '''!
                \brief Шаблонная функция умножения двух чисел

                \param [in] x Первый объект, который нужно умножить
                \param [in] y Второй объект, который нужно умножить

                \return Произведение *x* и *y*.
            '''
        return x * y

    def divide(self, x, y):
        '''!
            \brief Шаблонная функция деления двух чисел

            \param [in] x Первый объект, числитель
            \param [in] y Второй объект, знаменатель

            \return Частное *x* и *y*.
        '''
        if y == 0:
            raise ValueError("Division by zero is undefined")
        return x / y
