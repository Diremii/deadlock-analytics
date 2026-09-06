# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    client.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas <humontas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/04 01:34:55 by humontas          #+#    #+#              #
#    Updated: 2026/09/05 14:26:54 by humontas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import requests


def query_deadlock_api(query):
	success = False
	while not success:
		response = requests.get(
			"https://api.deadlock-api.com/v1/sql/",
			params={"query": query}
		)
		result = response.json()
		if isinstance(result, list):
			success = True
		else:
			wait_time = result["error"]["next_request_in"]
			wait_time = max(wait_time, 5) + 2
			time.sleep(wait_time)
	return result