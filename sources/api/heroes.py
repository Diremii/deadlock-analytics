# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    heroes.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas <humontas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 03:58:43 by humontas          #+#    #+#              #
#    Updated: 2026/09/06 12:57:14 by humontas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from api.client import query_deadlock_api


def get_heroes():
	return query_deadlock_api("SELECT id, name " \
							  "FROM heroes")