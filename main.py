import Gui as g
import sys
import tkinter.messagebox as mb


def main():
    g.Latte_Entry.insert("end", "0")
    g.Latte_price.insert("end","500")
    g.Espresso_Entry.insert("end", "0")
    g.Espresso_price.insert("end","1000")
    g.Iced_latte_Entry.insert("end", "0")
    g.Iced_latte_price.insert("end","1000")
    g.SexOn_Entry.insert("end", "0")
    g.sexOn_price.insert("end","1500")
    g.Cappucino_Entry.insert("end", "0")
    g.Cappucino_price.insert("end","1000")
    g.Frappé_Entry.insert("end", "0")
    g.Frappe_price.insert("end","1500")
    g.Doppio_Entry.insert("end", "0")
    g.Doppio_price.insert("end","2000")
    g.Iced_cap_Entry.insert("end", "0")
    g.Iced_cap_price.insert("end","1500")
    g.Mojito_Entry.insert("end", "0")
    g.Mojito_price.insert("end","1000")
    g.Cheese_Entry.insert("end", "0")
    g.Cheese_price.insert("end","1000")
    g.Red_Entry.insert("end", "0")
    g.Red_price.insert("end","1000")
    g.Pasta_Entry.insert("end", "0")
    g.Pasta_price.insert("end","8000")
    g.lasagna_Entry.insert("end", "0")
    g.lasagna_price.insert("end","6000")
    g.Carnitas_Entry.insert("end", "0")
    g.Carnitas_price.insert("end","5000")
    g.Cheeseburger_Entry.insert("end", "0")
    g.CheeseBurger_price.insert("end","8000")
    g.Layered_Entry.insert("end", "0")
    g.Layered_price.insert("end","20000")
    g.choc_Entry.insert("end", "0")
    g.choc_price.insert("end","9000")
    g.Reuben_Entry.insert("end", "0")
    g.Reuben_price.insert("end","8000")
    g.listbox_Drinks.insert("end", "0")
    g.listbox_Cakes.insert("end", "0")
    g.Total_Listbox.insert("end", "0")
    g.Cash_Entry.insert("end", "0")
    g.listbox_Remain.insert("end", "0")
    
    g.Checkbutton_Latte.insert("end","Latte")
    g.Espresso_Checkbutton.insert("end","Hot Choclate")
    g.Iced_cap_Checkbutton.insert("end","Iced Latte")
    g.SexOn_Checkbutton.insert("end","Tea")
    g.Cappucino_Checkbutton.insert("end","Cappuccino")
    g.Frappé_Checkbutton.insert("end","Orange Juice")
    g.Doppio_Checkbutton.insert("end","Ice Cream ")
    g.Iced_cap_Checkbutton2.insert("end","Iced Tea")
    g.Mojito_Checkbutton.insert("end","Mohito")
    ###########################################################
    g.Cheese_Checkbutton.insert("end","Cheese Cake")
    g.Red_Checkbutton.insert("end","Dolma")
    g.Pasta_Checkbutton.insert("end","Pasta")
    g.lasagna_Checkbutton.insert("end","Kabab")
    g.Carnitas_Checkbutton.insert("end","Kuba")
    g.Cheeseburger_Checkbutton.insert("end","Cheeseburger")
    g.Layered_Checkbutton.insert("end","Kintaki")
    g.choc_Checkbutton.insert("end","Tabula")
    g.Reuben_Checkbutton.insert("end","Fish")







    g.listbox.insert("end", "=================================================")
    g.listbox.insert("end", "                                           RESTAURANT BILLING SYSTEM")
    g.listbox.insert("end", "=================================================")

    g.window.mainloop()


def reset():
    m = mb.askyesno("SYSTEM ALERT", "Are You Sure Reset All..! \n")

    if m >= 1:
        g.Latte_Entry.delete(0, 5)
        g.Espresso_Entry.delete(0, 5)
        g.Iced_latte_Entry.delete(0, 5)
        g.SexOn_Entry.delete(0, 5)
        g.Cappucino_Entry.delete(0, 5)
        g.Frappé_Entry.delete(0, 5)
        g.Doppio_Entry.delete(0, 5)
        g.Iced_cap_Entry.delete(0, 5)
        g.Mojito_Entry.delete(0, 5)
        g.Cheese_Entry.delete(0, 5)
        g.Red_Entry.delete(0, 5)
        g.Pasta_Entry.delete(0, 5)
        g.lasagna_Entry.delete(0, 5)
        g.Carnitas_Entry.delete(0, 5)
        g.Cheeseburger_Entry.delete(0, 5)
        g.Layered_Entry.delete(0, 5)
        g.choc_Entry.delete(0, 5)
        g.Reuben_Entry.delete(0, 5)
        g.listbox_Drinks.delete(0, 5)
        g.listbox_Cakes.delete(0, 5)
    
        g.Total_Listbox.delete(0, 5)
        g.Cash_Entry.delete(0, 5)
        g.listbox_Remain.delete(0, 5)
        g.Entry_Cal.delete(0, 10)
        g.table_Entry.delete(0,5)
        g.Latte_Entry.insert("end", "0")
        g.Espresso_Entry.insert("end", "0")
        g.Iced_latte_Entry.insert("end", "0")
        g.SexOn_Entry.insert("end", "0")
        g.Cappucino_Entry.insert("end", "0")
        g.Frappé_Entry.insert("end", "0")
        g.Doppio_Entry.insert("end", "0")
        g.Iced_cap_Entry.insert("end", "0")
        g.Mojito_Entry.insert("end", "0")
        g.Cheese_Entry.insert("end", "0")
        g.Red_Entry.insert("end", "0")
        g.Pasta_Entry.insert("end", "0")
        g.lasagna_Entry.insert("end", "0")
        g.Carnitas_Entry.insert("end", "0")
        g.Cheeseburger_Entry.insert("end", "0")
        g.Layered_Entry.insert("end", "0")
        g.choc_Entry.insert("end", "0")
        g.Reuben_Entry.insert("end", "0")
        g.listbox_Drinks.insert("end", "0")
        g.listbox_Cakes.insert("end", "0")
        g.Total_Listbox.insert("end", "0")
        g.Cash_Entry.insert("end", "0")
        g.listbox_Remain.insert("end", "0")

        g.var1.set(value=0)
        g.var2.set(value=0)
        g.var3.set(value=0)
        g.var4.set(value=0)
        g.var5.set(value=0)
        g.var6.set(value=0)
        g.var7.set(value=0)
        g.var8.set(value=0)
        g.var9.set(value=0)
        g.var10.set(value=0)
        g.var11.set(value=0)
        g.var12.set(value=0)
        g.var13.set(value=0)
        g.var14.set(value=0)
        g.var15.set(value=0)
        g.var16.set(value=0)
        g.var17.set(value=0)
        g.var18.set(value=0)

        g.listbox.delete(0, 20)
        g.listbox.insert("end", "=================================================")
        g.listbox.insert("end", "                                           RESTAURANT BILLING SYSTEM")
        g.listbox.insert("end", "=================================================")

    else:
        mb.showinfo("SYSTEM ALERT", "Canceled")


def total():
    l = int(g.Latte_Entry.get())
    e = int(g.Espresso_Entry.get())
    il = int(g.Iced_latte_Entry.get())
    v = int(g.SexOn_Entry.get())
    c = int(g.Cappucino_Entry.get())
    af = int(g.Frappé_Entry.get())
    am = int(g.Doppio_Entry.get())
    ic = int(g.Iced_cap_Entry.get())
    im = int(g.Mojito_Entry.get())
    sc = int(g.Cheese_Entry.get())
    su = int(g.Red_Entry.get())
    j = int(g.Pasta_Entry.get())
    w = int(g.lasagna_Entry.get())
    lc = int(g.Carnitas_Entry.get())
    k = int(g.Cheeseburger_Entry.get())
    ck = int(g.Layered_Entry.get())
    q = int(g.choc_Entry.get())
    p = int(g.Reuben_Entry.get())

#########################################################3
    Latte=int(g.Latte_price.get())
    Espresso=int(g.Espresso_price.get())
    Iced_latte=int(g.Iced_latte_price.get())
    SexOn=int(g.sexOn_price.get())
    Cappucino=int(g.Cappucino_price.get())
    Frappé=int(g.Frappe_price.get())
    Doppio=int(g.Doppio_price.get())
    Iced_cap=int(g.Iced_cap_price.get())
    Mojito=int(g.Mojito_price.get())
    Cheese=int(g.Cheese_price.get())
    Red=int(g.Red_price.get())
    Pasta=int(g.Pasta_price.get())
    lasagna=int(g.lasagna_price.get())
    Carnitas=int(g.Carnitas_price.get())
    Cheeseburger=int(g.CheeseBurger_price.get())
    Layered=int(g.Layered_price.get())
    choc=int(g.choc_price.get())
    Reuben=int(g.Reuben_price.get())
    ##################################################
    ll = Latte * l
    ee = Espresso * e
    ilil = Iced_latte * il
    vv = SexOn * v
    cc = Cappucino * c
    aaf = Frappé * af
    aam = Doppio * am
    icic = Iced_cap * ic
    imim = Mojito * im
    ssc = Cheese * sc
    ssu = Red * su
    jj = Pasta * j
    ww = lasagna * w
    llc = Carnitas * lc
    kk = Cheeseburger * k
    cck = Layered * ck
    qq = choc * q
    pp = Reuben * p

    drink = ll + ee + ilil + vv + cc + aaf + aam + icic + imim

    cake = ssc + ssu + jj + ww + llc + kk + cck + qq + pp


    full_total = drink + cake 

    g.listbox_Drinks.delete(0, 5)
    g.listbox_Cakes.delete(0, 5)
    g.Total_Listbox.delete(0, 5)
    g.listbox_Drinks.insert("end", "IQD " + str('%.0f' % drink))
    g.listbox_Cakes.insert("end", "IQD " + str('%.0f' % cake))
    g.Total_Listbox.insert("end", "IQD " + str('%.0f' % full_total))

    cash = int(g.Cash_Entry.get())
    remain = 0

    if cash != 0:
        remain = cash - full_total
        g.listbox_Remain.delete(0, 5)
        g.Entry_Cal.delete(0, 5)
        g.listbox_Remain.insert("end", "IQD " + str('%.0f' % remain))


    return drink, cake, full_total, ll, ee, ilil, vv, cc, aaf, aam, icic, imim, ssc, ssu, jj, ww, llc, kk, cck, qq, pp, remain

def recipt():
    total_tuple = total()
    g.listbox.delete(0, 20)
    g.listbox.insert("end", "=================================================")
    g.listbox.insert("end", ("Ref : " + str(g.table_Entry.get())+ "                          RESTAURANT BILLING SYSTEM"))
    g.listbox.insert("end", "=================================================")
    g.listbox.insert("end", "                                                 ")
    g.listbox.insert("end", "           Items                             Number of Items                              Total")
    g.listbox.insert("end", "                                                 ")
    if g.var1.get() >= 1: g.listbox.insert("end", "     {}                                              {}                                    {}".format(g.Checkbutton_Latte.get(),g.Latte_Entry.get(), total_tuple[3]))
    if g.var2.get() >= 1: g.listbox.insert("end", "     {}                                    {}                                            {}".format(g.Espresso_Checkbutton.get(),g.Espresso_Entry.get(), total_tuple[4]))
    if g.var3.get() >= 1: g.listbox.insert("end", "     {}                                      {}                                            {}".format(g.Iced_cap_Checkbutton.get(),g.Iced_latte_Entry.get(), total_tuple[5]))
    if g.var4.get() >= 1: g.listbox.insert("end", "     {}                                                   {}                                {}".format(g.SexOn_Checkbutton.get(),g.SexOn_Entry.get(), total_tuple[6]))
    if g.var5.get() >= 1: g.listbox.insert("end", "     {}                                      {}                                            {}".format(g.Cappucino_Checkbutton.get(),g.Cappucino_Entry.get(), total_tuple[7]))
    if g.var6.get() >= 1: g.listbox.insert("end", "     {}                                   {}                                            {}".format(g.Frappé_Checkbutton.get(),g.Frappé_Entry.get(), total_tuple[8]))
    if g.var7.get() >= 1: g.listbox.insert("end", "     {}                                           {}                                      {}".format(g.Doppio_Checkbutton.get(),g.Doppio_Entry.get(), total_tuple[9]))
    if g.var8.get() >= 1: g.listbox.insert("end", "     {}                                            {}                                       {}".format(g.Iced_cap_Checkbutton2.get(),g.Iced_cap_Entry.get(), total_tuple[10]))
    if g.var9.get() >= 1: g.listbox.insert("end", "     {}                                              {}                                      {}".format(g.Mojito_Checkbutton.get(),g.Mojito_Entry.get(), total_tuple[11]))
    if g.var10.get() >= 1: g.listbox.insert("end","    {}                                         {}                                           {}".format(g.Cheese_Checkbutton.get(),g.Cheese_Entry.get(), total_tuple[12]))
    if g.var11.get() >= 1: g.listbox.insert("end","    {}                                                {}                                {}".format(g.Red_Checkbutton.get(),g.Red_Entry.get(), total_tuple[13]))
    if g.var12.get() >= 1: g.listbox.insert("end","    {}                                                 {}                                  {}".format(g.Pasta_Checkbutton.get(),g.Pasta_Entry.get(), total_tuple[14]))
    if g.var13.get() >= 1: g.listbox.insert("end","   {}                                                 {}                                   {}".format(g.lasagna_Checkbutton.get(),g.lasagna_Entry.get(), total_tuple[15]))
    if g.var14.get() >= 1: g.listbox.insert("end","    {}                                                 {}                               {}".format(g.Carnitas_Checkbutton.get(),g.Carnitas_Entry.get(), total_tuple[16]))
    if g.var15.get() >= 1: g.listbox.insert("end","    {}                                            {}                                          {}".format(g.Cheeseburger_Checkbutton.get(),g.Cheeseburger_Entry.get(), total_tuple[17]))
    if g.var16.get() >= 1: g.listbox.insert("end","    {}                                             {}                                {}".format(g.Layered_Checkbutton.get(),g.Layered_Entry.get(), total_tuple[18]))
    if g.var17.get() >= 1: g.listbox.insert("end","    {}                                                 {}                               {}".format(g.choc_Checkbutton.get(),g.choc_Entry.get(), total_tuple[19]))
    if g.var18.get() >= 1: g.listbox.insert("end","    {}                                                        {}                               {}".format(g.Reuben_Checkbutton.get(),g.Reuben_Entry.get(), total_tuple[20]))

    g.listbox.insert("end", "                                                 ")
    g.listbox.insert("end", "=================================================")
    g.listbox.insert("end", "                                                 ")
    g.listbox.insert("end", ("     Cost of Drinks : " + "                                                                            IQD " + str('%.0f' % total_tuple[0])))
    g.listbox.insert("end", ("     Cost of Food Items : " + "                                                                    IQD " + str('%.0f' % total_tuple[1])))
    g.listbox.insert("end", ("     Total : " + "                                                                                           IQD " + str('%.0f' % total_tuple[2])))
    if float(g.Cash_Entry.get()) != 0: g.listbox.insert("end", "     Cash                                                                                              IQD {}".format('%.0f' % float(g.Cash_Entry.get())))
    if float(g.Cash_Entry.get()) != 0: g.listbox.insert("end", "     Remain                                                                                           IQD {}".format('%.0f' % float(total_tuple[21])))

    g.listbox.insert("end", "                                                 ")
    g.listbox.insert("end", "=================================================")


def exit_window():
    m = mb.askyesno("SYSTEM ALERT", "Are You Sure Exit From System \n")
    if m >= 1:
        sys.exit()

    else:
        mb.showinfo("SYSTEM ALERT", "Canceled")


calculator = ""


def set_number7():
    global calculator
    calculator = calculator + "7"
    g.Entry_Cal.insert("end", "7")


def set_number8():
    global calculator
    calculator = calculator + "8"
    g.Entry_Cal.insert("end", "8")


def set_number9():
    global calculator
    calculator = calculator + "9"
    g.Entry_Cal.insert("end", "9")


def set_number6():
    global calculator
    calculator = calculator + "6"
    g.Entry_Cal.insert("end", "6")


def set_number5():
    global calculator
    calculator = calculator + "5"
    g.Entry_Cal.insert("end", "5")


def set_number4():
    global calculator
    calculator = calculator + "4"
    g.Entry_Cal.insert("end", "4")


def set_number3():
    global calculator
    calculator = calculator + "3"
    g.Entry_Cal.insert("end", "3")


def set_number2():
    global calculator
    calculator = calculator + "2"
    g.Entry_Cal.insert("end", "2")


def set_number1():
    global calculator
    calculator = calculator + "1"
    g.Entry_Cal.insert("end", "1")


def set_number0():
    global calculator
    calculator = calculator + "0"
    g.Entry_Cal.insert("end", "0")


def set_number_plus():
    global calculator
    calculator = calculator + " + "
    g.Entry_Cal.insert("end", " + ")


def set_number_minus():
    global calculator
    calculator = calculator + " - "
    g.Entry_Cal.insert("end", " - ")


def set_number_div():
    global calculator
    calculator = calculator + " / "
    g.Entry_Cal.insert("end", " / ")


def set_number_sub():
    global calculator
    calculator = calculator + " * "
    g.Entry_Cal.insert("end", " * ")


def set_number_dot():
    global calculator
    calculator = calculator + "."
    g.Entry_Cal.insert("end", ".")


def equal():
    g.Entry_Cal.delete(0, 50)
    global calculator
    g.Entry_Cal.insert("end", eval(calculator))


def clear():
    global calculator
    calculator = ""
    g.Entry_Cal.delete(0, 50)



if __name__ == '__main__':
    main()
