class EvenNumbers:
    last = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.last += 2

        if self.last > 8:
            raise StopIteration

        return self.last

en = EvenNumbers()

for num in en:
    print(num)   