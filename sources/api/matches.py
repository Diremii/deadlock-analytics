# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matches.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas <humontas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 10:56:27 by humontas          #+#    #+#              #
#    Updated: 2026/09/05 14:26:23 by humontas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import timedelta

from api.client import query_deadlock_api


def get_matches_for_period(start_date, end_date):
	print(f"⏳ Fetching matches from {start_date} to {end_date} — this may take a while depending on volume...")
	query = f"SELECT match_id, start_time, hero_id, won, items.item_id \
			  FROM match_player \
			  WHERE start_time >= '{start_date}' \
			  AND start_time < '{end_date + timedelta(days=1)}' \
			  AND match_mode='Ranked'" 
	result = query_deadlock_api(query)
	return result