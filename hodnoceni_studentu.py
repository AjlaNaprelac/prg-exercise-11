class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None
    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)
    def get_by_index(self, index):
        return self.scores[index]
    def get_grade(self, index):
        score= self.scores[index]

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else: return "F"

    def find(self, score):
        index= []
        for i in range(len(self.scores)):
            if self.socres[i] == scores:
                index.append(i)
        return index
    def get_sorted(self):
        scores = self.scores[:]
        n= len(scores)
        for j in range(0, n - i - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
        return scores
    def  find_sorted(self, score):
        if self.sorted_scores is None:
            self._sorted_scores= self.get_sorted()
        left = 0
        right= len(self._sorted_scores) - 1
        while left <= right:
            midd= (left + right) // 2
            if self._sorted_scores[midd] == score:
                return midd
            elif self._sorted_scores[midd] < score:
                left= midd + 1
            else: right = midd + 1
        return None
    def main():
        results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
        print(results.count())
        for i in range(results.count()):
            print(f"student{i}: {results.get_by_index(i)} points - {results.get_grade(i)}")

            print(results.finf(100))
            print(results.get_sorted())
            from sorting import random_numbers
            random_results = StudentsGrades(random_numbers(30, 0, 100))
            print(random_results.count())
            print(random_results.get_sorted())

            print(results.find_sorted(91))
            print(results.find_sorted(50))
            print(results.find_sorted(77))
    if __name__ == "__main__":
        main()
