# finds the lowest, highest and average score from a list
def get_stats(stats_list):

    # sort the lists.
    stats_list.sort()

    # find lowest, highest and average scores...
    lowest_score = stats_list[0]
    highest_score = stats_list[-1]
    average_score = sum(stats_list) / len(stats_list)

    return [lowest_score, highest_score, average_score]


# create lists to hold user and computer scores
user_scores = [10, 0, 13, 7, 10, 11]
comp_scores = [10, 11, 0, 0, 10, 11]

# Loop six times - for testing purposes, ask the user to enter the
# score for the user and the computer for each round
# for item in range(0, 6):
#     user_score = int(input("Enter the user score: "))
#     comp_score = int(input("Enter the computer score: "))
#
#     # add user & computer score to lists!
#     user_scores.append(user_score)
#     comp_scores.append(comp_score)

# calculate the lowest, highest and average
# scores and display them.

user_stats = get_stats(user_scores)
comp_stats = get_stats(comp_scores)

print("📊📊📊 Game Statistics 📊📊📊 ")
print(f"User - Lowest Score: {user_stats[0]}\t "
      f"Highest Score: {user_stats[1]}\t "
      f"Average Scores: {user_stats[2]}")

print(f"Computer - Lowest Score: {comp_stats[0]}\t "
      f"Highest Score: {comp_stats[1]}\t "
      f"Average Scores: {comp_stats[2]}")
