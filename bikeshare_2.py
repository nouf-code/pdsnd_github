import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# this method to get the input from the user
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid Input Please provide valid input.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Depending on which month you want to filter the data? Choose one of these[all,January, "
                      "February, "
                      "March, April, May, or June] ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid Input Please provide valid input.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Depending on which day you want to filter the data? Choose one of these[all, Sunday, Monday, "
                    "Tuesday, Wednesday, Thursday, Friday, or Saturday] ").lower()
        if day in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            break
        else:
            print("Invalid Input Please provide valid input.")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Read the city file
    df = pd.read_csv(CITY_DATA[city])

    # Convert the dtype of Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month
    df['month'] = df['Start Time'].dt.month
    # extract day
    df['day'] = df['Start Time'].dt.day_name().str.lower()

    # filtering by month and day
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month : ", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day'].value_counts().idxmax()
    print("The most common day of week : ", most_common_day)

    # TO DO: display the most common start hour
    df['hours'] = df['Start Time'].dt.hour
    most_start_time = df['hours'].value_counts().idxmax()
    print("The most common start hour : ", most_start_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station : ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station : ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_start_end_station = df.groupby('Start Station')['End Station'].value_counts().idxmax()
    print("The most frequent combination of start station and end station trip : ", most_frequent_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print("The counts of user types:\n", counts_of_user_types)

    if city != 'washington':
        # Replace Nan value
        df['Gender'] = df['Gender'].fillna(df['Gender'].value_counts().idxmax())
        df['Birth Year'] = df['Birth Year'].fillna(df['Birth Year'].median())
        # print(df.info())

        # TO DO: Display counts of gender
        counts_of_gender = df['Gender'].value_counts()
        print("\nThe counts of gender:\n", counts_of_gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("\nThe earliest year of birth: ", earliest_year)
        most_recent_year = df['Birth Year'].max()
        print("The most recent year of birth: ", most_recent_year)
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print("The most common year of birth: ", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)




        # Print 5 row of data
        i = 0
        while True:
            data = input('\nWould like to see the raw data? Enter yes or no.\n')
            if data.lower() == 'yes':
                print(df[i:i + 5])
                i += 5
            else:
                break




        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
