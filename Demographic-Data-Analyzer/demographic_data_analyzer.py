import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = {}
    for race in df['race']:
        if race in race_count:
            race_count[race] += 1
        else:
            race_count[race] = 1
    race_count = pd.Series(data=race_count)

    # What is the average age of men?
    sum_age_men = 0
    no_of_men = 0
    for age, sex in zip(df["age"], df["sex"]):
        if sex == "Male":
            no_of_men += 1
            sum_age_men += age
    average_age_men = round(sum_age_men / no_of_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    no_of_people = 0
    no_of_bachelors = 0
    for degree in df['education']:
        no_of_people += 1
        if degree == "Bachelors":
            no_of_bachelors += 1
    percentage_bachelors = round(no_of_bachelors / no_of_people * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = 0
    lower_education = 0
    # percentage with salary >50K
    higher_education_rich = 0
    lower_education_rich = 0
    for education, salary in zip(df['education'], df['salary']):
        if education in ('Bachelors', 'Masters', 'Doctorate'):
            higher_education += 1
            if salary == '>50K':
                higher_education_rich += 1
        else:
            lower_education += 1
            if salary == '>50K':
                lower_education_rich += 1
    lower_education_rich = round(lower_education_rich / lower_education * 100, 1)
    higher_education_rich = round(higher_education_rich / higher_education * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None
    for hours in df['hours-per-week']:
        if min_work_hours is None or hours < min_work_hours:
            min_work_hours = hours

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = 0
    min_work_hours_rich = 0
    for hours, salary in zip(df['hours-per-week'], df['salary']):
        if hours == min_work_hours:
            if salary == '>50K':
                min_work_hours_rich += 1
            num_min_workers += 1
    rich_percentage = round(min_work_hours_rich / num_min_workers * 100)

    # What country has the highest percentage of people that earn >50K?
    country_earnings = {}
    for country, salary in zip(df['native-country'], df['salary']):
        if country in country_earnings:
            country_earnings[country][1] += 1
        else:
            country_earnings[country] = [0, 1]
        if salary == ">50K":
            country_earnings[country][0] += 1

    highest_earning_country = max(country_earnings, key=lambda x: country_earnings[x][0] / country_earnings[x][1])
    highest_earning_country_percentage = round(country_earnings[highest_earning_country][0] / country_earnings[highest_earning_country][1] * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation_dict = {}
    for occupation, country, salary in zip(df["occupation"], df["native-country"], df["salary"]):
        if country == "India" and salary == ">50K":
            if occupation in top_IN_occupation_dict:
                top_IN_occupation_dict[occupation] += 1
            else:
                top_IN_occupation_dict[occupation] = 1
    top_IN_occupation = max(top_IN_occupation_dict, key=lambda x: top_IN_occupation_dict[x])

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }