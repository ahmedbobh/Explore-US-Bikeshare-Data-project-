import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def view_rows(df):
    z=0
    while True:
        z=z+5
        display_rows= input('\nWould you like to display first ' + str(z) +' raw data ? Enter :\n1)yes\n2)no\n').lower()
        
        if display_rows=='yes'and z<len(df.index):
            print(df.head(z))
            continue;
        if display_rows =='no':
            break;
        if display_rows not in ['yes','no']:
            print('invalid input please type yes or no')
            continue;
     
    
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
    cities=['chicago','new york city','washington']
    city=''
    while city not in cities:
       
        city=input('select chicago , new york city , washington  :').lower()
        if city not in cities:
            print('Oops! Incorrect input. Select city again')
        

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march','april','may','june']
    month=''
    while month not in months:
        month = input('Select january , february , march , april , may or june :').lower()
        if month not in months:
            print('Oops! Incorrect input. Select month again')
  

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days= ['monday', 'tuesday', 'wednesday','thursday','saturday','friday','sunday']
    day = ''
    while day not in days:
        day = input('Select monday , tuesday , wednesday , thursday , friday , saturday :').lower()
        if day not in days:
           day = print('Oops! Incorrect input. Select day of week again')
        

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    df = df[df['month']==month]
    if day != 'all':
        df = df[df['day_of_week']==day.capitalize()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('most common month :', common_month)
    # display the most common day of week
    common_day=df['day_of_week'].value_counts().idxmax()
    print('most common day of week :',common_day)
    # display the most common start hour
    common_hour=df['hour'].value_counts().idxmax()
    print('most common start hour :',common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station=df['Start Station'].value_counts().idxmax()
    print('most common used start station :',common_start_station)
    
    # display most commonly used end station
    common_endstation=df['End Station'].value_counts().idxmax()
    print('most common used end station :',common_endstation)

    # display most frequent combination of start station and end station trip
    
    most_popular_trip = df.groupby(["Start Station", "End Station"]).size().idxmax()
    print('most frequent combination of start station and end station trip :',most_popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trtime=df['Trip Duration'].sum()
    print('total travel time :',total_trtime)

    # display mean travel time
    mean_trtime=df['Trip Duration'].mean()
    print('mean travel time :',mean_trtime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_usertypes=df['User Type'].value_counts()
    print('counts of user types :',counts_usertypes)
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")

    #Similarly, this try clause is there to ensure only df containing
    #'Birth Year' column are displayed
    #The earliest birth year, most recent birth year and the most common
    #birth years are displayed
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year details in this file.")


    # Display earliest, most recent, and most common year of birth
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        view_rows(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
