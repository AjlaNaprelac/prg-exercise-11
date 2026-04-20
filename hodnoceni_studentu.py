class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

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
    def  find_sorted(self, scores):
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

