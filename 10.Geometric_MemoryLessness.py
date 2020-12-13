import numpy as np
import matplotlib.pyplot as plt
def count_frequencies( data, relative = True):
    counter = {} # dictionary
    
    for element in data:
        if element not in counter:
            counter[element]=1
        else:
            counter[element]+=1
    if relative == True:
        for element in counter:
            counter[element] = counter[element] / len(data)
    return counter

def generateGeometricSamples(p=0.2,reps = 10000):
    samples = np.random.geometric(p,reps)
    return samples

def generateGeometricSamplesConditional(p=0.2, k=3, reps = 20000):
    samples = np.random.geometric(p,reps)
    samples = samples[samples>k] #only take samples where samples > k
    samples -= k
    return samples

reps = 10000
p=0.2
samples1 = generateGeometricSamples(p,reps)

samples2 = generateGeometricSamplesConditional(p) # simulate x-k|X>k
samples2 = samples2[:reps]

freq1 = count_frequencies(samples1)
freq2 = count_frequencies(samples2)

plt.figure(0)
plt.bar(freq1.keys(), freq1.values())
plt.figure(1)
plt.bar(freq2.keys(), freq2.values())
plt.show()

