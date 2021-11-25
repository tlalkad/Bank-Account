#!/usr/bin/env python
# coding: utf-8
import tkinter
import pickle


class BankAccount:
    def __init__(self, balance, name, accnt_nr, acc_type):
        self.__balance = balance
        self.__name = name
        self.__accnt_nr = accnt_nr
        self.__acc_type = acc_type

    def set_balance(self, balance):
        self.__balance = balance

    def set_name(self, name):
        self.__name = name

    def set_accnt_nr(self, accnt_nr):
        self.__accnt_nr = accnt_nr

    def set_acc_type(self, acc_type):
        self.__acc_type = acc_type

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def get_accnt_nr(self):
        return self.__accnt_nr

    def get_acc_type(self):
        return self.__acc_type

    def __str__(self):
        return (
                f'Bank name: {self.get_name()},'
                f'account type: {self.get_acc_type()},'
                f'account number: {self.get_accnt_nr()},'
                f'account balance: {self.get_balance()}'
                )


class BankAccount_INT(BankAccount):
    def __init__(self, balance, name, accnt_nr, acc_type, currency):
        BankAccount.__init__(self, balance, name, accnt_nr, acc_type)

        self.__currency = currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_currency(self):
        return self.__currency

    def __str__(self):
        return (
                f'Bank name: {self.get_name()},'
                f'account type: {self.get_acc_type()},'
                f'account number: {self.get_accnt_nr()},'
                f'account balance: {self.get_balance()},'
                f'currency: {self.get_currency()}'
                )


class BankAccount_COVID19(BankAccount):
    def __init__(self, balance, name, accnt_nr, acc_type, pesel):
        BankAccount.__init__(self, balance, name, accnt_nr, acc_type)

        self.__pesel = pesel

    def set_pesel(self, pesel):
        self.__pesel = pesel

    def get_pesel(self):
        return self.__pesel

    def __str__(self):
        return (
                f'Bank name: {self.get_name()},'
                f'account type: {self.get_acc_type()},'
                f'account number: {self.get_accnt_nr()},'
                f'account balance: {self.get_balance()},'
                f'pesel: {self.get_pesel()}'
                )


class BankAccount_COVID19_company(BankAccount):
    def __init__(self, balance, name, accnt_nr, acc_type, nip):
        BankAccount.__init__(self, balance, name, accnt_nr, acc_type)
        self.__nip = nip

    def set_nip(self, nip):
        self.__nip = nip

    def get_nip(self):
        return self.__nip

    def __str__(self):
        return (
                f'Bank name: {self.get_name()},'
                f'account type: {self.get_acc_type()},'
                f'account number: {self.get_accnt_nr()},'
                f'account balance: {self.get_balance()},'
                f'nip: {self.get_nip()}'
                )


class TestAvg:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.minsize(250, 300)
        self.typ_frame = tkinter.Frame(self.main_window)

        self.logo = tkinter.Canvas(self.main_window, bg ="yellow", height = 600, width = 600)
        self.logo.pack()
        self.img = tkinter.PhotoImage(file='logo.png')
        self.logo.create_image(300, 300, image=self.img)

        self.balance_frame = tkinter.Frame(self.main_window)
        self.name_frame = tkinter.Frame(self.main_window)
        self.accnt_nr_frame = tkinter.Frame(self.main_window)
        self.acc_type_frame = tkinter.Frame(self.main_window)
        self.extra_info = tkinter.Frame(self.main_window)

        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.next_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var2 = tkinter.IntVar()
        self.balance_var = tkinter.StringVar()
        self.accnt_nr_var = tkinter.StringVar()
        self.acc_type_var = tkinter.StringVar()
        self.name_var = tkinter.StringVar()
        self.extra_var = tkinter.StringVar()

        self.radio_var.set(0)

        self.rb1 = tkinter.Radiobutton(
                                        self.acc_type_frame,
                                        text='BankAccount_INT ',
                                        font=('Verdana', 15),
                                        variable=self.radio_var, value=1
                                        )
        self.rb2 = tkinter.Radiobutton(
                                        self.acc_type_frame,
                                        text='BankAccount_COVID19',
                                        font=('Verdana', 15),
                                        variable=self.radio_var, value=2
                                        )
        self.rb3 = tkinter.Radiobutton(
                                        self.acc_type_frame,
                                        text='BankAccount_COVID19_company',
                                        font=('Verdana', 15),
                                        variable=self.radio_var, value=3
                                        )

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.balance_label = tkinter.Label(
                                        self.balance_frame,
                                        text='Balance: ',
                                        font=('Verdana', 15)
                                        )
        self.balance_entry = tkinter.Entry(self.balance_frame, width=10)
        self.balance_label.pack(side='left')
        self.balance_entry.pack(side='left')

        self.name_label = tkinter.Label(
                                        self.name_frame,
                                        text='Account name: ',
                                        font=('Verdana', 15)
                                        )
        self.name_entry = tkinter.Entry(self.name_frame, width=10)
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.accnt_nr_label = tkinter.Label(
                                          self.accnt_nr_frame,
                                          text='Account number: ',
                                          font=('Verdana', 15)
                                          )
        self.accnt_nr_entry = tkinter.Entry(self.accnt_nr_frame, width=10)
        self.accnt_nr_label.pack(side='left')
        self.accnt_nr_entry.pack(side='left')

        self.extra_label = tkinter.Label(
                                        self.extra_info,
                                        text=(
                                            'Extra info: BankAccount_INT - currency, '
                                            'BankAccount_COVID19 - PESEL, '
                                            'BankAccount_COVID19_company - nip'
                                            ),
                                        font=('Verdana', 15)
                                        )
        self.extra_entry = tkinter.Entry(self.extra_info, width=10)
        self.extra_label.pack(side='left')
        self.extra_entry.pack(side='left')

        self.info_label = tkinter.Label(
                                        self.info_frame,
                                        text='Acc data:',
                                        font=('Verdana', 15)
                                        )

        self.info = tkinter.StringVar()

        self.info_label2 = tkinter.Label(
                                        self.info_frame,
                                        textvariable=self.info
                                        )
        self.info_label.pack(side='left')
        self.info_label2.pack(side='left')

        self.add_button = tkinter.Button(
                                        self.button_frame,
                                        text='Add account',
                                        font=('Verdana', 15),
                                        command=self.add_account
                                        )
        self.quit_button = tkinter.Button(
                                        self.button_frame,
                                        text='Quit',
                                        font=('Verdana', 15),
                                        command=self.main_window.destroy
                                        )
        self.add_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.radio_var2.set(1)

        self.rb1_2 = tkinter.Radiobutton(
                                        self.next_frame,
                                        text='Add another account ',
                                        font=('Verdana', 13),
                                        variable=self.radio_var2, value=1
                                        )

        self.rb2_2 = tkinter.Radiobutton(
                                        self.next_frame,
                                        text='Finish adding accounts',
                                        font=('Verdana', 13),
                                        variable=self.radio_var2,
                                        value=2
                                        )

        self.rb1_2.pack()
        self.rb2_2.pack()

        self.acc_type_frame.pack()
        self.name_frame.pack()
        self.accnt_nr_frame.pack()
        self.balance_frame.pack()
        self.extra_info.pack()
        self.info_frame.pack()
        self.button_frame.pack()
        self.next_frame.pack()

        tkinter.mainloop()

    def add_account(self):
        if self.radio_var.get() == 1:
            self.acc_type_var.set('BankAccount_INT')
        elif self.radio_var.get() == 2:
            self.acc_type_var.set('BankAccount_COVID19')
        elif self.radio_var.get() == 3:
            self.acc_type_var.set('BankAccount_COVID19_company')
        else:
            self.acc_type_var.set('Unknown')

        self.balance_var.set(self.balance_entry.get())
        self.name_var.set(self.name_entry.get())
        self.accnt_nr_var.set(self.accnt_nr_entry.get())
        self.acc_type_var.set(self.acc_type_var.get())
        self.extra_var.set(self.extra_entry.get())
        self.info.set((
            f'Account type: {self.acc_type_var.get()}, '
            f'name: {self.name_var.get()}, '
            f'Balance: {self.balance_var.get()}, '
            f'number: {self.accnt_nr_var.get()}, '
            f'extra_info: {self.extra_var.get()} '
        ))


FILENAME = 'account.dat'
output_file = open(FILENAME, 'wb')
again = 1
while again == 1:
    test_avg = TestAvg()

    balance = test_avg.balance_var.get()
    name = test_avg.name_var.get()
    accnt_nr = test_avg.accnt_nr_var.get()
    acc_type = test_avg.acc_type_var.get()
    extra_info = test_avg.extra_var.get()

    if test_avg.radio_var.get() == 1:
        account = BankAccount_INT(balance, name, accnt_nr, acc_type, extra_info)
    elif test_avg.radio_var.get() == 2:
        account = BankAccount_COVID19(balance, name, accnt_nr, acc_type, extra_info)
    elif test_avg.radio_var.get() == 3:
        account = BankAccount_COVID19_company(balance, name, accnt_nr, acc_type, extra_info)
    else:
        print("Incorrect account type - using default type")
        account = BankAccount(balance, name, accnt_nr, acc_type)

    pickle.dump(account, output_file)
    again = test_avg.radio_var2.get()

output_file.close()
print('Account data saved here: ', FILENAME)


FILENAME = 'account.dat'


def main():
    end_of_file = False
    input_file = open(FILENAME, 'rb')
    while not end_of_file:
        try:
            account = pickle.load(input_file)
            print(account)
        except EOFError:
            end_of_file = True
    input_file.close()


main()
