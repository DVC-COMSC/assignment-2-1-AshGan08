def main():
    num_male = int(input("# of male students: "))
    num_fem = int(input("# of female students: "))

    total = num_male + num_fem

    m_perc = float((num_male / (num_fem + num_male)) *100)
    f_perc = float((num_fem / (num_fem + num_male)) *100)

    return total, num_male, num_fem, m_perc, f_perc


if __name__ == '__main__':
    total, num_male, num_fem, m_perc, f_perc = main() 
    print (f'Calculating Total students within classroom \t {total: .2f}')
    print (f'Calculating male students in class \t {num_male: .2f}')
    print (f'Calculating female students in class \t {num_fem: .2f}')
    print (f'Calculating female percentages within classroom \t {f_perc: .2f}')
    print (f'Calculating male percentages within classroom \t {m_perc: .2f}')
