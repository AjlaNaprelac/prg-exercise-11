from sorting import random_numbers
def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.count())
    for i in range(result.count()):
        print(f"student{i}: {result.get_by_index(i)} points - {result.get_grade(i)}")

        print(results.finf(100))
        print(results.get_sorted())

        random_results = StudentsGrades(random_numbers(30, 0, 100))
        print(random_results.count())
        print(random_results.get_sorted())

        print(results.find_sorted(91))
        print(results.find_sorted(50))
        print(results.find_sorted(77))
    main()