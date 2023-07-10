import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': r'C:\Users\timom\Downloads\all-project-files\chicago.csv',
    'new york': r'C:\Users\timom\Downloads\all-project-files\new_york_city.csv',
    'washington': r'C:\Users\timom\Downloads\all-project-files\washington.csv'
}


MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze. This was sprecifically requested in the project charter

    Returns:
        (str, str, str) city, month, day - Strings representing the city name, month, and day of the week
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = None
    month = None
    day = None

    # Get the city filter
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington? ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid input. Please enter a valid city name.')

    # Get the time filter
    while True:
        time_filter = input('Would you like to filter the data by month, day, or not at all? ').lower()
        if time_filter in ['month', 'day', 'none']:
            break
        else:
            print('Invalid input. Please enter "month", "day", or "none".')

    # Get the month or day filter if applicable
    month = None
    day = None

    if time_filter == 'month':
        while True:
            month = input('Which month - January, February, March, April, May, June, or all? ').lower()
            if month in MONTHS:
                break
            else:
                print('Invalid input. Please enter a valid month.')

    elif time_filter == 'day':
        while True:
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').lower()
            if day in DAYS:
                break
            else:
                print('Invalid input. Please enter a valid day.')

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - Name of the city to analyze
        (str) month - Name of the month to filter by, or None to apply no month filter
        (str) day - Name of the day of week to filter by, or None to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # Convert the 'Start Time' column to datetime type
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from the 'Start Time' column to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name().str.lower()

    # Apply month filter if applicable
    if month is not None and month != 'all':
        month_index = MONTHS.index(month) + 1
        df = df[df['Month'] == month_index]

    # Apply day filter if applicable
    if day is not None and day != 'all':
        df = df[df['Day of Week'] == day]

    return df

def popular_times_of_travel(df):
    """
    Displays the popular times of travel based on the start time.

    Args:
        df - Pandas DataFrame containing filtered city data
    """
    print('Popular times of travel (based on start time):\n')

    # Most common month
    if 'Month' in df.columns:
        start_time = time.time()
        most_common_month = df['Month'].mode()[0]
        if most_common_month != 13:  # Exclude 'all' option if chosen
            print('Most common month:', MONTHS[most_common_month - 1].title())
        else:
            print('Most common month: All')
        print("Execution time: %s seconds" % (time.time() - start_time))

    # Most common day of week
    if 'Day of Week' in df.columns:
        start_time = time.time()
        most_common_day = df['Day of Week'].mode()[0]
        print('Most common day of week:', most_common_day.title())
        print("Execution time: %s seconds" % (time.time() - start_time))

    # Most common hour of day
    if 'Start Time' in df.columns:
        start_time = time.time()
        df['Hour'] = df['Start Time'].dt.hour
        most_common_hour = df['Hour'].mode()[0]
        print('Most common hour of day:', most_common_hour)
        print("Execution time: %s seconds" % (time.time() - start_time))

    print('-' * 40)

def popular_stations_and_trips(df):
    """
    Displays the popular stations and trips.

    Args:
        df - Pandas DataFrame containing filtered city data
    """
    print('Popular stations and trips:\n')

    # Most common start station
    if 'Start Station' in df.columns:
        start_time = time.time()
        most_common_start_station = df['Start Station'].mode()[0]
        print('Most common start station:', most_common_start_station)
        print("Execution time: %s seconds" % (time.time() - start_time))

    # Most common end station
    if 'End Station' in df.columns:
        start_time = time.time()
        most_common_end_station = df['End Station'].mode()[0]
        print('Most common end station:', most_common_end_station)
        print("Execution time: %s seconds" % (time.time() - start_time))

    # Most common trip from start to end
    if 'Start Station' in df.columns and 'End Station' in df.columns:
        start_time = time.time()
        df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
        most_common_trip = df['Trip'].mode()[0]
        print('Most common trip from start to end:', most_common_trip)
        print("Execution time: %s seconds" % (time.time() - start_time))

    print('-' * 40)

def trip_duration(df):
    """
    Displays the total and average trip duration.

    Args:
        df - Pandas DataFrame containing filtered city data
    """
    print('Trip duration:\n')

    # Total travel time
    if 'Trip Duration' in df.columns:
        start_time = time.time()
        total_travel_time = df['Trip Duration'].sum()
        print('Total travel time:', total_travel_time)
        print("Execution time: %s seconds" % (time.time() - start_time))

    # Average travel time
    if 'Trip Duration' in df.columns:
        start_time = time.time()
        average_travel_time = df['Trip Duration'].mean()
        print('Average travel time:', average_travel_time)
        print("Execution time: %s seconds" % (time.time() - start_time))

    print('-' * 40)

def user_info(df, city):
    """
    Displays user information.

    Args:
        df - Pandas DataFrame containing filtered city data
        city - Name of the city being analyzed
    """
    print('User info:\n')

    # Counts of each user type
    if 'User Type' in df.columns:
        start_time = time.time()
        user_type_counts = df['User Type'].value_counts()
        print('Counts of each user type:')
        print(user_type_counts)
        print("Execution time: %s seconds" % (time.time() - start_time))

    if city in ['chicago', 'new york']:
        # Counts of each gender
        if 'Gender' in df.columns:
            start_time = time.time()
            gender_counts = df['Gender'].value_counts()
            print('\nCounts of each gender:')
            print(gender_counts)
            print("Execution time: %s seconds" % (time.time() - start_time))

        # Earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns:
            start_time = time.time()
            earliest_birth_year = int(df['Birth Year'].min())
            most_recent_birth_year = int(df['Birth Year'].max())
            most_common_birth_year = int(df['Birth Year'].mode()[0])

            print('\nEarliest year of birth:', earliest_birth_year)
            print('Most recent year of birth:', most_recent_birth_year)
            print('Most common year of birth:', most_common_birth_year)
            print("Execution time: %s seconds" % (time.time() - start_time))

    print('-' * 40)

def display_raw_data(df):
    """
    Displays raw data upon request by the user.

    Args:
        df - Pandas DataFrame containing filtered city data
    """
    i = 0
    while True:
        show_raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no: ')
        if show_raw_data.lower() == 'yes':
            print(df.iloc[i:i+5])
            i += 5
        elif show_raw_data.lower() == 'no':
            break
        else:
            print('Invalid input. Please enter either "yes" or "no".')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        popular_times_of_travel(df)
        popular_stations_and_trips(df)
        trip_duration(df)
        user_info(df, city)

        display_raw_data(df)

        restart = input('\nWould you like to restart and explore another city? Enter yes or no: ')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


    print('-'*40)
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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no. Please make no other inputs\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
