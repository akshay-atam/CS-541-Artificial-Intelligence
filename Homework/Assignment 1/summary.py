import pandas as pd

def summary_statistics(state):
    #Start your code implementation from here
    df = pd.read_csv("data.txt", delimiter=',')

    # get data of specific state
    state_summary = df[df['state'] == state]

    # store each value in a variable
    min_cases = state_summary['cases'].min()
    max_cases = state_summary['cases'].max()
    mean_cases = state_summary['cases'].mean()
    std_cases = state_summary['cases'].std()

    return min_cases, max_cases, mean_cases, std_cases

def main():
    #The output should contain Minimum, Maximum, Standard deviation and Mean, each data in separate line in below given order:
    #Minimum:
    #Maximum:
    #Mean:
    #Standard Deviation:
    ip_state = input("Enter state: ")
    m, M, mean, std = summary_statistics(ip_state)
    print(f" Minimum: {m}\n Maximum: {M}\n Mean: {mean}\n Standard Deviation: {std}")

if __name__ == "__main__":
    main()