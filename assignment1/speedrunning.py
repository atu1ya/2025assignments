# Name: Atulya Chaturvedi
# Student Number: 24225113

class Leaderboard:
    """A leaderboard of speedrunning record times.

    Each entry has a time in seconds and a runner name.
    Runners may submit multiple runs.
    The leaderboard is ranked fastest run first.
    Ties receive the same rank as each other, so for example if runners submit
    the times 10, 20, 20, and 30, they will have the ranks 1, 2, 2, and 4.
    """

    def __init__(self, runs):
        """Constructs a leaderboard with the given runs.
        The given list of runs is not required to be in order.
        Args:
            runs: Initial leaderboard entries as list of (time, name) pairs.
        """

        # Helper function to merge two sorted lists into one sorted list
        def merge(S1, S2, S):
            i = j = 0
            while i + j < len(S):
                # Compare elements from both lists and add the smaller one to the result
                if j == len(S2) or (i < len(S1) and (
                        S1[i][0] < S2[j][0] or 
                        (S1[i][0] == S2[j][0] and S1[i][1] < S2[j][1])
                    )):
                    S[i+j] = S1[i]
                    i += 1
                else:
                    S[i+j] = S2[j]
                    j += 1
            return S

        # Recursive merge sort function to sort the runs
        def merge_sort(runs):
            n = len(runs)
            if n < 2:  # Base case: a list of 0 or 1 elements is already sorted
                return runs
            else:
                mid = n // 2
                runs1 = runs[0:mid]  # Split the list into two halves
                runs2 = runs[mid:n]
                runs1 = merge_sort(runs1)  # Recursively sort the first half
                runs2 = merge_sort(runs2)  # Recursively sort the second half
                return merge(runs1, runs2, [None] * n)  # Merge the sorted halves

        # Sort the runs and store them in the leaderboard
        self.leaderboard = merge_sort(runs) if runs else []
        
    def get_runs(self):
        """Returns the current leaderboard.

        Leaderboard is given in rank order, tie-broken by runner name.

        Returns:
            The current leaderboard as a list of (time, name) pairs.
        """
        return self.leaderboard

    def submit_run(self, time, name):
        """Adds the given run to the leaderboard

        Args:
            time: The run time in seconds.
            name: The runner's name.
        """
        data = self.leaderboard

        # Binary search to find the correct position to insert the new run
        def binsearch(data, time, name):
            low = 0
            high = len(data) - 1
            while low <= high:
                mid = (low + high) // 2
                # Compare the current run with the target run
                if data[mid][0] < time or (data[mid][0] == time and data[mid][1] < name):
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        # Find the insertion index and insert the new run
        index = binsearch(data, time, name)
        data.insert(index, (time, name))

    def get_rank_time(self, rank):
        """Get the time required to achieve at least a given rank.

        For example, get_rank_time(5) will give the maximum possible time
        that would be ranked fifth.

        Args:
            rank: The rank to look up.

        Returns:
            The time required to place rankth or better.
        """
        # Check if the rank is valid
        if not self.leaderboard or rank <= 0 or rank > len(self.leaderboard):
            return None
        # Return the time of the run at the given rank
        return self.leaderboard[rank - 1][0]
    

    def get_possible_rank(self, time):
        """Determine what rank the run would get if it was submitted.
    
        Does not actually submit the run.
    
        Args:
            time: The run time in seconds.
    
        Returns:
            The rank this run would be if it were to be submitted.
        """
        # If the leaderboard is empty, the run would be ranked first
        if not self.leaderboard:
            return 1
        
        # Binary search to find the rank for the given time
        low = 0
        high = len(self.leaderboard) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.leaderboard[mid][0] < time:
                low = mid + 1
            else:
                high = mid - 1
        
        # Return the rank (1-based index)
        return low + 1

    def count_time(self, time):
        """Count the number of runs with the given time.

        Args:
            time: The run time to count, in seconds.

        Returns:
            The number of submitted runs with that time.
        """
        # If the leaderboard is empty, there are no runs to count
        if not self.leaderboard:
            return 0
        
        # Helper function to find the first occurrence of the given time
        def find_first(time):
            low = 0
            high = len(self.leaderboard) - 1
            result = -1
            while low <= high:
                mid = (low + high) // 2
                if self.leaderboard[mid][0] == time:
                    result = mid
                    high = mid - 1  # Continue searching in the left half
                elif self.leaderboard[mid][0] < time:
                    low = mid + 1
                else:
                    high = mid - 1
            return result
            
        # Helper function to find the last occurrence of the given time
        def find_last(time):
            low = 0
            high = len(self.leaderboard) - 1
            result = -1
            while low <= high:
                mid = (low + high) // 2
                if self.leaderboard[mid][0] == time:
                    result = mid
                    low = mid + 1  # Continue searching in the right half
                elif self.leaderboard[mid][0] < time:
                    low = mid + 1
                else:
                    high = mid - 1
            return result
        
        # Find the first and last occurrences of the given time
        first = find_first(time)
        if first == -1:  # If the time is not found, return 0
            return 0
        
        last = find_last(time)
        # Return the count of runs with the given time
        return last - first + 1