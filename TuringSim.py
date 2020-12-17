

class TM:
    BLANK = ' '
    """A simple turing machine simulator"""
    def __init__(self):
        self.tuples = []
        self.get_input()
        self.tape = list(input("Enter the initial tape and press enter.\n"))
        self.tape.append(TM.BLANK)
        self.num_iter = int(input("Maximum Iterations: "))
        self.state = self.tuples[0][0]
        self.index = 0
        self.run()

    def get_input(self):
        print("Enter 5-Tuples. A . by itself to end.")
        in_tuple = "_"
        while in_tuple != '.':
            self.tuples.append(in_tuple)
            in_tuple = input()
        self.tuples.pop(0)

    def run(self):
        tup = self.get_tuple()
        self.print_state()
        while tup and self.num_iter > 0:
            self.tape[self.index] = tup[2]
            self.state = tup[4]
            self.update_index(tup[3])
            self.print_state()
            tup = self.get_tuple()
            self.num_iter -= 1

    def get_tuple(self):
        t_id = self.state + self.tape[self.index]
        return [tup for tup in self.tuples if tup.startswith(t_id)][0]  # ew

    def update_index(self, motion):
        if motion == 'N':
            return
        elif motion == 'R':
            if self.index == len(self.tape)-1:
                self.tape.append(TM.BLANK)
            self.index += 1
        elif motion == 'R' and self.index == 0:
            self.tape.insert(0, TM.BLANK)
        else:
            self.index -= 1

    def print_state(self):
        print("".join(self.tape[:self.index]),
              "{", f"{self.state}", "}",
              "".join(self.tape[self.index:]), sep='')


if __name__ == '__main__':
    a = TM()
