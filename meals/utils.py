from datetime import datetime, timedelta


def get_available_dates(current_date: datetime, subscription_days: int) -> tuple:
    # Calculate the end date based on the current date and subscription days
    end_date = current_date + timedelta(days=subscription_days)

    # Initialize variables
    date_list = []  # store all days
    message = ''

    # Check if the current time is after 4:00 PM
    if current_date.time().hour >= 16:
        end_date += timedelta(days=1)
        current_date += timedelta(days=1)
        message = "You cannot subscribe after 4:00 PM"

    # Iterate through each day
    while current_date != end_date:
        # Check if the current date is not a Friday or Saturday
        if current_date.weekday() != 4 and current_date.weekday() != 5:
            date_list.append(current_date.date())

        # Move to the next day
        current_date += timedelta(days=1)

    return date_list, message