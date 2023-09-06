def main():
    
    ##################################################
    # m_perc = 40
    # f_perc = 60
    
    m_students = int(input())
    f_students = int(input())

    total_students = m_students + f_students
    m_perc = m_students / total_students
    f_perc = f_students / total_students
    
    print (total_students)
    print (m_perc)
    print (f_perc)
    ##################################################
    

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
