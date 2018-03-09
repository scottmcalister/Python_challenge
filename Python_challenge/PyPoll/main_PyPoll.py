import csv

file_num = 1

upload_file = 'election_data_' + str(file_num) + '.csv'

votes = 0
winner_votes = 0
total_num_candidates = 0
most_votes = ["", 0]
candidate_options = []
candidate_votes = {}

with open(upload_file) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        votes = votes + 1
        total_num_candidates = row['Candidate']
        if row['Candidate'] not in candidate_options:
            candidate_options.append(row['Candidate'])
            candidate_votes[row['Candidate']] = 1
        else:
            candidate_votes[row['Candidate']] = candidate_votes[row['Candidate']] + 1

    print("Election Results")
    print("-------------------")
    print("Total Votes" + str(votes))
    for candidate in candidate_votes:
        print(candidate + ' ' + str(round(((candidate_votes[candidate]/votes)*100))) + '%' + ' (' + str(candidate_votes[candidate]) + ')')
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + '%' + '(' + str(candidate_votes[candidate]) + ')')
candidate_votes
winner = sorted(candidate_votes.items())

print("---------------")
print("Winner: " + str(winner[0]))