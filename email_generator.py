class EmailGenerator:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()

    def generator(self):
        f_email = self.first_name+'@gmail.com'
        f_l_email = self.first_name+self.last_name+'@gmail.com'
        f_n_email = self.first_name+'70'+'@gmail.com'
        all_email = self.first_name[0]+self.last_name+'_70@gmail.com'

        print('These are some possible emails you can try:', end='\n')
        print(
            f_email,
            f_l_email,
            f_n_email,
            all_email,
        end='\n', sep='\n')


name = EmailGenerator('Linux', 'Tolvard')
print(name.generator())
