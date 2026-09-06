# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas <humontas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/02 15:59:58 by humontas          #+#    #+#              #
#    Updated: 2026/09/06 12:55:16 by humontas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import date, datetime


MIN_DATE = date(2026, 7, 30)

def get_date(prompt):
	max_date = date.today()

	while True:
		try:
			d = datetime.strptime(input(prompt), "%Y-%m-%d").date()
			if MIN_DATE <= d <= max_date:
				return d
			print(f"❌ Date must be between {MIN_DATE} and {max_date}.")
		except ValueError:
			print("❌ Invalid date. Please use YYYY-MM-DD.")

def get_date_range():
	start_date = get_date("Start date (YYYY-MM-DD): ")

	while True:
		end_date = get_date("End date (YYYY-MM-DD): ")
		if end_date >= start_date:
			return start_date, end_date
		print("❌ End date cannot be before start date.")