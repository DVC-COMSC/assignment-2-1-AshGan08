def main():
    num_male = int(input("# of male students: "))
    num_fem = int(input("# of female students: "))

    total = num_male + num_fem

    m_perc = float((num_male / (num_fem + num_male)) *100)
    f_perc = float((num_fem / (num_fem + num_male)) *100)

    return total, num_male, num_fem, m_perc, f_perc


if __name__ == '__main__':
    print(main())
