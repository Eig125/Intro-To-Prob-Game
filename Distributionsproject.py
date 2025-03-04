import math as m
import random as rdm
import numpy as np

print("Hello aspiring Mathematician! Select your Random Variable:")
print("1. Discrete")
print("2. Continuous")
print("3. Just what is a Random Variable?")
choice = input("Enter choice (1/2/3):")
if choice in ('1', '2', '3'):
    if choice == '2':
        print("what type of continuous distribution would you like to view?")
        print("a. Normal")
        print("b. Uniform")
        print("c. Exponential")
        choice = input("Enter choice (a/b/c):")
        if choice in ('a', 'b', 'c'):
            if choice == 'a':
                import matplotlib.pyplot as plt
                mean = 100  # Average UK IQ score
                std_dev = 15  # Standard deviation of UK IQ scores

                # Generate IQ scores based on a normalal distribution
                iq_scores = np.random.normal(mean, std_dev, 1000)

                # Plot the histogram of IQ scores
                plt.hist(iq_scores, bins=30, density=True, alpha=0.7)
                plt.xlabel('IQ Score')
                plt.ylabel('Probability Density')
                plt.title('Distribution of IQ Scores')
                plt.grid(True)

                # Get user input for their IQ value
                value = float(input("Enter your IQ value:"))


                # Calculate the probability density at the user's IQ value
                result = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((value - mean) / std_dev) ** 2)


                # Plot a vertical line at the user's IQ value
                plt.axvline(x=value, color='r', linestyle='--', label='Your IQ')


                # Find the rank of the user's IQ value among UK IQ scores
                rank = np.sum(iq_scores <= value) / len(iq_scores)

                # Add a marker for the user's rank on the plot

                plt.annotate(f'Your Rank: {rank:.2%}', xy=(value, result), xytext=(value, result + 0.01),
                             arrowprops=dict(facecolor='black', arrowstyle='->'))

                # Show the plot
                plt.legend()
                plt.show()

                # Print the probability density at the user's IQ value
                print("The probability density at {} is {}".format(value, result))
            elif choice == 'b':
                import matplotlib.pyplot as plt
                num_rolls = int(input("Enter the number of dice rolls: "))
                dice_rolls = np.random.randint(1, 7, num_rolls)
                # Plot the histogram of dice rolls
                plt.hist(dice_rolls, bins=range(1, 8), density=True, alpha=0.7)
                plt.xlabel('Dice Roll')
                plt.ylabel('Probability Density')
                plt.title('Distribution of Dice Rolls')
                plt.grid(True)
                # Get user input for their desired dice roll
                value = int(input("Enter your desired dice roll (1-6): "))
                # Calculate the probability density of the desired dice roll
                result = np.sum(dice_rolls == value) / len(dice_rolls)
                # Plot a vertical line at the desired dice roll
                plt.axvline(x=value, color='r', linestyle='--', label='Your Desired Roll')
                # Find the rank of the desired dice roll among all dice rolls
                rank = np.sum(dice_rolls <= value) / len(dice_rolls)
                # Add a marker for the user's rank on the plot
                plt.annotate(f'Your Rank: {rank:.2%}', xy=(value, result), xytext=(value, result + 0.01),
                             arrowprops=dict(facecolor='black', arrowstyle='->'))
                # Show the plot
                plt.legend()
                plt.show()
                # Print the probability density of the desired dice roll
                print("The probability density of rolling a {} is {}".format(value, result))
            elif choice == 'c':
                import matplotlib.pyplot as plt
                mean = 10  # Average UK bus wait time in minutes
                # Generate bus wait times based on an exponential distribution
                bus_wait_times = np.random.exponential(mean, 1000)
                # Plot the histogram of bus wait times
                plt.hist(bus_wait_times, bins=30, density=True, alpha=0.7)
                plt.xlabel('Bus Wait Time (minutes)')
                plt.ylabel('Probability Density')
                plt.title('Distribution of Bus Wait Times')
                plt.grid(True)
                # Get user input for their average bus wait time
                value = float(input("Enter your average bus wait time (minutes):"))
                # Calculate the probability density at the user's average bus wait time
                result = mean * np.exp(-mean * value)
                # Plot a vertical line at the user's average bus wait time
                plt.axvline(x=value, color='r', linestyle='--', label='Your Average Wait Time')
                # Find the rank of the user's average bus wait time among UK bus wait times
                rank = np.sum(bus_wait_times <= value) / len(bus_wait_times)
                # Add a marker for the user's rank on the plot
                plt.annotate(f'Your Rank: {rank:.2%}', xy=(value, result), xytext=(value, result + 0.01),
                             arrowprops=dict(facecolor='black', arrowstyle='->'))
                # Show the plot
                plt.legend()
                plt.show()
                # Print the probability density at the user's average bus wait time
                print("The probability density at {} minutes is {}".format(value, result))
            
        else:
            print("Invalid choice. Please try again.")
    elif choice == '1':
        print("what type of discrete distribution would you like to view?")
        print("a. Binomial")
        print("b. Bernoulli")
        print("c. Geometric")
        choice = input("Enter choice (a/b/c):")
        if choice in ('a', 'b', 'c'):
            if choice == 'a':
                print("You're a world class striker with a conversion rate of 25.9%, How many shots would you like to take?")
                num1 = float(input("enter here:"))
                string_in_string = "On average, you scored {} goals".format(num1 * 0.259)
                print(string_in_string)
            elif choice == 'b':
                print("Take the red pill or blue pill")
                choice = input("Enter choice (red/blue)")
                if choice in ('red', 'blue'):
                    if choice == 'red':
                        print("further down the rabbit hole you go....")
                    elif choice == 'blue':
                        print("Back to 'reality' for you...")
            elif choice == 'c':
                print("Consider a game where you flip a fair coin until it comes up heads, you win fa^n where")
                num2 = float(input("enter your price:"))
                n = rdm.randint(1, 100)
                print(num2 ** n)
                string_in_string = "you had {} heads tossed till a tails was tossed!".format(n)
                print(string_in_string)
        else:
            print("Invalid choice. Please try again.")
    elif choice == '3':
        print("A random variable is a variable that takes on different values with certain probabilities.")
else:
    print("Invalid choice. Please try again.")