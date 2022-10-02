import csv

def process_csv(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        array = []
        for line in csv_reader:
            array = line
        
        results = []

        stable = [14.127292, 19.289649, 91.969033, 654.889104, 0.096360, 0.104341, 0.088799, 0.048919, 0.181162, 0.062798, 0.405172, 1.216853, 2.866059, 40.337079, 0.007041, 0.025478, 0.031894, 0.011796, 0.020542, 0.003795, 16.269190, 25.677223, 107.261213, 880.583128, 0.132369, 0.254265, 0.272188, 0.114606, 0.290076, 0.083946]
        # for i in range(0, 30):
        #     results.append(float(stable[i])-float(array[i])/float(stable[i]))

        # print(results)

        return results