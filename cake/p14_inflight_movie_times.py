def inflight_combine_times(flight_time, movie_times):
    differences = [0] * (flight_times + 1)
    for single_movie_time in movie_times:
        if differences[single_movie_time] >= 0:
            return True
        time_difference = flight_time - single_movie_time
        if time_difference > 0:
            differences[time_difference] += 1
    return False