from prettytable import PrettyTable
import matplotlib.pyplot as plt
from termcolor import cprint


def fun(x, y):
    if (typee == 1):
        return y + (1 + x) * (y * y)
    if (typee == 2):
        if (x == 0):
            x = 0.000000000000000000000000000000000001
            return y / x - 3
        else:
            return y / x - 3
    if (typee == 3):
        return x * x - 2 * y
    return


def runge(step, pr):
    start_x = x0
    end_x = end

    x_zero = x0
    y_zero = y0
    decimal_places = 3
    n = int((end_x - start_x) / step)

    functions_data = list()
    functions_data_mod1 = list()
    functions_data_mod2 = list()
    functions_data_mod3 = list()
    k1 = list()
    k2 = list()
    k3 = list()
    k4 = list()
    x_data = list()
    y_data = list()
    iter = list()

    iter.append(0)
    x_data.append(round(x_zero, decimal_places))
    y_data.append(round(y_zero, decimal_places))

    functions_data.append(round(fun(x_zero, y_zero), decimal_places))
    k1.append(round(step * functions_data[0], decimal_places))

    functions_data_mod1.append(round(fun(x_zero + step / 2, y_zero + k1[0] / 2), decimal_places))
    k2.append(round(step * functions_data_mod1[0], decimal_places))

    functions_data_mod2.append(round(fun(x_zero + step / 2, y_zero + k2[0] / 2), decimal_places))
    k3.append(round(step * functions_data_mod2[0], decimal_places))

    functions_data_mod3.append(round(fun(x_zero + step, y_zero + k3[0]), decimal_places))
    k4.append(round(step * functions_data_mod3[0], decimal_places))

    for i in range(n):
        iter.append(i + 1)
        start_x += step
        x_data.append(round(start_x, decimal_places))
        y_data.append(round(y_data[i] + (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6, decimal_places))

        if i != n - 1:
            functions_data.append(round(fun(x_data[i + 1], y_data[i + 1]), decimal_places))
            k1.append(round(step * functions_data[i + 1], decimal_places))

            functions_data_mod1.append(
                round(fun(x_data[i + 1] + step / 2, y_data[i + 1] + k1[i + 1] / 2), decimal_places))
            k2.append(round(step * functions_data_mod1[i + 1], decimal_places))

            functions_data_mod2.append(
                round(fun(x_data[i + 1] + step / 2, y_data[i + 1] + k2[i + 1] / 2), decimal_places))
            k3.append(round(step * functions_data_mod2[i + 1], decimal_places))

            functions_data_mod3.append(round(fun(x_data[i + 1] + step, y_data[i + 1] + k3[i + 1]), decimal_places))
            k4.append(round(step * functions_data_mod3[i + 1], decimal_places))
        else:
            functions_data.append(0)
            k1.append(0)

            functions_data_mod1.append(0)
            k2.append(0)

            functions_data_mod2.append(0)
            k3.append(0)

            functions_data_mod3.append(0)
            k4.append(0)

    t = PrettyTable()

    t.add_column("i", iter)
    t.add_column("Xi", x_data)
    t.add_column("Yi", y_data)
    t.add_column("Fi", functions_data)
    t.add_column("K1", k1)
    t.add_column("K2", k2)
    t.add_column("K3", k3)
    t.add_column("K4", k4)
    t.add_column("F(x0+h/2,y0+k1/2)", functions_data_mod1)
    t.add_column("F(x0+h/2,y0+k2/2)", functions_data_mod2)
    t.add_column("F(x0+h,y0+k3)", functions_data_mod3)

    if (pr):
        print(t)

    i = 4

    while i <= n:
        iter.append(i)
        y_pred = y_data[i - 1] + step * (
                55 * functions_data[i - 1] - 59 * functions_data[i - 2] + 37 * functions_data[i - 3] - 9 *
                functions_data[i - 4]) / 24
        start_x += step
        f = 0
        y_cor = y_pred
        a = 0
        while abs(y_cor - a) > eps:
            a = y_cor
            f = fun(start_x, a)
            y_cor = y_data[i - 1] + step * (
                    9 * f + 19 * functions_data[i - 1] - 5 * functions_data[i - 2] + functions_data[i - 3]) / 24

        y_data.append(round(y_cor, decimal_places))
        functions_data.append(round(f, decimal_places))
        x_data.append(round(start_x, decimal_places))
        i += 1

    print("Эта таблица со всеми вычисленными значениями дополняем первую таблицу с i = 4")
    t = PrettyTable()
    t.add_column("i", iter)
    t.add_column("Xi", x_data)
    t.add_column("Yi", y_data)
    t.add_column("Fi", functions_data)
    if (pr):
        print(t)
    return x_data, y_data


def adams(step, pr):
    start_x = x0
    end_x = end

    x_zero = x0
    y_zero = y0

    decimal_places = 3
    n = int((end_x - start_x) / step)

    functions_data = list()
    functions_data_mod1 = list()
    functions_data_mod2 = list()
    functions_data_mod3 = list()
    k1 = list()
    k2 = list()
    k3 = list()
    k4 = list()
    x_data = list()
    y_data = list()
    iter = list()

    iter.append(0)
    x_data.append(round(x_zero, decimal_places))
    y_data.append(round(y_zero, decimal_places))

    functions_data.append(round(fun(x_zero, y_zero), decimal_places))
    k1.append(round(step * functions_data[0], decimal_places))

    functions_data_mod1.append(round(fun(x_zero + step / 2, y_zero + k1[0] / 2), decimal_places))
    k2.append(round(step * functions_data_mod1[0], decimal_places))

    functions_data_mod2.append(round(fun(x_zero + step / 2, y_zero + k2[0] / 2), decimal_places))
    k3.append(round(step * functions_data_mod2[0], decimal_places))

    functions_data_mod3.append(round(fun(x_zero + step, y_zero + k3[0]), decimal_places))
    k4.append(round(step * functions_data_mod3[0], decimal_places))

    for i in range(3):
        iter.append(i + 1)
        start_x += step
        x_data.append(round(start_x, decimal_places))
        y_data.append(round(y_data[i] + (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6, decimal_places))

        functions_data.append(round(fun(x_data[i + 1], y_data[i + 1]), decimal_places))
        k1.append(round(step * functions_data[i + 1], decimal_places))

        functions_data_mod1.append(round(fun(x_data[i + 1] + step / 2, y_data[i + 1] + k1[i + 1] / 2), decimal_places))
        k2.append(round(step * functions_data_mod1[i + 1], decimal_places))

        functions_data_mod2.append(round(fun(x_data[i + 1] + step / 2, y_data[i + 1] + k2[i + 1] / 2), decimal_places))
        k3.append(round(step * functions_data_mod2[i + 1], decimal_places))

        functions_data_mod3.append(round(fun(x_data[i + 1] + step, y_data[i + 1] + k3[i + 1]), decimal_places))
        k4.append(round(step * functions_data_mod3[i + 1], decimal_places))

    t = PrettyTable()

    t.add_column("i", iter)
    t.add_column("Xi", x_data)
    t.add_column("Yi", y_data)
    t.add_column("Fi", functions_data)
    t.add_column("K1", k1)
    t.add_column("K2", k2)
    t.add_column("K3", k3)
    t.add_column("K4", k4)
    t.add_column("F(x0+h/2,y0+k1/2)", functions_data_mod1)
    t.add_column("F(x0+h/2,y0+k2/2)", functions_data_mod2)
    t.add_column("F(x0+h,y0+k3)", functions_data_mod3)

    if (pr):
        print(t)

    i = 4

    while i <= n:
        iter.append(i)
        y_pred = y_data[i - 1] + step * (
                55 * functions_data[i - 1] - 59 * functions_data[i - 2] + 37 * functions_data[i - 3] - 9 *
                functions_data[i - 4]) / 24
        start_x += step
        f = 0
        y_cor = y_pred
        a = 0
        while abs(y_cor - a) > eps:
            a = y_cor
            f = fun(start_x, a)
            y_cor = y_data[i - 1] + step * (
                    9 * f + 19 * functions_data[i - 1] - 5 * functions_data[i - 2] + functions_data[i - 3]) / 24

        y_data.append(round(y_cor, decimal_places))
        functions_data.append(round(f, decimal_places))
        x_data.append(round(start_x, decimal_places))
        i += 1

    print("Эта таблица со всеми вычисленными значениями дополняем первую таблицу с i = 4")
    t = PrettyTable()
    t.add_column("i", iter)
    t.add_column("Xi", x_data)
    t.add_column("Yi", y_data)
    t.add_column("Fi", functions_data)
    if (pr):
        print(t)
    return x_data, y_data


def chooseType():
    print("Please choose a equation:\n"
          "\t1. y' = y + (1+x)y^2\n"
          "\t2. y' = y/x - 3\n"
          "\t3. y' = x^2 - 2y")
    while 1:
        try:
            answer = int(input("Type: ").strip())
            if answer < 1 or answer > 4:
                answer = 1
                print("По умолчанию выбрано 1")
                return answer
                break
            else:
                return answer
                break
        except ValueError:
            print("ошибка, такого числа нет")
            continue
        except TypeError:
            print("ошибка, введите число")
            continue


def chooseXY():
    while 1:
        try:
            x0answ = float(input("X0: ").strip())
            y0answ = float(input("Y0: ").strip())
            Endansw = float(input("интервал до: [ " + str(x0answ) + " ; ? ]: ").strip())
            print("[ " + str(x0answ) + " ; " + str(Endansw) + " ]")
            eps = float(input("точность: ").strip())
            step = float(input("шаг: ").strip())
            return x0answ, y0answ, Endansw, eps, step

        except ValueError:
            print("ошибка, такого числа нет")
            continue
        except TypeError:
            print("ошибка, введите число")
            continue


def draw_graph(x, y, equation, name):
    try:
        "\t1. y' = y + (1+x)y^2\n"
        "\t2. y' = y/x - 3\n"
        "\t3. y' = x^2 - 2y"
        eq_name = {1: "y' = y + (1+x)y^2",
                   2: "y' = y/x - 3",
                   3: "y' = x^2 - 2y"}
        ax = plt.gca()
        plt.grid()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.title(name + ": график уравнения " + eq_name[equation])
        plt.plot(x, y, color='r', linewidth=2)
        for i in range(len(x)):
            plt.scatter(x[i], y[i], color='r', s=20)
        plt.show()
    except ValueError:
        return
    except ZeroDivisionError:
        return


while (1):
    typee = chooseType()
    x0, y0, end, eps, step = chooseXY()
    flag = True
    h = step
    while (flag):
        eeflag = True
        runge0_5 = runge(h / 2, False)[1]
        runge1 = runge(h, False)[1]
        k = 0
        for i in range(len(runge1)):
            k = k + 1
            if ((runge1[i] - runge0_5[i * 2]) / 1) > eps:
                h = h / 2
                print("Точность на шаге " + str(k) + " мала, шаг уменьшен до " + str(h))
                eeflag = False
                break

        if eeflag != False:
            cprint('\n__________Эйлера метод_________', 'cyan', attrs=['bold'])
            print("Шаг:" + str(h))
            x, y = runge(h, True)
            draw_graph(x, y, typee, "Рунге-Кутта")
            break

    flag = True
    while (flag):
        n = int((end - x0) / step)
        if (n < 6):
            print("Метод Адамса не работает")
            break

        eeflag = True
        adams0_5 = runge(h / 2, False)[1]
        adams1 = runge(h, False)[1]
        k = 0
        for i in range(len(runge1)):
            k = k + 1
            if ((adams1[i] - adams0_5[i * 2]) / 1) > eps:
                h = h / 2
                print("Точность на шаге " + str(k) + " мала, шаг уменьшен до " + str(h))
                eeflag = False
                break

        if eeflag != False:
            cprint('\n_________Адамса метод_________', 'cyan', attrs=['bold'])
            print("Шаг:" + str(h))
            x, y = adams(h, True)
            draw_graph(x, y, typee, "Адамс")
            break