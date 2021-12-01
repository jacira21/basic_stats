def basic_stats(x):
    #This is a module to compute basic statics mean (mu), standard deviation (sigma).
    #This module also produces a graph (fig) of the distribution of elements in the sample.

    import matplotlib.pyplot as plt

    #Determine the length of x
    N = 0
    for i in x:
        N += 1

    # Compute the mean of the elements in list x
    mu = 0
    for i in x:
        mu_i = i/N
        mu += mu_i

    # Compute the std deviation, using the mean and the elements in list x.

    #list2 = [(element-mean)**2 for element in list1]
    sumTerm = 0
    for i in x:
        termSq = (i - mu)**2
        sumTerm += termSq
    sigma = (sumTerm**.5)/(N-1)

    # Count the number of values that are within +/- 1 std. deviation of the mean.  
    # A normal distribution will have approx. 68% of the values within this range.  
    # Based on this criteria is the list normally distributed?

#     sumSig = 0
#     for i in x:
#         if abs(i - mu) <= sigma:
#             sumSig += 1
#     stdPct = 100 * (sumSig / N)
#     print(stdPct,'% of the sample elements are within 1 standard deviation of the mean')

    # Use print() and if statements to report a message about whether the data is normally distributed.
#     if stdPct >= 68:
#          print('The sample is normally distributed.')
#     else:
#          print('The sample is not normally distributed.')

    ### Use Matplotlb.pyplot to make a histogram of x.
    fig = plt.figure()
    plt.hist(x, bins=19)
    plt.title('Frequency Distribution of Sample Data')
    plt.ylabel('Frequency')
    plt.xlabel('Data')
    plt.close(fig)

#     #Calculate skewness and determine whether the sample is normally distributed
#     sumG = 0
#     for i in x:
#         G = ((i - mu)/sigma)**3
#         sumG += G
#     skew = (N/((N-1)*(N-2)))*sumG
#     print(skew)
#     print('The skewness of the sample is', skew)
#     print('The sample is not normally distributed')

    return mu, sigma, fig
