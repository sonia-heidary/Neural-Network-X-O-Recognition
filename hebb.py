class Hebb:
    def __init__(self, inputs: list):
        self.inputs = [] # this a list of lists where each list represents one input
        self.targets = [] # this is a list of target where the target out put of the self.inputs[i] can be found in self.targets[i]
        self.weight = [] # weights of the variables
        self.bios = 1
        self.weight_bios = 0
        for i in range(0, len(inputs)):
            # only the inputs that have targets will be considered
            if inputs[i][0] and inputs[i][1]:
                self.inputs.append(inputs[i][0])
                self.targets.append(inputs[i][1])

        self.hebb()

    def hebb(self):
        for i in range(0, len(self.inputs)):
            self.weight_bios += self.bios * self.targets[i]
            for j in range(0, len(self.inputs[i])):
                if j >= len(self.weight):
                    self.weight.append(0)
                self.weight[j] += self.inputs[i][j] * self.targets[i]
